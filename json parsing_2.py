import json
from pprint import pprint

with open("Digital_Music.json") as data_file:
    data = json.load(data_file)

#Create a dictionary of the first reviews posted on a product

firstReview = {}
for item in data:
    if item["asin"] in firstReview:
        if firstReview[item["asin"]]["unixReviewTime"] > item["unixReviewTime"]:
            firstReview[item["asin"]] = item
    else:
        firstReview[item["asin"]] = item
#pprint(firstReview)

#Create a list of the reviewers from the above dictionary who posted Extreme Ratings

reviewerCount = []
for value in firstReview.values():
    if value["overall"] == 1 or value["overall"] == 5:
        reviewerCount.append(value["reviewerID"]) #print(value["reviewerID"], value["overall"])
#pprint(reviewerCount)

#Count the amount of the above reviews for each reviewer

from collections import Counter
#pprint(Counter(reviewerCount).most_common(15))

#Get the whole set of attributes of the above reviews, for further analysis

helpfulist = []
h = 0
asinlist = []
for value in firstReview.values():
    if value["reviewerID"] == "A1W16J9R4DOBEC" and (value["overall"] == 1 or value["overall"] == 5):
        if value["helpful"][1] > 2: #Evaluate using helpfulnes and median score
            helpfulist.append(value["helpful"][0]/value["helpful"][1])
            h = h + (value["helpful"][0]/value["helpful"][1])
            asinlist.append(value["asin"])
        #pprint(value)
pprint(helpfulist)
h = h/len(helpfulist)
pprint(h)
#pprint(asinlist)

medianlist = []
for item in data:
    if item["asin"] == "B001ESGVUA":
        medianlist.append(item["overall"])
        if item["reviewerID"] == "A1W16J9R4DOBEC":
            print(item["overall"], item["helpful"])
medianlist.sort()
#pprint(medianlist)
print(len(medianlist))
m = int(len(medianlist)/2)
#print("{:1.0f}".format(m))
print(m)
print(medianlist[m])
