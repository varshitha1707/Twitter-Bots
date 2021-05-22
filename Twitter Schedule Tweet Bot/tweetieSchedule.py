import tweepy
import time

auth = tweepy.OAuthHandler('--insert API Key--','--insert API secret Key--')
auth.set_access_token('--insert Access Token--','--insert Secret Access Token--')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user =  api.me()

tweets = ['Enter','your','tweets']

current_time = '23:40:50' #--enter the time at which you want to upload

while(tweets):
        t = time.localtime()
        timehai = time.strftime("%H:%M:%S", t)
        if(current_time==timehai):
            for i in tweets:
                api.update_status(i)
                print('Tweeted')
                time.sleep(60)
            break       
