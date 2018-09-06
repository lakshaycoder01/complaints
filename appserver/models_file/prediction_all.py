from .sen_model import predicting_sentiment
from .type_model import predicting_type
from .pro_model import predicting_product
from .ser_type_model import predicting_ser_type
import keras.backend as K
import json



def prediction_result(text):
	print("lakshay")
	polarity,sentiment=predicting_sentiment(text)
	print("############Sentiment Prediction ##########")
	print(sentiment)
	print("lak")
	type_result,type_label=predicting_type(text)
	print("donee")
	print("###### type prediction #######")
	print(type_label,type_result)
	K.clear_session()
	product_result,product_label=predicting_product(text)
	print("###### product prediction #########")
	print(product_label,product_result)
	if(product_label=='Services'):
		K.clear_session()
		ser_type_prob,ser_type_label=predicting_ser_type(text)
		print("###### service type #######")
		print(ser_type_label,ser_type_prob)
		K.clear_session()
		data=json.dumps({"senti":sentiment,"type":type_label,"product":product_label,"ser_type":ser_type_label})
		return data
	else:
		ser_type_label=None
		data=json.dumps({"senti":sentiment,"type":type_label,"product":product_label,"ser_type":ser_type_label})	
		return data
	
