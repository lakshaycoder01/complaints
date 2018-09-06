from elasticsearch import Elasticsearch
import json

from elasticsearch import TransportError
es=Elasticsearch()

es.indices.create(index='complaindaa089',ignore=400)

with open('brain5.json') as datafile:
	data=json.load(datafile)
	for line in data:
		es.index(index='complaindaa089',doc_type="user",body=line)



	
def deleteindex():
	es.indices.delete(index='complaindata089')


	
print('done deploying')
