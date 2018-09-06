from nltk.util import ngrams
from nltk.corpus import stopwords
import nltk
import re
import os
import json,requests


def remove_limiters(text):
	try:
		arr=[]
		print(text)
		for element in text:
			data=re.split("[,-/_#$%@*&~| ]",element)
			joined_no=''.join(data)
			arr.append(joined_no)
		return arr
	except:
		print("Delimiter remove function has some problem")

	

def get_card_no(text):
	try:
		text = re.sub('[.]', ' ', text)
		pattern=r"(^|\s+)([0-9A-Za-z]{4}-?/?\s?[0-9A-Za-z]{4}-?/?\s?[0-9A-Za-z]{4}-?/?\s?\d{4}/?)(?:\s+|$)"
		card_number=re.findall(pattern,text)
		if(card_number):
			arr=[]
			print(card_number)
			for element in card_number:
				arr.append(element[1])
			print(arr)
			return arr
		else:
			arr=[]
			print("None")
			arr.append(None)
		return arr
			
	except:
		print("Card no. hasn't generated")

def get_acc_no(text):
	try:
		pattern=r'(?:[0-9]{11}|[0-9]{10}|[0-9]{9}|[0-9]{8}|[0-9]{12}|[0-9]{13}|[0-9]{14}|[0-9]{15}|[0-9]{16})'
		acc_no=re.findall(pattern,text)
		if(acc_no):
			arr=[]
			for element in acc_no:
				if(len(element)>=8):
					arr.append(element)
			print(arr)
			return arr
		else:
			arr=[]
			print("None")
			arr.append(None)
		print(arr)
		return arr
	except:
		print('Acc no has not generated')
		
def get_car_acc_no(text):
	try:
		text = re.sub('[.]', ' ', text)
		pattern=r"(^|\s+)([0-9A-Za-z]{4}-?/?\s?[0-9A-Za-z]{4}-?/?\s?[0-9A-Za-z]{4}-?/?\s?(?:\d{5}|\d{4}|\d{3}|\d{2})/?)(?:\s+|$)"
		card_number=re.findall(pattern,text)
		if(card_number):
			arr=[]
			print(card_number)
			for element in card_number:
				arr.append(element[1])
			print(arr)
			return arr
			
		else:
			pattern=r'(?:[0-9]{11}|[0-9]{10}|[0-9]{9}|[0-9]{8}|[0-9]{12}|[0-9]{13}|[0-9]{14}|[0-9]{15}|[0-9]{16})'
			acc_no=re.findall(pattern,text)
			if(acc_no):
				arr=[]
				for element in acc_no:
					if(len(element)>=8):
						arr.append(element)
				print(arr)
				return arr
			else:
				arr=[]
				arr.append(None)
				print(arr)
				return arr
				
	except:
		print("Cre_Acc no. hasn't generated")
	
			
		
		
def get_url(msg):
	pattern='http'
	if pattern in msg:
		return msg
	else:
		return None


	
