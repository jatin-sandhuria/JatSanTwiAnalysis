import sys,yweather
import tweepy

class TrendingTweets:
    client = yweather.Client()

    def getTrends(self, countryName, apiTweet):
        woeid = (TrendingTweets.client.fetch_woeid(countryName))

        print("Top trends for " + countryName + " which has woeid " + str(woeid))

        trend = (apiTweet.trends_place(woeid))
        data = trend[0]
        # grab the trends
        trends = data['trends']
        # grab the name from each trend
        # print(trends)
        dict = {}
        for trend in trends:
            volume = str([trend['tweet_volume']]).replace("[", "").replace("]", "")
            trendName = trend['name']
            # print(volume)
            if (str(volume).isdigit() is True and "#" in trendName):
                dict[trendName] = int(volume)

        a1_sorted_keys = sorted(dict, key=dict.get, reverse=True)
        for r in a1_sorted_keys:
            print(r, dict[r])

        print("")
