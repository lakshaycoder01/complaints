
from textblob import TextBlob
	
def predicting_sentiment(message):
	text=TextBlob(message)
	polarity=text.sentiment.polarity
	if(polarity>0):
		sentiment="Good"
	elif(polarity<0):
		sentiment="Bad"
	else:
		sentiment="Neutral"
	return polarity,sentiment