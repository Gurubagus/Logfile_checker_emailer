import sys
import errno
import os
import time
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
m =''

def send_email():
    
	global name
	global ksize
	global m
    
	msg = MIMEMultipart()
	
	# create message object instance
	message = m.read()

	# setup the parameters of the message
	msg['From'] = "zachary.taylor@benemen.com"
	
	# username/password for Mailtrap.io - decomment to activate
	username = "add8b392c0958c"
	password = "5bbdd41abe1990"

	
	msg['To'] = "mikko.muurinen@benemen.com"
	msg['Subject'] = """
	Log File %s has a new entry.
	""" % name
    
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
    
	# create server
	server = smtplib.SMTP('smtp.mailtrap.io: 2525') #Test Server @Mailtrap.io usrname:zachary.taylor@benemen.com psswrd:benementestserver
	#server = smtplib.SMTP('217.77.194.1: 25')
	server.starttls()
    
	#Login Credentials for sending the mail
	
	server.login(username, password) #for Mailtrap.io decomment to activate
	#server.connect()
	# send the message via the server
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	server.quit()
	print('email successfully sent')
	
def main():
	global name
	global m
	
	cwd = os.getcwd()
	f = os.listdir(cwd)
    
	for file in f:
		if file != 'logchange_checker.py':
			statinfo = os.stat(file)
			size = statinfo.st_size
			kbsize = size/1000
			name = file

			if size > 0:
				m = open(file,'r')
				send_email()
			else:
				pass
			


if __name__== "__main__":
    main()
        
        
    

