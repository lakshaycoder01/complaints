from nltk.util import ngrams
from nltk.corpus import stopwords
import nltk
import re
import os
stop_dir='./stopwords'
parsetokens = ['VB','VBP','RB','NN','JJ','NNS','NNP']
use_words = { word.strip() for word in open(os.path.join(stop_dir,'useful.txt')).readlines() if word.strip()}


def get_grams(text):
	try:
		arr=[]
		for i in range(1,4):
			gram=ngrams(text,i)
			arr.append(gram)
		arr1=[]
		for data in arr:
			for line in data:
				combine=' '.join(line)
				arr1.append(combine)
		return arr1
	except:
		print("Ngrams are not generated")
	
	
def get_tagged(words):
	arr=[]
	tagged_sen=nltk.tag.pos_tag(words)
	for word,tag in tagged_sen:
		if tag in parsetokens:
			arr.append(word)
	print(arr)
	return arr
	
					
def relational_bank_keywords(text):
	try:
		tex=text.split()
		stop_words=stopwords.words('english')
		words=[word for word in tex if word not in stop_words]
		#tagged_sen=get_tagged(words)
		grams=get_grams(words)
		for words in grams:
			if words in use_words:
				print(words)
				return words
	except:
		print("There is problem in keywords generation")