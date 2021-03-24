from datetime import datetime
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
import os

def get_email_client():
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(os.environ['EMAIL_ADDRESS'], os.environ['GMAIL_APP_PASS'])
	return server

def send_text(city, vaccine_type, link):
	text = "{} has a {} vaccine available".format(city, vaccine_type)
	text += "\n {}".format(link)
	send_msg(text, city, vaccine_type, link)

def send_msg(text, city, vaccine_type, link):
	server = get_email_client()
	
	from_addr = os.environ['EMAIL_ADDRESS']
	to_addr = [""] # YOUR PHONE NUMBER EMAIL GOES HERE


	try:
		for num in to_addr:
			msg = MIMEMultipart()
			msg['From'] = from_addr
			msg['To'] = num
			msg['Subject'] = "{} {} vaccine".format(city, vaccine_type)

			msg.attach(MIMEText(text.encode('utf-8'), _subtype='html', _charset="UTF-8"))
			server.sendmail(from_addr, num, msg.as_string())
			print("Sent text to {}".format(num))
		server.quit()
	except Exception as e:
		print("Error!")
		print(e)
