import tweepy
import time

auth = tweepy.OAuthHandler('--insert API Key--','--insert API secret Key--')
auth.set_access_token('--insert Access Token--','--insert Secret Access Token--')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user =  api.me()

search = 'deliver' , 'pune'    
nrTweets = 5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break        

