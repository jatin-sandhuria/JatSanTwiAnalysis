from geopy.geocoders import Nominatim
from geopy.exc import *
import time,urllib
from datetime import datetime

class FIndGeoLocation:
    def findLocation(self,fileName,extension):

        dictInfo = {}
        dictCount = {}
        fileN = 'C:\\Users\\jatin\\Desktop\\Project_Twitter\\' + fileName+extension
        fileA = open(fileN, 'r',encoding='utf-8')

        fileW = open('C:\\Users\\jatin\\Desktop\\Project_Twitter\\'+fileName+"_Geo.txt", 'w', encoding='utf-8')
        countRequests = 1
        countLine = 0

        for line in fileA:
            countLine+=1
            if(countLine<120000000):
                splitLine = line.split("\t")

                locationName = str(splitLine[0].replace('"',"")).strip().replace("/",",")[:-1]
                if(locationName):

                    try:
                        if locationName not in dictInfo:
                            print(str(countRequests)+" | "+locationName +" key not found in dict")
                            geolocator = Nominatim()
                            location = geolocator.geocode(locationName)
                            print(geolocator.country_bias)
                            dictInfo[locationName] = str(location.address).replace("\t","")+"\t"+ str(location.latitude)+"\t" +str(location.longitude)
                            dictCount[locationName] = 1
                            countRequests += 1

                            if (countRequests % 500 == 0):
                                print("Total Lines Processed is " + str(countLine))
                                print("Total CountRequests is " + str(countRequests))
                                print("Sleeping for 7 minutes at "+str(datetime.now()))
                                time.sleep(60 * 7)

                        else:
                            dictCount[locationName] = dictCount.get(locationName)+1


                    except (AttributeError,ValueError):
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