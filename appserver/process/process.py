import json
import requests
from clean_doc import clean_text
from models_file import prediction_result
from elasLnQ import get_response_from_search
from acc_cre import get_url
from .comprocess import command_process,no_elastic_res

from emailresponse import send_mail

def mainfunction(mail_text,user_mail):

	extkeymessage=mail_text
	cleaned_text=clean_text(mail_text)  #removed unwanted text for prediction
	predicted_data=prediction_result(cleaned_text)  #CNN models call and result
	prediction_res=json.loads(predicted_data)
	print(prediction_res)
	type_problem=prediction_res['type']   #type of complaint
	product_type=prediction_res['product']   #product complaint
	sentiment=prediction_res['senti']
	print("************************")
	
	if(product=="Services"):
		try:
			ser_type_label=data['ser_type_label']		
			search_result=get_response_from_search(product_type,extkeymessage)  #elasticsearch call
			search_result=json.loads(search_result)
			elastic_response=search_result['response']
			check_url=get_url(elastic_response)       #checking elasticresponse for service request
			if(check_url!=None):
				command_type=search_result['command_type']
				sub_type=search_result['sub_type']
				req_ser_response=command_process(elastic_response,commmand_type,user_mail,extkeymessage)
				print("***************")
				print(req_ser_response)	
			else:
				req_ser_response=no_elastic_res(user_mail)
			subject=product if(sub_type is None and product is None) else sub_type+" "+product
					
			response_data=json.dumps({'sentiment':sentiment,'complain_product_class':product,'complain_type_class':type_problem,'complain_ser_type':ser_type_label,'response':req_ser_response})
			email_response=send_mail(user_mail,req_ser_response,subject_mail)
			return response_data
		except:
			print("No response from bank server")
	else:
		try:
			search_result=get_response_from_search(product_type,extkeymessage)
			search_result=json.loads(search_result)
			elastic_response=search_result['response']
			check_url=get_url(elastic_response) #checking elasticresponse for service request
			print(check_url)
			if(check_url!=None):
				command_type=search_result['command_type']
				text=search_result['text']
				print(text)
				req_ser_response=command_process(elastic_response,command_type,user_mail,extkeymessage)
				print("***************")
				print(req_ser_response)
			else:
				req_ser_response=no_elastic_res(user_mail)
			subject_mail=product if(text is None and product is None) else text+" "+product
			print(subject)
			response_data=json.dumps({'sentiment':sentiment,'complain_product_class':product_type,'complain_type_class':type_problem,'response':req_ser_response})
			print(response_data)
			email_response=send_mail(user_mail,last_response,subject_mail)
			return response_data
		except:
			print("No response from bank server")

				
			
				
					
					
					
	
	
	