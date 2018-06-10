#!/usr/local/bin/python3

import http.client

def extract(classID):
	conn = http.client.HTTPSConnection("classes.berkeley.edu")
	conn.request("GET", "/enrollment/update/2188/" + str(classID))
	request = conn.getresponse()
	return request.read().decode()

if __name__ == "__main__":
	print(extract(27019))