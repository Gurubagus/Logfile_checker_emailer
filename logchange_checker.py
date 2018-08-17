import sys
import errno
import os
import time
import zipfile
import itertools
import smtplib
from smtplib import SMTP

import socket

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
m = ''
message = ''

def send_email():
    
	global name
	global m
	global message
    
	msg = MIMEMultipart()
	email = ["170ab767.benemen.com@emea.teams.ms"]
	#email = ["zactaylor.benemenacct@gmail.com"]

	# create message object instance
	
	with m as text_file:
		for line in itertools.islice(text_file, 0,5):
	
			message += str(line)
	
		

	# setup the parameters of the message
	msg['From'] = "G1ETL01@benemen.com"
	msg['To'] = ','.join(email)
	msg['Subject'] = """
	Log File: %s has a new entry.
	""" % name	
		
 
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
    
	# create server
	server = smtplib.SMTP() #connect to local system 
	server.connect(host='217.77.194.1', port=25) # connects to 'sender' server

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

				if size != 0:
					m = open(file, 'r')				
					send_email()
				else:
					pass
			


if __name__== "__main__":
    main()
        
        
    

