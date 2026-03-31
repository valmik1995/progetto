import re
from django.http import response
from django.shortcuts import render
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect
from elasticsearch_dsl import Q
from elasticsearch_dsl import Search
from social.models import Tweet
from social.twitter import save_to_db
from social.documents import TweetDocument
from social.forms import SearchForm  
from social.helpers import SearchResults
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required
def tweet_list(request):
    tweets = Tweet.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tweets, 100)
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)
    return render(request, 'social/tweet_list.html', {'tweets': tweets})


def set_inactive(pk):
    Tweet.objects.filter(tweet_id = pk).update(is_active = False)

def set_active(pk):
    Tweet.objects.filter(tweet_id = pk).update(is_active = True)

@login_required
def tweet_set_inactive(request, pk):
    set_inactive(pk)
    return redirect('social:tweet_list')

@login_required
def tweet_set_active(request, pk):
    set_active(pk)
    return redirect('social:tweet_list')


@login_required
def tweet_fetch(request):
    save_to_db()
    return redirect('social:tweet_list')


def search(request):
    pattern = "^[0-9_-]*$"
    q = request.GET.get('q')

    
    if re.match(pattern, q):
        if len(q) == 10:
            first_days = last_days = q
        elif len(q) == 7:
            c = q[5:7]
            if c == '04' or c == '06' or c == '09' or c == '11':
                last_days = '-30'
            elif c == '02':
                last_days = '-29'
            else:
                last_days = '-31'

            first_days = q + '-01'
            last_days = q + last_days

        elif len(q) == 4:
            first_days = q + '-01-01'
            last_days = q + '-12-31'

        tweets = TweetDocument.search().extra(size=100).filter("range", published_date={
            "gte": first_days, "lte": last_days}).sort('-like')
    elif q.isalnum():
        tweets = TweetDocument.search().extra(size=100).filter(
            "match", tweet_text="dog").sort('-like')
    else:
        pass

    paginate_by = 20
    search_results = SearchResults(tweets)
    paginator = Paginator(search_results, paginate_by)
    page_number = request.GET.get("page")
    
    try:
        tweets = paginator.page(page_number)
    except PageNotAnInteger:
        # If page parameter is not an integer, show first page.
        tweets = paginator.page(1)
    except EmptyPage:
        # If page parameter is out of range, show last existing page.
        tweets = paginator.page(paginator.num_pages)


    return render(request, 'social/search.html', {'tweets': tweets})


class CategoryElasticSearch(LoginRequiredMixin, ListView):
    template_name = 'social/view.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['search_term'] = self.request.GET.get('q')
        return context  
    
    def get_queryset(self):
        request = self.request
        search_term = request.GET.get('q', None)
        order = request.GET.get('r')
        
        if search_term is not None:
            q = Q("multi_match", query=search_term, fields=['tweet_text'], operator= 'AND')
            s = Search().sort(order)
            s = s.query(q)
            self.count = s.count()
            results = s[0:self.count].execute()
            return results

        tweets = Tweet.objects.order_by('-id')
        return tweets


class SearchResultsView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'social/search_results.html'
    paginate_by = 15
    count = 0
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['term'] = self.request.GET.get('q')
        context['date'] = self.request.GET.get('d')
        return context

    def get_queryset(self):
        request = self.request
        term = request.GET.get('q')
        date = request.GET.get('d')
        order = request.GET.get('r')

        
        if term and date:
            q = Q("match", tweet_text=term) & Q("range", published_date={"gte": str(date + '-01-01'), "lt": str(date +'-12-31'), "format": "yyyy-MM-dd"})
        elif term != "":
            q = Q("match", tweet_text=term)
        elif date != "":
            q = Q("range", published_date={"gte": str(date + '-01-01'), "lt": str(date +'-12-31'), "format": "yyyy-MM-dd"})
        else:
            pass
            
        s = Search().sort(order)
        s = s.query(q)
        self.count = s.count()
        results = s[0:self.count].execute()

        return results



# class SearchResultsView(ListView):
#     model = Tweet
#     context_object_name = "object"
#     template_name = 'social/search_results.html'

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         test = query.split(" ")
#         print(test[0])
#         vector = SearchVector('tweet_text', 'published_date' , config='english')
#         query = SearchQuery("(" + test[0] + ") & (" + test[1] + ")", search_type="raw")
#         return Tweet.objects.annotate(search=vector).filter(search=query)