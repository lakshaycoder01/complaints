from acc_cre import relational_bank_keywords,remove_limiters,get_card_no,get_url,get_acc_no,get_car_acc_no
from .send_req import send_request
import json


def command_process(response,command_type,user_details,message):
	if(command_type=='CA'):	
		card_no=get_card_no(message)       #card_no extraction
		if(card_no[0]!=None):
			delimited_no=remove_limiters(card_no) #remove delimiters from card no
			keyword=relational_bank_keywords(message)
			service_request_data=json.dumps({'user':user_details,'gen_coa_no':delimited_no,'keywords':keyword})
			server_response=send_request(response,service_request_data)       #sending request to bank server
			return server_response
		else:
			response="Please provide card details"
			return response		
	elif(command_type=='ACC'):
		acc_no=get_acc_no(message)   #acc_no extraction
		if(acc_no[0]!=None):
			keyword=relational_bank_keywords(message)
			service_request_data=json.dumps({'user':user_details,'gen_coa_no':acc_no,'keywords':keyword})
			server_response=send_request(response,service_request_data)    #sending request to bank server
			return server_response	
		else:
			response="Please provide account details"
			return response		
	elif(command_type=='Acc_CA'):
		gen_no=get_car_acc_no(message)          #extracting acc_card no 
		if(gen_no[0]!=None):
			delimited_no=remove_limiters(gen_no)
			keyword=relational_bank_keywords(message)
			service_request_data=json.dumps({'user':user_details,'gen_coa_no':delimited_no,'keywords':keyword})
			server_response=send_request(response,service_request_data)                #sending request to bank server
			return server_response
		else:
			response="Please provide details"
			return response
	else:
		response="Please be more clear with your complaint"
		return response
			
	
def no_elastic_res(user_details):
	url='http://localhost:8787/no_response'
	service_request_data=json.dumps({'user':user_details})
	server_response=send_request(url,service_request_data)
	return server_response
	
	

			
		
			
			
		
		


		
			
			
			
	