import sys
import errno
import os
import time
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    
	global name
	global ksize
    
	msg = MIMEMultipart()
	
	username = 'add8b392c0958c'
	password = '5bbdd41abe1990'
	
	# create message object instance
	message = "%s has a new entry." % name

	# setup the parameters of the message
	msg['From'] = "zachary.taylor@benemen.com"
	
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
	
	cwd = os.getcwd()
	f = os.listdir(cwd)
    
	for file in f:
		statinfo = os.stat(file)
		size = statinfo.st_size
		kbsize = size/1000
		name = file

		if size > 0:
			send_email()
		else:
			pass
			


if __name__== "__main__":
    main()
        
        
    

