import json
from pprint import pprint

with open("Digital_Music.json") as data_file:
    data = json.load(data_file)

#Create a dictionary of low helpfulnes reviews

lowhelp = {}
for item in data:
    if item["helpful"][1] > 3:
        h = (item["helpful"][0]/item["helpful"][1])
        if h < 0.5:
            lowhelp[item["unixReviewTime"]] = item
#pprint(lowhelp.keys())

#Create a list of the reviewers posted the as above defined reviews

revlow = []
for value in lowhelp.values():
    revlow.append(value["reviewerID"])
#pprint(revlow)

#Count the reviews having the most low helpfulnes reviews

from collections import Counter
#pprint(Counter(revlow).most_common(10))

#Get and sort in the timeline the reviews for each of the above reviewers

lowlist = []
for value in lowhelp.values():
    if value["reviewerID"] == "A3HQ4QMJ8JUDUW":
        lowlist.append(value["unixReviewTime"])
lowlist.sort()
pprint(lowlist)
print(len(lowlist))

unixlist = []
for item in data:
    if item["reviewerID"] == "A3HQ4QMJ8JUDUW" and item["helpful"][1] > 3:
        unixlist.append(item["unixReviewTime"])
unixlist.sort()
print(len(unixlist))
pprint(unixlist)