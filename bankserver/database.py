from pymongo import MongoClient
from flask import jsonify
try:
	client = MongoClient()
	print("Connected Successfully")
except:
	print('There is problem in connection')


def get_data():

	db=client['complaint_1']
	db_collection=db['customer']
	return db_collection
	




