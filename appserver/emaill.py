import imaplib,email,os
import json,requests
import ctypes
import getpass
import re
import time

imap_url='imap.gmail.com'
port=25
usr="intellect2345@gmail.com"

password=passwd =getpass.getpass('enter it')

m=imaplib.IMAP4_SSL(imap_url)
direc='archive_today'

typ,accountdetails=m.login(usr,password)
if(typ!='OK'):
		print("No sign in")
		raise

def get_body(msg):
	if(msg.is_multipart()):
		return get_body(msg.get_payload(0))
	else:
		return msg.get_payload(None,True)
		
		
def get_mail():
	
	m.select('Inbox')

	typ,data=m.uid('search', None, 'UNSEEN')
	if(typ!='OK'):
		print("Error searching inbox")
		raise
	data1=data[0].split()
	for msgid in data1:
		type,messageparts=m.fetch(msgid,('RFC822'))
		if(typ!='OK'):
			print("Error fetching mail")
			raise
		emailbody=messageparts[0][1].decode('utf-8')
		mail=email.message_from_string(emailbody)
		text=get_body(mail)
		text=text.decode()
		text=re.sub(r'\r\n', ' ', text)
		emaill=mail['From']
		emaill = re.findall(r'[\w\.-]+@[\w\.-]+', emaill)
		print(emaill[0])
		
		if(emaill!=None):
			url='http://localhost:8545'
			data=json.dumps({'msg':text,'from':emaill[0]})
			print(data)
			rr=requests.post(url,data)
			print(rr.json())
		else:
			print("there is no new mail to responsed for currently")
		

	
if __name__ == "__main__":
	
	
    while True:
		
        get_mail()
        time.sleep(15)
	
	

