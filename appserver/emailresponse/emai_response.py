import email
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_address='intellect2345@gmail.com'
password='takeiteasy'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_address, password)


def send_mail(user_details,response,subject):
	msg = MIMEMultipart()
	msg['From'] = email_address
	msg['To'] = user_details
	msg['Subject'] = subject
	msg.attach(MIMEText(response, 'plain'))
	text = msg.as_string()
	server.sendmail(email_address,[user_details], text)
	server.quit()
	print("Message send")
	return "Email Send"



 



