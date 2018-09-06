from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import os
from pickle import load
import tensorflow as tf
import numpy as np
import re




Model_dir='./models'
tokenize_fil_dir='./tokenizefiles'
max_len_dir='./max_length_files'
dict_dir='./dict_files'

global model_type,model_product
global graph


def load_product_model():
	try:
		model_product=load_model(os.path.join(Model_dir,'model.h123331'))
		graph = tf.get_default_graph()
		return model_product,graph
	except:
		print("Product model has problem in loading")
	
def create_tokenizer_product():
	tokenizer=load(open(os.path.join(tokenize_fil_dir,'protokenized.pkl'),'rb'))
	return tokenizer
	
def result_from_dict_product(clas):
	global dicti
	dicti=load(open(os.path.join(dict_dir,'consumerdict.pkl'),'rb'))
	labelcom=list(dicti.keys())[list(dicti.values()).index(clas)]
	return labelcom

	
	
def max_len_product():
	arr=[]
	with open(os.path.join(max_len_dir,'file_name.txt')) as f:  
		for line in f:
			arr.append(line)
	return int(arr[1])
	
def encode_docs(tokenizer,max_length,doc):
	encoding=tokenizer.texts_to_sequences(doc)
	padding=pad_sequences(encoding,maxlen=max_length,padding='post')
	return padding

	
def predicting_product(message):
	try:
		max_length=max_len_product()
		tokenized=create_tokenizer_product()
		padding=encode_docs(tokenized,max_length,[message])
		model,graph=load_product_model()

		with graph.as_default():
			product_proba=model.predict(padding,verbose=0)     #Modified input to 3 channels
			product_result=product_proba[0]
			product_class=model.predict_classes(padding,verbose=0) #Modified input to 3 channel
			
		product_label=result_from_dict_product(product_class)
		
		return product_result.tolist(),product_label
	except:
		print("Problem in product prediction")
	
	
	
