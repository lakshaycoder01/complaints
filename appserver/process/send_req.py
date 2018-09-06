import json,requests


def send_request(response,data):
	requestt=requests.post(response,data)
	response_bankk=requestt.json()
	#print(response_bankk)
	return response_bankk
	