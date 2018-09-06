from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
import database
from gevent.pywsgi import WSGIServer
from werkzeug.serving import run_with_reloader
from werkzeug.debug import DebuggedApplication
from geventwebsocket.handler import WebSocketHandler
import logging

app=Flask(__name__)
CORS(app)

@app.route('/no_response',methods=['GET','POST'])
def no_response():
	print("kakakkaa")
	data=request.get_json(force=True)
	user_details=data['user']
	print(user_details)
	db=database.get_data()
	database_data=db.find({'email':user_details})
	for line in database_data:
		name=line['name']
	return jsonify("Hey "+name+"\r\n\r\nWe registered your complaint. We're transferring it to concerned department.They'll get back to you in 2 working days.\r\n\r\nThanks for raising this issue with us.\r\n\r\nWe are here to help you in any way possible.\r\n\r\nRegards\r\n\r\nIntellect Design")

@app.route('/credit_reporting/balance_in',methods=['GET','POST'])
def report_incorr_bal():
	data=request.get_json(force=True)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']

	db=database.get_data()
	database_data=db.find({'email':user_details})
	for line in database_data:
		name=line['name']
		acc=line['']
	return jsonify("Hey "+name+",\r\n\r\nWe'll correct the balance in your account and generate a new credit report based on correct balance.\r\n\r\nSorry for the inconvience caused due to this.Your inputs are important to us.Rest Assured.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")


@app.route('/services/credit_report',methods=['GET','POST'])
def ser_problem():
	data=request.get_json(force=True)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']

	db=database.get_data()
	database_data=db.find({'email':user_details})
	for line in database_data:
		name=line['name']
	return jsonify("Hey "+name+",\r\n\r\nThese inquiries will not affect your credit report in any way. If any way these inquiries affect your credit report.We'll correct it.\r\n\r\nWe are deeply regretted for any inconvience caused to you due to inquiries.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to help you in any way possible and we are assuring you this will not affect your credit report.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")


@app.route('/services/incorr/invalid',methods=['GET','POST'])
def ser_incorr():
	data=request.get_json(force=True)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']

	db=database.get_data()
	database_data=db.find({'email':user_details})
	for line in database_data:
		name=line['name']
	return jsonify("Hey "+name+",\r\n\r\nWe're currently working on your complaint regarding incorrect information. If we find something wrong with your information,We'll correct it and generate a new credit report for you.\r\n\r\nSorry for any inconvience you have faced due to this.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to help you in any way possible.\r\n\r\nWarm Regards\r\nIntellect Design Team")


