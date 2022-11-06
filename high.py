from heapq import nlargest
dict = {
 "Name": ["Sachin", "Sourav", "Rahul"],
 "Runs": [92, 96, 90]
}
highest = nlargest
for i in range(0, len(dict["Runs"])):
 if highest == nlargest or dict["Runs"][i] > dict["Runs"][highest]:
    highest = i
print(dict["Name"][highest], 'scored the highest number')