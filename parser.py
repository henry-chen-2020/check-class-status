#!/usr/local/bin/python3

import json

def parse(string):
	data = json.loads(string)
	relevant = data["available"]["enrollmentStatus"]
	return relevant