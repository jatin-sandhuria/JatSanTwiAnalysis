import geocoder
from geopy.geocoders import Nominatim
from geopy.exc import *

from geopy import geocoders



import time,urllib
from datetime import datetime

class GeoCoder2:
    def findGeo(self,fileName,extension):

        dictInfo = {}
        dictCount = {}
        fileN = 'C:\\Users\\jatin\\Desktop\\Project_Twitter\\' + fileName+extension
        fileA = open(fileN, 'r',encoding='utf-8')

        fileW = open('C:\\Users\\jatin\\Desktop\\Project_Twitter\\'+fileName+"_Geo.txt", 'w', encoding='utf-8')
        fileW.write("Keyword\tCity\tState\tCountry\tLatitude\tLongitude\tTotalTweets"+"\n")

        countRequests = 1
        countLine = 0

        for line in fileA:
            countLine+=1
            if(countLine<1400000000000):
                splitLine = line.split("\t")

                locationName = str(splitLine[0].replace('"',"")).strip().replace("/",",")[:-1]
                if(locationName):

                    try:
                        if locationName not in dictInfo:

                            g = geocoder.google(locationName)
                            city = str(g.city_long).strip().replace("\t",";")
                            state = str(g.state_long).strip().replace("\t",";")
                            country = str(g.country_long).strip().replace("\t",";")
                            latitude = str(g.lat).strip().replace("\t",";")
                            longitude = str(g.lng).strip().replace("\t",";")

                            info = city+"\t"+state+"\t"+country+"\t"+latitude+"\t"+longitude

                            print(str(countRequests)+" | "+locationName+" | "+info)

                            dictInfo[locationName] = info
                            dictCount[locationName] = 1
                            countRequests += 1

                            if (countRequests % 500 == 0):
                                print("Total Lines Processed is " + str(countLine))
                                print("Total CountRequests is " + str(countRequests))
                                print("Sleeping for 7 minutes at "+str(datetime.now()))
                                time.sleep(60 * 7)

                        else:
                            dictCount[locationName] = dictCount.get(locationName)+1


                    except (AttributeError,ValueError,IndexError):
                         print(locationName+"   "+"Error Occurred")
                         continue

                    except GeocoderServiceError:
                        print("waiting")
                        continue
        print(dictInfo)
        print(dictCount)

        for key in dictInfo:
            fileW.write(key.replace("\t", "") + "\t")
            fileW.write((dictInfo.get(key) + "\t"))
            fileW.write(str(dictCount.get(key)))
            fileW.write("\n")

        fileA.close()
        fileW.flush()
        fileW.close()
