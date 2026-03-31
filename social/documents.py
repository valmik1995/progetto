from django_elasticsearch_dsl import Document, fields
from elasticsearch_dsl import analyzer, tokenizer
from django_elasticsearch_dsl.registries import registry
from social.models import Tweet

autocomplete_analyzer = analyzer('autocomplete_analyzer',
                                 tokenizer=tokenizer(
                                     'trigram', 'nGram', min_gram=1, max_gram=20),
                                 filter=['lowercase']
                                 )


@registry.register_document
class TweetDocument(Document):
    class Index:
        name = 'socials'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0,
        'max_ngram_diff': 20,
    }
    class Django:
         model = Tweet
         fields = [
             'tweet_text',
             'media_url',
             'published_date',
             'url',
             'like',
             'retweet',
         ]




