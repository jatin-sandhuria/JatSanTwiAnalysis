from TwitterAnalysisHashTag import Analysis;
from Authentication import AuthenticationAPI;
from Trending import TrendingTweets;
from GetGeoLocation import FIndGeoLocation;
from GetGeocoder import GeoCoder2

class MainProgram:

    if __name__ == "__main__":
        auth = AuthenticationAPI();
        trend = TrendingTweets()
        tweet = Analysis()
        geo = FIndGeoLocation
        geoC = GeoCoder2
        fileName = "HappyBirthdayGurudev_Y2017_.csv"
        tweet.createFile(fileName)

        api = auth.authentication();

        #trend.getTrends('India', api)
        #trend.getTrends('USA', api)
        #trend.getTrends('World', api)

        #tweet.getLocationTweet(api, "HappyBirthdayGurudev")

        #geo.findLocation("","mk",".csv")

        geoC.findGeo("","mk",".csv")