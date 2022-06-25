import json
from time import strftime, gmtime

with open("acdc.json", "r") as f:
    file = json.load(f)
    duration = sum(int(i["duration"]) for i in file["album"]["tracks"]["track"])
    print("Length of whole album equals: ", strftime('%H:%M:%S', gmtime(duration)))
    # print(f'Length of whole album equals: {duration} seconds')  --- >>> BASIC SOLUTION
