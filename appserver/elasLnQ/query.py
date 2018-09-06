from elasticsearch import Elasticsearch
import os
from nltk.corpus import stopwords
import nltk
import json
client=Elasticsearch()
stop_dir='./stopwords'
stop_words = { word.strip() for word in open(os.path.join(stop_dir,'stop_ser.txt')).readlines() if word.strip()}


def clean_data(message):
	tag_list=['VB','VBP','RB','NN','JJ','UH','NNS','NNP','WRB','CD','VBG','VBN','VBD','VBZ']
	line=message.split()
	print('split done')
	stop=stopwords.words('english')
	words=[word for word in line if word not in stop] 
	words=[word for word in words if word not in stop_words]
	print('lak')
	#arr=[]
	#tagged_sentence=nltk.tag.pos_tag(words)
	#for word,tag in tagged_sentence:
	#	if tag in tag_list:
	#		arr.append(word)
	#print(arr)
	message=' '.join(words)
	print(message)
	return message
			
	
	
def get_response_from_search(label,message):
	try:
		print('got message and label')
		message=clean_data(message)
		print(message)
		product_label=label
		
		response = client.search(
			index ="complaindaa089",
			doc_type ="user",
			body={
				"query":{
					"bool":{
						"must":{
							"match":{
								"text":message
							}
						},
						"filter":{
							"match":{
								"Product":product_label
							}
						}
					}
				}
			}	
		)
		print(response)
		
		if not response['hits']['hits']:
			response="Our server is not responding currently.Please try after sometime"
			data=json.dumps({'response':response})
			return data
			
		else:
			response_filtered=response['hits']['hits'][0]
			print(response_filtered)
			last_response=response_filtered['_source']['action']
			text=response_filtered['_source']['text']
			command_type=response_filtered['_source']['command_type']
			product=response_filtered['_source']['Product']
			print(command_type,text,last_response)
			if(product=='Services'):
				sub_type=response_filtered['_source']['sub_type']
				data=json.dumps({'response':last_response,'command_type':command_type,'sub_type':sub_type})
				return data
				
			else:
				data=json.dumps({'response':last_response,'command_type':command_type,'text':text})
				return data

				
	except:
		print("No message to query elasticsearch engine")