#!/usr/local/bin/python3

import extractor
import parser
import selfsend
import json

output = input("Class ID: ")
address = input("Email: ")
string = extractor.extract(output)
data = parser.parse(string)
pretty = json.dumps(data, indent = 4)
#print(pretty)

res = "nope"

if data["waitlistedCount"] < data["maxWaitlist"]:
    spots = data["maxWaitlist"] - data["waitlistedCount"]
    res = "There are {} spots on the waitlist.".format(spots)
else:
    res = "Class full at {}".format(data["maxWaitlist"])
	
selfsend.sendemail(address, "Update on classID " + str(output), res, "is.testingscripts@gmail.com", "Lower05!")
