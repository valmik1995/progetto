from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_id = models.CharField(max_length=50, null=True, blank=True)
    tweet_text = models.TextField()
    retweet = models.IntegerField()
    like  = models.IntegerField()
    url = models.CharField(max_length=250, null=True)
    media_url= models.URLField(max_length=250, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
   
    def __str__(self):
        return self.tweet_text