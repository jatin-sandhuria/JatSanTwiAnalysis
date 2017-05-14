import tweepy

class Analysis:
    file = None



    def getLocationTweet(self, api, keyword):
        count = 0
        fileWrite = Analysis.file
        for tweet in tweepy.Cursor(api.search, q=keyword, since = "2017-05-12",
                           until = "2017-05-14", include_entities=True,
                                   lang="en").items():
            #print(count)
            # if (count < 1000):
            # jTweet = tweet._json
            # for key, value in jTweet.items():
            #    print(key, value)

            loca = str(tweet.user.location)#.replace(",", ";")
            #time = str(tweet.created_at).replace(",", ";")

            if not loca:
                info = (" " )#+ "," + (time))
            #else:
            #    if not time:
            #        info = ((loca) + "," + " ")
            if loca:# and time:
                info = ((loca))# + "," + (time))
            print(str(count) + "  " + info)
            fileWrite.write(info)
            fileWrite.write("\n")

            # else:
            #   break

            count += 1
        fileWrite.close();


    def createFile(self, fileName):
        Analysis.file = open('C:\\Users\\jatin\\Desktop\\Project_Twitter\\' + fileName, 'a', encoding='utf-8')

