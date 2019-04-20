#loading the pyspark context
import findspark
findspark.init()

import pyspark

sc = pyspark.SparkContext(appName = "Test")

sc.master

#loading the uer-artist ratings dataset
#user_artist_data_small.txt
#3 columns: userid artistid playcount
uadatapath="user_artist_data_small.txt"
rawUserArtistData = sc.textFile(uadatapath)

print"The data set is"
print""

data_set = rawUserArtistData.take(10)
 
# print the data set
for element in data_set:
    print(element)

print""

from pyspark.mllib.recommendation import Rating,ALS

uaData=rawUserArtistData\
    .map(lambda x:x.split(" "))\
    .filter(lambda x: float(x[2])>=20)\
    .map(lambda x:Rating(x[0],x[1],x[2]))

#Persisting it into disk    
uaData.persist()

#Feeding uaData to ALS (Alternating least squares)
model=ALS.trainImplicit(uaData,10,5,0.01)

user = input("Enter a uer id ")
print""

#recommendProducts method to give recommendation for the given user id and the number of recommendations
recommendations=model.recommendProducts(user,5)

print"The recommended artist ID for the user"
print""

result = recommendations
for element in result:
    print(element)

print""

#artist_data.txt
#2 columns: artistid artist_name
artistsPath="artist_data_small.txt"

#load the data and split the rows into list
artistLookup=sc.textFile(artistsPath).map(lambda x:x.split("\t"))

#persist it into disk
artistLookup.persist()

#print the recommended artist names
print "The corresponding artist names are"
print ""
for rating in recommendations: 
    print artistLookup.lookup(str(rating.product))

sc.appName

sc.stop()
