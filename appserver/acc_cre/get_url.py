from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin

app=Flask(__name__)
CORS(app)

@app.route('/',methods=['POST','GET'])
def live():
	return "Hello World"







if(__name__=='__main__'):
	app.run(debug=True,port=8765,threaded=True,use_reloader=True)
	app.run(ssl_context=('cert.pem', 'key.pem'))