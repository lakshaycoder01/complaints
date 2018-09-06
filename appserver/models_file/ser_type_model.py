from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import os
from pickle import load
import keras.backend as K

import tensorflow as tf
import numpy as np
import re


Model_dir='./models'
tokenize_fil_dir='./tokenizefiles'
max_len_dir='./max_length_files'
dict_dir='./dict_files'

global model_type,model_product
global graph

def load_ser_model():
	try:
		ser_model=load_model(os.path.join(Model_dir,'model.h1211'))
		graph=tf.get_default_graph()
		return ser_model,graph
	except:
		print("Problem in service type model loading")

def create_tokens_servicetype():
	
	tokenizer_ser=load(open(os.path.join(tokenize_fil_dir,'sertokenize.pkl'),'rb'))
	return tokenizer_ser
	
def result_from_dict_service(clas):	
	global dicti2
	dicti2=load(open(os.path.join(dict_dir,'serdic.pkl'),'rb'))
	labelser=list(dicti2.keys())[list(dicti2.values()).index(clas)]
	return labelser
	
def max_len_ser_type():
	arr=[]
	with open(os.path.join(max_len_dir,'sermax.txt')) as f:
		for line in f:
			arr.append(line)
	return int(arr[0])
	
def encode_docs(tokenizer,max_length,doc):
	encoding=tokenizer.texts_to_sequences(doc)
	padding=pad_sequences(encoding,maxlen=max_length,padding='post')
	return padding
	
def predicting_ser_type(message):
	try:
		max_length=max_len_ser_type()
		tokenized=create_tokens_servicetype()
		padding=encode_docs(tokenized,max_length,[message])
		model,graph=load_ser_model()
		with graph.as_default():
			ser_type_prob=model.predict(padding,verbose=0)
			ser_type_prob=ser_type_prob[0]
			ser_class=model.predict_classes(padding,verbose=0)
			
		ser_type_label=result_from_dict_service(ser_class)
		K.clear_session()
		
		return ser_type_prob.tolist(),ser_type_label
	except:
		print("Problem in Service type prediction")
	



