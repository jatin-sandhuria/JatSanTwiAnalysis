import sys
import tweepy


class AuthenticationAPI:
    def authentication(self):

        # Consumer keys and access tokens, used for OAuth
        consumer_key = 'Dnx9DXVyAksxONOH5RdGkq9EC'
        consumer_secret = 'mnvbBLmm2R7fCqFhAqz4TY4Eb1yMXqs0ys7ilCXgAazEJi9uUr'
        access_token = '1250598696-yqIBBwBqsvgU1A4XZ7ZUXrHzfPSLJXLBlJdSq23'
        access_token_secret = 'f4vZeAkrLK5QfeW4w5MfRlyxjnBdVeBdwxa8mQBrEJH1o'

        # OAuth process, using the keys and tokens
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        # Creation of the actual interface, using authentication
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        if (not api):
            print("Can't Authenticate")
            sys.exit(-1)
        return api
