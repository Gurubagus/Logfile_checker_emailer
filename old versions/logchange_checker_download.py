import sys
import errno
import os
import time
import zipfile
import smtplib
import socket

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
m = ''

def send_email():
    
	global name
	global ksize
	global m
    
	msg = MIMEMultipart()
	
	# create message object instance
	message = m.read()

	# setup the parameters of the message
	msg['From'] = "mikko.muurinen@benemen.com"
	
	msg['To'] =  "170ab767.benemen.com@emea.teams.ms"
	msg['Subject'] = """
	Log File: %s has a new entry.
	""" % name
    
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
    
	# create server
	server = smtplib.SMTP('localhost')

	server.connect(host='217.77.194.1', port=25)

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
		if file.endswith('.txt'):
			if file != 'DW_Status_checks.txt':
				statinfo = os.stat(file)
				size = statinfo.st_size
				name = file

				if size > 0:
					m = open(file,'r')				
					send_email()
				else:
					pass
			


if __name__== "__main__":
    main()
        
        
    