@app.route('/services/deduc/freeze',methods=['GET','POST'])
def deduc_freeze():

	data=request.get_json(force=True)
	print(data)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords=='card'):
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details},{keywords:{'$elemMatch':{'details.card_no':accocar_details[0]}}})
			for line in database_data:
				type_1=line['card'][0]['type']
				sub_type=line['card'][0]['sub_type']
				name=line['card'][0]['details'][0]['name']
				card_no=line['card'][0]['details'][0]['card_no']
				print(card_no)
			if(accocar_details[0]!=card_no):
				return jsonify("Hey "+name+". Please give correct card no.")
			else:
				return jsonify("Hey " + name+ ",\r\n\r\nWe're currently freezing your "+sub_type+" "+type_1+" no: "+card_no+" to prevent any fradulent transactions.We'll start investigating what went wrong with your "+type_1+" account.\r\n\r\nThanks for raising this issue with us in time.Otherwise some fraud activity may have occured.Your inputs are important to us.Rest Assured.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team ")
		else:
			print("Please provide your card details")

	else:
		if(keywords=='Mortgage'):
			keywords='home loan'
		elif(keywords=='savings account' or keywords=='current account' or keywords=='account' or keywords=='deposit account'):
			keywords='checking account'
		else:
			keywords=keywords
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details})
			for line in database_data:
				acc=line[keywords]
				name=line['name']
			if(accocar_details[0]!=acc):
				return jsonify("Hey "+name+". Please give your correct account details.")
			else:
				return jsonify("Hey "+name+ ",\r\n\r\nWe're currently freezing your "+keywords+" account no: "+acc+" to prevent any fradulent transactions.We'll start investigating what went wrong with your "+keywords+" account.\r\n\r\nThanks for raising this issue with us in time.Otherwise some fraud activity may have occured.Your inputs are important to us.Rest Assured.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
		else:
			return jsonify("Please provide your account details")



@app.route('/services/deduc/acc',methods=['GET','POST'])
def deduc_acc():
	data=request.get_json(force=True)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords=='card'):
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details},{keywords:{'$elemMatch':{'details.card_no':accocar_details[0]}}})
			for line in database_data:
				type_1=line['card'][0]['type']
				sub_type=line['card'][0]['sub_type']
				name=line['card'][0]['details'][0]['name']
				card_no=line['card'][0]['details'][0]['card_no']
			if(accocar_details[0]!=card_no):
				return jsonify("Hey "+name+". Please give correct card details")
			else:
				return jsonify("Hey " + name+ ",\r\n\r\nSorry for the money you have been charged. We're already raised the request to concerned department. If your claim is genuine. You'll get the money back into your "+type_1+" account no: "+card_no+".\r\n\r\nWe are deeply regretting inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nThanks for raising this issue with us.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

		else:
			reply="Give your Card Details"
			return jsonify(reply)

	else:
		if(keywords=='Mortgage'):
			keywords='home loan'
		elif(keywords=='savings account' or keywords=='current account' or keywords=='account' or keywords=='deposit account'):
			keywords='checking account'
		else:
			keywords=keywords
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details})
			for line in database_data:
				acc=line[keywords]
				name=line['name']
			if(accocar_details[0]!=acc):
				return jsonify("Hey "+name+". Please give your correct account details.")
			else:
				return jsonify("Hey "+name+ ",\r\n\r\nSorry for the money you have been charged. We're already raised the request to concerned department. If your claim is genuine. You'll get money back into your "+keywords+" account no: "+acc+".\r\n\r\nWe are deeply regretting any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nThanks for register this issue with us.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
		else:
			return jsonify("Please provide your account details")


@app.route('/services/stop',methods=['GET','POST'])
def service_delin_stop():
	data=request.get_json(force=True)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords=='card'):
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details},{keywords:{'$elemMatch':{'details.card_no':accocar_details[0]}}})
			for line in database_data:
				type_1=line['card'][0]['type']
				sub_type=line['card'][0]['sub_type']
				name=line['card'][0]['details'][0]['name']
				card_no=line['card'][0]['details'][0]['card_no']
				print(card_no)
			if(accocar_details[0]!=card_no):
				return jsonify("Hey "+name+". Please give your correct card details")
			else:
				return jsonify("Hey " + name+ ",\r\n\r\nIf you claim is genuine with valid reasons. We'll help to get money credit back into your "+type_1+" account no: "+card_no+".\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.Thanks for registering the issue with us.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

		else:
			reply="Give your Card Details"
			return jsonify(reply)

	else:
		if(keywords=='Mortgage'):
			keywords='home loan'
		elif(keywords=='savings account' or keywords=='current account' or keywords=='account' or keywords=='deposit account'):
			keywords='checking account'
		else:
			keywords=keywords
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details})
			for line in database_data:
				acc=line[keywords]
				name=line['name']
			if(accocar_details[0]!=acc):
				return jsonify("Hey "+name+". Please give your correct account details.")
			else:
				return jsonify("Hey "+name+ ",\r\n\r\nThanks for reaching out to this. We're already raised the request to concerned department. If your claim is genuine. You'll get the money back into your "+keywords+" no: "+acc+".\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.Thanks for registering the issue with us.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
		else:
			return jsonify("Please provide your account details")


@app.route('/services/late',methods=['GET','POST'])
def service_late():
	data=request.get_json(force=True)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords=='card'):
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details},{keywords:{'$elemMatch':{'details.card_no':accocar_details[0]}}})
			for line in database_data:
				type=line['card'][0]['type']
				sub_type=line['card'][0]['sub_type']
				name=line['card'][0]['details'][0]['name']
				card_no=line['card'][0]['details'][0]['card_no']
				print(card_no)
			if(accocar_details[0]!=card_no):
				return jsonify("Hey "+name+". Please provide correct card details.")
			else:
				return jsonify("Hey " + name+ ",\r\n\r\nThanks for reaching out to this. We're already raised the request to concerned department. If your claim is genuine. You'll get the money back into your "+type_1+" account no: "+card_no+".\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

		else:
			reply="Give your Card Details"
			return jsonify(reply)
	else:
		if(keywords=='Mortgage'):
			keywords='home loan'
		elif(keywords=='savings account' or keywords=='current account' or keywords=='account' or keywords=='deposit account'):
			keywords='checking account'
		else:
			keywords=keywords
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details})
			for line in database_data:
				acc=line[keywords]
				name=line['name']
			if(accocar_details[0]!=acc):
				return jsonify("Hey "+name+". Please give your correct account details.")
			else:
				return jsonify("Hey "+name+ ",\r\n\r\nThanks for reaching out to this. We're already raised the request to concerned department. If your claim is genuine. You'll get the money back into your "+keywords+" no: "+acc+".\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
		else:
			return jsonify("Please provide your account details")


@app.route('/services/promotion/promo',methods=['GET','POST'])
def promo():
	data=request.get_json(force=True)
	print(data)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords=='card'):
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details},{keywords:{'$elemMatch':{'details.card_no':accocar_details[0]}}})
			for line in database_data:
				print(line)
				type_1=line['card'][0]['type']
				sub_type=line['card'][0]['sub_type']
				name=line['card'][0]['details'][0]['name']
				card_no=line['card'][0]['details'][0]['card_no']
				print(card_no)
			if(accocar_details[0]!=card_no):
				return jsonify("Hey "+name+". Please give correct card details")
			else:
				return jsonify("Hey " + name+ ",\r\n\r\nThanks for reaching out to this. We're already raised the request to concerned department. If your claim is genuine. You'll get the promotional credit into your "+type_1+" no: "+card_no+".\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nYou can also check our new"+type_1+" promotional offer.\r\n\r\nYou are a valuable customer to us.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

		else:
			reply="Give your Card Details"
			return jsonify(reply)
	else:
		if(keywords=='mortgage'):
			keywords='home loan'
		elif(keywords=='savings account' or keywords=='current account' or keywords=='account' or keywords=='deposit account'):
			keywords='checking account'
		else:
			keywords=keywords

		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details})
			for line in database_data:
				print(line)
				acc=line[keywords]
				name=line['name']
			if(accocar_details[0]!=acc):
				return jsonify("Hey "+name+". Please give correct account details.")
			else:
				return jsonify("Hey "+name+ ",\r\n\r\nThanks for reaching out to this. We're already raised the request to concerned department. If your claim is genuine. You'll get the promotional credit into your "+keywords+" no: "+acc+".\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nYou can also check our new promotional"+keywords+"offer at our website.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
		else:
			return jsonify("Please provide your account details")


@app.route('/debt/debt_charge',methods=['GET','POST'])
def debt_charge():
	data=request.get_json(force=True)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords=='card'):
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details},{keywords:{'$elemMatch':{'details.card_no':accocar_details[0]}}})
			for line in database_data:
				print(line)
				type_1=line['card'][0]['type']
				sub_type=line['card'][0]['sub_type']
				name=line['card'][0]['details'][0]['name']
				card_no=line['card'][0]['details'][0]['card_no']
				print(card_no)
			if(accocar_details[0]!=card_no):
				return jsonify("Hey "+name+". Please give correct card details.")
			else:
				return jsonify("Hey " + name+ ",\r\n\r\nSorry for the extra charges you have faced on your "+sub_type+" "+type_1+" account. We'll investigate it and credit back the money into your account if your claim is genuine.\r\n\r\nWe are regretting any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team ")

		else:
			reply="Give your Card Details"
			return jsonify(reply)
	else:
		if(keywords=='mortgage'):
			keywords='home loan'
		elif(keywords=='savings account'):
			keywords='checking account'
		else:
			keywords=keywords
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details})
			for line in database_data:
				print(line)
				acc=line[keywords]
				name=line['name']
			if(accocar_details[0]!=acc):
				return jsonify("Hey "+name+". Please give correct account details.")
			else:
				return jsonify("Hey "+name+ ",\r\n\r\nSorry for extra charges you have faced on your "+keywords+ " account no: "+acc+". We'll investigate it and credit back the money into your account if your claim is genuine.\r\n\r\nWe're regretting any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
		else:
			return jsonify("Please provide your account details")


@app.route('/debt/owed',methods=['GET','POST'])
def owed():
	data=request.get_json(force=True)
	accocar_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords=='card'):
		if(accocar_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details},{keywords:{'$elemMatch':{'details.card_no':accocar_details[0]}}})
			for line in database_data:
				print(line)
				type_1=line['card'][0]['type']
				sub_type=line['card'][0]['sub_type']
				name=line['card'][0]['details'][0]['name']
				card_no=line['card'][0]['details'][0]['card_no']
				print(card_no)
			if(accocar_details[0]!=card_no):
				return jsonify("Hey "+name+". Please provide us with your correct card details")
			else:
				return jsonify("Hey " + name+ ",\r\n\r\nWe're currently investigating your "+sub_type+" "+type_1+" account no: "+card_no+". If your claim is genuine.We'll remove debt status from your "+sub_type+" "+type_1+" account.\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

		else:
			reply="Give your Card Details"
			return jsonify(reply)
	else:
		if(keywords=='mortgage'):
			keywords='home loan'
		elif(keywords=='savings account'):
			keywords='checking account'
		else:
			keywords=keywords
		if(accor_details[0]!=None):
			db=database.get_data()
			database_data=db.find({'email':user_details})
			for line in database_data:
				print(line)
				acc=line[keywords]
				name=line['name']
			if(accocar_details[0]!=acc):
				return jsonify("Hey "+name+". Please give your correct account details.")
			else:
				return jsonify("Hey "+name+ ",\r\n\r\nWe're investigating your "+keywords+ " account no: "+acc+".If your claim is genuine.We'll remove debt from your "+keywords+  " account.\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
		else:
			return jsonify("Please provide your account details")

@app.route('/home/modify',methods=['GET','POST'])
def modify():
	data=request.get_json(force=True)
	acc_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='home loan'
	else:
		keywords=keywords
	if(acc_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)
			acc=line['home loan']
			name=line['name']
		if(acc_details[0]!=acc):
			return jsonify("Hey "+name+". Please provide your correct account details.")
		else:
			return jsonify("Hey "+name+ ",\r\n\r\nWe notified your request for modification of your "+keywords+"no: "+acc+".We've forwarded your request to concerned department and they'll get back to you in 2 days time.\r\n\r\nYou can also check our website for new home loan offers at lower interest rates.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
	else:
		return jsonify("Please share your loan account details")

@app.route('/home/delinquency',methods=['GET','POST'])
def delinquency():
	data=request.get_json(force=True)
	acc_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='home loan'
	else:
		keywords=keywords
	if(acc_details[0] !=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			acc=line['home loan']
			name=line['name']
		if(acc_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details.")
		else:
			return jsonify("Hey "+name+ ",\r\n\r\nGive us sometime to figure out why your "+keywords+" account no: "+acc+ " is marked delinquent and if your claim is genuine. We'll remove delinquency status from your "+keywords+" account.\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
	else:
		return jsonify("Please provide your home loan account details")

@app.route('/home/assis_home',methods=['GET','POST'])
def assis_home():
	data=request.get_json(force=True)
	acc_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='home loan'
	else:
		keywords=keywords
	if(acc_details[0] !=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			acc=line['home loan']
			name=line['name']
		if(acc_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details." )
		else:
			return jsonify("Hey "+name+ ",\r\n\r\nWe're here to provide you with any kind of assistance you need with your  "+keywords+" account no:"+acc+"\r\n\r\nYou can visit our website to check new home loan offers at lower interest rates.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
	else:
		return jsonify("Please provide your home loan account details")


@app.route('/home/refinance',methods=['GET','POST'])
def refinance():
	data=request.get_json(force=True)
	print(data)
	acc_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='home loan'
	else:
		keywords=keywords
	if(acc_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)
			acc=line['home loan']
			print(acc)
		if(acc_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details.")
		else:
			return jsonify("Hey "+name+ ",\r\n\r\nWe're currently processing your request for refinancing of your "+keywords+" account no. "+ acc +". Give us sometime to process how we can help you to refinance your "+keywords+".\r\n\r\nYou can aslo check our website for new home loan offers at lower interest rates.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
	else:
		return jsonify("Please provide your home loan account details")

@app.route('/home/interest',methods=['GET','POST'])
def home_interest():
	data=request.get_json(force=True)
	print(data)
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='home loan'
	else:
		keywords=keywords

	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)
			acc=line['home loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details.")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nWe'll investigate your complaint and if your claim is genuine. We'll reduce the loan amount from your " +keywords+ " account: " +account_details[0]+".\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
	else:
		return jsonify("Please provide your loan account details")

@app.route('/Consumer_loan/forgive',methods=['GET','POST'])
def loan_forgive():
	data=request.get_json(force=True)
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='loan'
	else:
		keywords=keywords
	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)
			acc=line['loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details.")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nWe can understand your current financial condition. Concerned team is working on your request for  "+keywords+" account:"+account_details[0]+ " forgiveness.\r\n\r\nYou can also check our website for new Consumer loan offers at lower interest rates.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team"  )

	else:
		return jsonify("Please provide account details ")

@app.route('/Consumer_loan/defer',methods=['GET','POST'])
def loan_deffer():
	data=request.get_json(force=True)
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='loan'
	else:
		keywords=keywords

	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)
			acc=line['loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give your correct account details ")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nWe checked the status of your "+keywords+" account:"+account_details[0]+". It is deferred. We'll credit back the money you have been charged.\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nYou can also check our new customer loan offers at lower interest rates at our website. \r\n\r\nWarm Regards\r\n\r\nIntellect Design Team" )

	else:
		return jsonify("Please provide account details ")

@app.route('/Consumer_Loan/repay',methods=['GET','POST'])
def repay():
	data=request.get_json(force=True)
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='loan'
	else:
		keywords=keywords

	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)
			acc=line['loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details.")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nWe can understand your current financial status. We'll let you know in 2 days what we can do to help you with your "+keywords + " account : " + account_details[0]+ " repayment request.\r\n\r\nYou can also visit our website for new customer loan offers at lower interest rates.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team" )

	else:
		return jsonify("Please provide account details ")

@app.route('/Consumer_loan/interest',methods=['GET','POST'])
def interest():
	data=request.get_json(force=True)
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='loan'
	else:
		keywords=keywords
	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)

			acc=line['loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details.")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nWe'll investigate your complaint and if your claim is genuine. We'll reduce the loan amount from your " +keywords+ " account: " +account_details[0]+" .\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nYou can visit our websites to check new offers on consumer loan at lower interest rates.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		return jsonify("Please provide account details ")


@app.route('/Consumer_loan/assis1',methods=['GET','POST'])
def assis():
	data=request.get_json(force=True)
	print(data)
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='loan'
	else:
		keywords=keywords
	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)

			acc=line['loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details.")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nWe'll provide you with any assistance you need with your " +keywords+ " account:" +account_details[0]+".\r\n\r\nYou can visit our website to check the latest customer loan offers at lower interest rates.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		return jsonify("Please provide account details ")



@app.route('/Consumer_loan/inquiry',methods=['GET','POST'])
def inquiry():
	data=request.get_json(force=True)
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='loan'
	else:
		keywords=keywords
	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)

			acc=line['loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details." )
		else:
			return jsonify("Hey " + name + ",\r\n\r\nWe'll remove any hard inquiries on your " +keywords+ " account:" +account_details[0]+ " that will not affect your credit report in future.\r\n\r\nSorry for the inconvience caused to you deu to inquiries.Your inputs are important to us.Rest Assured.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nYou can visit our website to check the latest customer loan offer at lower interest rates.\r\n\r\nWarm Regards\r\n\r\nIbtellect Design Team")

	else:
		return jsonify("Please provide account details ")

@app.route('/Consumer_loan/rehab',methods=['GET','POST'])
def rehab():
	data=request.get_json(force=True)
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='loan'
	else:
		keywords=keywords
	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)

			acc=line['loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details.")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nYour request for loan rehabilitation of your " +keywords+ " account:" +account_details[0]+"is under process. We'll get back to you in 2 days time to tell you whether you are eligible for loan rehabilitation.\r\n\r\nYou can visit our website to check the latest customer loan offers at lower interest rates.\r\n\r\nWe are always here to help you.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		return jsonify("Please provide account details ")

@app.route('/Consumer_loan/balance',methods=['GET','POST'])
def loan_balance_corr():
	data=request.get_json(force=True)
	db=database.get_data()
	account_details=data['gen_coa_no']
	user_details=data['user']
	keywords=data['keywords']
	if(keywords is None):
		keywords='loan'
	else:
		keywords=keywords
	if(account_details[0]!=None):
		db=database.get_data()
		database_data=db.find({'email':user_details})
		for line in database_data:
			print(line)

			acc=line['loan']
			name=line['name']
		if(account_details[0]!=acc):
			return jsonify("Hey "+name+". Please give correct account details")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nWe'll investigate your complaint. If your claim is genuine. We'll correct the balance of your "+keywords+ " account:"+account_details[0]+".\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		return jsonify("Please provide account details ")



@app.route('/Cards/lost',methods=['GET','POST'])
def lost():
	data=request.get_json(force=True)
	card_details=data['gen_coa_no']
	print(card_details)
	user_details=data['user']
	print(user_details)
	keyword=data['keywords']
	if(keyword is None):
		keyword='card'
	else:
		keyword=keyword
	if(card_details[0]!=None):
		if(len(card_details)>1):
			type_1=[]
			sub_type=[]
			name=[]
			card_noo=[]
			for element in card_details:
				print(element)
				db=database.get_data()
				data=db.find({'email':user_details},{keyword:{'$elemMatch':{'details.card_no':element}}})
				for line in data:
					type_1.append(line['card'][0]['type'])
					sub_type.append(line['card'][0]['sub_type'])
					name.append(line['card'][0]['details'][0]['name'])
					card_noo.append(line['card'][0]['details'][0]['card_no'])
			print(card_noo)
			print("Hey "+name[0]+ ",\r\n\r\nWe blocked your " + sub_type[0]+" " +type_1[0]+ " no: "+ card_noo[0] +" and "+sub_type[1]+" "+type_1[1]+" no: "+card_noo[1]+  " to prevent any fraudelent transactions. We'll issue you a new "+ keyword+ "s in 2 days.\r\n\r\nThanks for quickly raising the issue with us.Otherwise some fraud transactions may have happened.\r\n\r\nYou can subscribe to our new loss cards insurance plan for future incident.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
			return jsonify("Hey "+name[0]+ ",\r\n\r\nWe blocked your " + sub_type[0]+" " +type_1[0]+ " no: "+ card_noo[0] +" and "+sub_type[1]+" "+type_1[1]+" no: "+card_noo[1]+  " to prevent any fraudelent transactions. We'll issue you a new "+ keyword+ "s in 2 days.\r\n\r\nThanks for quickly raising the issue with us.Otherwise some fraud transactions may have happened.\r\n\r\nYou can subscribe to our new loss cards insurance plan for future incident.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team" )
		else:
			db=database.get_data()
			data=db.find({'email':user_details},{keyword:{'$elemMatch':{'details.card_no':card_details[0]}}})
			print(data)
			for line in data:
				print(line)
				type_1=line['card'][0]['type']
				sub_type=line['card'][0]['sub_type']
				name=line['card'][0]['details'][0]['name']
				card_no=line['card'][0]['details'][0]['card_no']
			if(card_details[0]!=card_no):
				return jsonify("Hey " +name+ ". Please give the correct card no.")
			else:
				print("Hey " + name+",\r\n\r\nWe blocked your " + sub_type+" " +type_1+ " no: "+ card_no + " to prevent any fraudelent transactions. We'll issue you a new "+ type_1+ " in 2 days")
				return jsonify("Dear " + name+ "\r\n\r\nWe blocked your " + sub_type+" " +type_1+ " no: "+ card_no + " to prevent any fraudelent transactions. We'll issue you a new "+ type_1+ " in 2 days.\r\n\r\nThanks for quickly raising the issue with us.Otherwise some fraud transactions may have happened.\r\n\r\nYou can subscribe to our new loss card insurance plan for future incident.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")
	else:
		reply="please give your card details"
		return jsonify(reply)

@app.route('/Cards/offer_cred',methods=['GET','POST'])
def offer_credt():
	data=request.get_json(force=True)
	card_details=data['gen_coa_no']
	user_details=data['user']
	keyword=data['keywords']
	if(keyword is None):
		keyword='card'
	else:
		keyword=keyword
	if(card_details[0]!=None):
		db=database.get_data()
		data=db.find({'email':user_details},{keyword:{'$elemMatch':{'details.card_no':card_details[0]}}})
		for line in data:
			print(line)
			type_1=line['card'][0]['type']
			sub_type=line['card'][0]['sub_type']
			name=line['card'][0]['details'][0]['name']
			card_no=line['card'][0]['details'][0]['card_no']
			print(card_no)
		if(card_details[0]!=card_no):
			return jsonify("Hey " +name+",\r\n\r\nPlease give correct details of your card no.")
		else:
			return jsonify("Hey " + name+ ",\r\n\r\nThanks for reaching out to this. We're already raised the request to concerned department. If your claim is genuine. You'll get the promotional credit into your "+type_1+" no: "+card_no+".\r\n\r\nSorry for any inconvience caused to you due to this.Your inputs are important to us.Rest Assured.\r\n\r\nYou can also check the new promotional "+type_1+"offer at our website.\r\n\r\nWe are always here to help you in any way possible.\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		reply="Give your Card Details"
		return jsonify(reply)
@app.route('/Cards/charge',methods=['GET','POST'])
def charge():
	data=request.get_json(force=True)
	card_details=data['gen_coa_no']
	user_details=data['user']
	print(user_details)
	keyword=data['keywords']
	if(keyword is None):
		keyword='card'
	else:
		keyword=keyword
	if(card_details[0]!=None):
		db=database.get_data()
		data=db.find({'email':user_details},{keyword:{'$elemMatch':{'details.card_no':card_details[0]}}})
		for line in data:
			print(line)
			type_1=line['card'][0]['type']
			sub_type=line['card'][0]['sub_type']
			name=line['card'][0]['details'][0]['name']
			card_no=line['card'][0]['details'][0]['card_no']
		if(card_details[0]!=card_no):
			return jsonify("Hey "+name+ ". Please give correct card no.")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nGive us sometime to investigate why your " + sub_type+" " +type_1+ " no:"+ card_no + " has been charged. If your claim is genuine. We'll credit back the amount in your "+type_1+ " account.\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nYou can also visit our websites for new offers on your "+type_1+".\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		reply="Give your Card Details"
		return jsonify(reply)

@app.route('/Cards/statement',methods=['GET','POST'])
def statement():
	data=request.get_json(force=True)
	card_details=data['gen_coa_no']
	user_details=data['user']
	print(user_details)
	keyword=data['keywords']
	if(keyword is None):
		keyword='card'
	else:
		keyword=keyword
	if(card_details[0]!=None):
		db=database.get_data()
		data=db.find({'email':user_details},{keyword:{'$elemMatch':{'details.card_no':card_details[0]}}})
		for line in data:
			print(line)
			type_1=line['card'][0]['type']
			sub_type=line['card'][0]['sub_type']
			name=line['card'][0]['details'][0]['name']
			card_no=line['card'][0]['details'][0]['card_no']
			print(card_no)
		if(card_details[0]!=card_no):
			return jsonify("Hey "+name+". Please provide correct card no.")
		else:
			return jsonify("Hey " + name + ",\r\n\r\nGive us sometime to update statements of your " + sub_type+" " +type_1+ " no:"+ card_no + ". After sometime when you'll login to your account you'll get updated statements.\r\n\r\nSorry for the inconvience caused to you due to this.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to help you in any way possible.\r\n\r\nYou can also visit our website to check any new offers on your "+type_1+".\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		reply="Give your Card Details"
		return jsonify(reply)


@app.route('/Cards/dupli',methods=['GET','POST'])
def dupli():
	data=request.get_json(force=True)
	card_details=data['gen_coa_no']
	user_details=data['user']
	print(user_details)
	keyword=data['keywords']
	if(keyword is None):
		keyword='card'
	else:
		keyword=keyword
	if(card_details[0]!=None):
		db=database.get_data()
		data=db.find({'email':user_details},{keyword:{'$elemMatch':{'details.card_no':card_details[0]}}})
		for line in data:
			print(line)
			type_1=line['card'][0]['type']
			sub_type=line['card'][0]['sub_type']
			name=line['card'][0]['details'][0]['name']
			card_no=line['card'][0]['details'][0]['card_no']
			print(card_no)
		if(card_details[0]!=card_no):
			return jsoniify("Hey "+name+ ". Please provide correct card details")
		else:
			return jsonify("Hii " + name+ ",\r\n\r\nThere is duplicate statement with your " + sub_type+" " +type_1+ " no:"+ card_no + " We'll correct it and generate new statements for your "+keywords+".\r\n\r\nSorry for inconvience caused to you due to this issue.Your inputs are important to us.Rest Assured.\r\n\r\nWe are always here to help you in any way possible way.\r\n\r\nYou can also check our website for new offers on your "+type_1+".\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		reply="Give your Card Details"
		return jsonify(reply)


@app.route('/Cards/late',methods=['GET','POST'])
def late():
	data=request.get_json(force=True)
	card_details=data['gen_coa_no']
	user_details=data['user']
	keyword=data['keywords']
	if(keyword is None):
		keyword='card'
	else:
		keyword=keyword
	if(card_details[0]!=None):
		db=database.get_data()
		data=db.find({'email':user_details},{keyword:{'$elemMatch':{'details.card_no':card_details[0]}}})
		for line in data:
			print(line)
			type_1=line['card'][0]['type']
			sub_type=line['card'][0]['sub_type']
			name=line['card'][0]['details'][0]['name']
			card_no=line['card'][0]['details'][0]['card_no']
			print(card_no)
		if(card_details[0]!=card_no):
			return jsonify("Hey "+name+",\r\n\r\nPlease provide correct card details")
		else:
			return jsonify("Hii " + name+ "\r\n\r\nWe'll investigate why your " + sub_type+" " +type_1+ " no:"+ card_no + " has been charged for late fee. If your claim is genuine. We'll credit back the amount into your "+type_1+ " account.\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nYou can also visit our website to check new offers on your "+type_1+".\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		reply="Give your Card Details"
		return jsonify(reply)



@app.route('/Cards/lost_bal',methods=['GET','POST'])
def lost_bal():
	data=request.get_json(force=True)
	card_details=data['gen_coa_no']
	user_details=data['user']
	print(user_details)
	keyword=data['keywords']
	if(keyword is None):
		keyword='card'
	else:
		keyword=keyword
	if(card_details[0]!=None):
		db=database.get_data()
		data=db.find({'email':user_details},{keyword:{'$elemMatch':{'details.card_no':card_details[0]}}})
		for line in data:
			print(line)
			type=line['card'][0]['type']
			sub_type=line['card'][0]['sub_type']
			name=line['card'][0]['details'][0]['name']
			card_no=line['card'][0]['details'][0]['card_no']
			print(card_no)
		if(card_details[0]!=card_no):
			return jsonify("Hey "+name+". Please provide correct card no.")
		else:
			return jsonify("Dear " + name + "\r\n\r\n.We'll investigate why balance in your " +sub_type+" " +type+ " no:"+ card_no + " has been lost. If your claim is genuine. We'll credit back the amount into your "+type+ " account.\r\n\r\nSorry for any inconvience you have faced from our end.Your inputs are important to us.Rest Assured.\r\n\r\nWe are here to serve you in any way possible.\r\n\r\nYou can also visit our website to check new offers on your "+type_1+".\r\n\r\nWarm Regards\r\n\r\nIntellect Design Team")

	else:
		reply="Give your Card Details"
		return jsonify(reply)

def run_server():
	if(app.debug):
		application=DebuggedApplication(app)
	else:
		application=app
	logger=logging.getLogger()
	fh=logging.FileHandler('D:\\flask_v2\\bankserver\\banklog.txt')
	logger.setLevel(logging.DEBUG)
	logger.addHandler(fh)
	server=WSGIServer(('',8787),application,log=logger)
	print("Server Start")
	server.serve_forever()







if (__name__=='__main__'):
	run_with_reloader(run_server)
	#app.run(debug=True,port=8787,threaded=True)
