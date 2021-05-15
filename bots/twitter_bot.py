import os
import tweepy


class Twitter_bot:
    def __init__(self):
        self.creds = {
            "consumer_key": os.environ['CONSUMER_KEY'],
            "consumer_secret": os.environ['CONSUMER_SECRET'],
            "access_token": os.environ['ACCESS_TOKEN'],
            "access_token_secret": os.environ['ACCESS_TOKEN_SECRET']
        }
        self.api = self.create_api(self.creds['consumer_key'], 
                                    self.creds['consumer_secret'], 
                                    self.creds['access_token'], 
                                    self.creds['access_token_secret']
        )

    # Authenticate to Twitter
    def authenticate_api(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

    # verifies credentials; returns message depending on the result
    def verify_credentials(self, api):
        try:
            api.verify_credentials()
            print("Authentication OK")
        except Exception as e:
            print("Error during authentication")
            raise e

    # creates api object & checks for authentication validation
    def create_api(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = self.authenticate_api(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        self.verify_credentials(api)
        return api

    # 'likes' 'count' number of tweets with 'keyword' in them
    # if location == global. If location == feed, then keyword is neglected
    def favorite_tweets(self, location, count, keyword=None):
        if location == 'global':
            cursor = tweepy.Cursor(self.api.search, q=keyword)
        else:
            cursor = tweepy.Cursor(self.api.home_timeline)

        for tweet in cursor.items(count):
            try:
                tweet.favorite()
            except tweepy.TweepError as e:
                print(e.reason)

    # follows a follower if not following yet
    def follow_followers(self):
        everyone = tweepy.Cursor(self.api.followers).items()
        count = 5
        for person in everyone:
            if count > 0:
                if not person.following:
                    person.follow()
            count -= 1

    # simple function for tweeting some input content
    def tweet(self, content):
        self.api.update_status(content)