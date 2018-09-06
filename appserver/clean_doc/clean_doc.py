import re
from nltk.corpus import stopwords

def clean_text(message):
	message=re.sub(r'[^A-Za-z0-9]+',' ',message)
	doc= message.split()
	stop_words=stopwords.words('english')
	stop_words.extend(['dont','know','what'])
	lis=[]
	for word in doc:
		if word not in lis:
			lis.append(word)
	tokens=[word for word in lis if word not in stop_words]
	message=' '.join(tokens)
	return message