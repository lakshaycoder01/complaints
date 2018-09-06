from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import os
from pickle import load
import re
import keras.backend as K
import tensorflow as tf


Model_dir='./models'
tokenize_fil_dir='./tokenizefiles'
max_len_dir='./max_length_files'
dict_dir='./dict_files'

global model_type,model_product
global graph

def load_type_model():
	try:
	
		model=load_model(os.path.join(Model_dir,'model.h2213'))
		
		graph = tf.get_default_graph()
		return model,graph
	except:
		print("Type complaint model is not loading")
	
	
def create_tokenizer_type():
	tokenizer=load(open(os.path.join(tokenize_fil_dir,'typetokens.pkl'),'rb'))
	return tokenizer
	
def result_from_dict_type(clas):
	if(clas==0):
		claas='FeedBack'
	elif(clas==1):
		claas='Problem'
	else:
		claas='Suggestion'
	return claas
	
def max_len_product():
	arr=[]
	with open(os.path.join(max_len_dir,'file_type.txt')) as f:  
		for line in f:
			arr.append(line)
	return int(arr[1])
	
def encode_docs(tokenizer,max_length,doc):
	encoding=tokenizer.texts_to_sequences(doc)
	padding=pad_sequences(encoding,maxlen=max_length,padding='post')
	return padding

	
def predicting_type(message):
	try:
		print(message)
		max_length=max_len_product()
		print(max_length)
		tokenized=create_tokenizer_type()
		padding=encode_docs(tokenized,max_length,[message])
		model,graph=load_type_model()

		with graph.as_default():
			type_proba=model.predict(padding,verbose=0)     #Modified input to 3 channels
			type_result=type_proba[0]
			type_class=model.predict_classes(padding,verbose=0) #Modified input to 3 channel	
		type_label=result_from_dict_type(type_class)
		print(type_label)
		
		return type_result.tolist(),type_label
	except:
		print("Problem in type of complaint prediction")

	
