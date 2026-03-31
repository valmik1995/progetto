# #!/usr/bin/env python
# # encoding: utf-8

# import tweepy
# from social.models import Tweet

# #VALMIK1995
# # CONSUMER_KEY = 'XK1j7YqCgd5Is4dSxjwPDZoVS'
# # CONSUMER_SECRET = 'tJhy6CydJXRgoJW43681ex32Pv0VRBU9RevWN405mZgv5rrXWI'
# # ACCESS_TOKEN = '180315787-Kndf3zPFddI0eS1rmrDwEWj8zKvcYINlwuvyleav'
# # ACCESS_TOKEN_SECRET = 'mOfFKxnBJjMaT1FboAmg8FvHW5vBeMc8a7hIzMIaLSwjq'

# #EMERGENZAVVF
# CONSUMER_KEY = 'bmySN5h92wU6lRqud12CUAV31'
# CONSUMER_SECRET = 'juZv54dYaPCa3kZWkqiHasm1FFosPuHCPSkksQ7zhdUFUPW1Tt'
# ACCESS_TOKEN = '702594325625085952-0ryjivDCoNU56hkhoV5QiZEbvgeHYo8'
# ACCESS_TOKEN_SECRET = 'O4iesS2rXpayk2P6q1KjXBmyKs8nC9P5d0CvXlC5b3Co0'


# consumer_key = CONSUMER_KEY
# consumer_secret = CONSUMER_SECRET
# access_key = ACCESS_TOKEN
# access_secret = ACCESS_TOKEN_SECRET


# screen_name = 'vigilidelfuoco'
# # screen_name = 'valmik1995'

# #authorize twitter, initialize tweepy
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)
# api = tweepy.API(auth)

# #initialize a list to hold all the tweepy Tweets
# alltweets = []

# #make initial request for most recent tweets (200 is the maximum allowed count)
# new_tweets = api.user_timeline(screen_name=screen_name, tweet_mode='extended', count=200)

# #save most recent tweets
# alltweets.extend(new_tweets)

# #save the id of the oldest tweet less one
# oldest = alltweets[-1].id - 1

# #keep grabbing tweets until there are no tweets left to grab
# while len(new_tweets) > 0:
#     print(f"getting tweets gefore {oldest}")

#     screen_name = 'vigilidelfuoco'
#     # screen_name = 'valmik1995'

#     #all subsiquent requests use the max_id param to prevent duplicates
#     new_tweets = api.user_timeline(screen_name=screen_name, tweet_mode='extended', count=200, max_id=oldest)

#     #save most recent tweets
#     alltweets.extend(new_tweets)

#     #update the id of the oldest tweet less one
#     oldest = alltweets[-1].id - 1

#     print(f"...{len(alltweets)} tweets downloaded so far")

#     nuovo = []
#     for tweet in alltweets:
#         if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
#             tweet_record = {}
#             # tweet_record['tweet.text'] = tweet.full_text
#             tweet_record['id'] = tweet.id_str
#             tweet_record['tweet.text'] = tweet.full_text
#             # tweet_record['tweet.user.name'] = tweet.user.name
#             # tweet_record['tweet.user.location'] = tweet.user.location
#             # tweet_record['tweet.user.verified'] = tweet.user.verified
#             # tweet_record['tweet.lang'] = tweet.lang
#             # tweet_record['tweet.created_at'] = tweet.created_at
#             # tweet_record['tweet.user'] = tweet.user
#             tweet_record['retweet_count'] = tweet.retweet_count
#             tweet_record['favorite_count'] = tweet.favorite_count

#             try:
#                 tweet_record['display_url'] = tweet.extended_entities['media'][0]['url']
#             except AttributeError:
#                 tweet_record['display_url'] = 'none'

#             try:
#                 tweet_record['media.url'] = tweet.extended_entities['media'][0]['video_info']['variants'][1]['url']
#             except KeyError:
#                 tweet_record['media.url'] = tweet.extended_entities['media'][0]['media_url']
#             except IndexError:
#                 tweet_record['media.url'] = tweet.extended_entities['media'][0]['media_url']
#             except AttributeError:
#                 tweet_record['media.url'] = 'none'

#             tweet_record['tweet.created_at'] = tweet.created_at

#             nuovo.append(tweet_record)


def save_to_db():
    for test in nuovo:
        values = test.values()
        values_list = list(values)
        if not Tweet.objects.filter(tweet_id=values_list[0]):
            new_tweet = Tweet(tweet_id=values_list[0], tweet_text=values_list[1],  retweet=values_list[2],
                              like=values_list[3], url=values_list[4], media_url=values_list[5], published_date=values_list[6])
            new_tweet.save()

