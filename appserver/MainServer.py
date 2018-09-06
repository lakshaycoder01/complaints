from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
from gevent.pywsgi import WSGIServer
from werkzeug.serving import run_with_reloader
from werkzeug.debug import DebuggedApplication
import logging
from process import mainfunction



app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
@cross_origin()
def predict():                                       #request will come here
	request_data=request.get_json(force=True)
	mail_text=data['msg']
	user_mail=data['from']
	mail_response=mainfunction(mail_text,user_mail)
	return mail_response

def run_server():
	if(app.debug):
		application=DebuggedApplication(app)
	else:
		application=app
	logger=logging.getLogger()
	fh=logging.FileHandler('D:\\flask_v2\\appserver\\applog.txt')
	logger.setLevel(logging.DEBUG)
	logger.addHandler(fh)
	server=WSGIServer(('',8545),application,log=logger)
	print("Server Start")
	server.serve_forever()
	
	
if (__name__=='__main__'):
	
	run_with_reloader(run_server)
	#serve(application,listen='localhost:8545')
	#application.run(debug=True,port=8545,threaded=True)
