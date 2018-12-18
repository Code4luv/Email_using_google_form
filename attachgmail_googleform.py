import oauth2client
import gspread
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import imaplib
from base64 import encodebytes 
from oauth2client.service_account import ServiceAccountCredentials

from_address="email address"
scope=["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client=gspread.authorize(creds)
sheet=client.open("Form Name (Responses)").sheet1
list_of_hashes=sheet.col_values(2)#instead of 2 no,insert number of column where the email address are in your google form

toaddress=np.array(list_of_hashes[1:])

msg =MIMEMultipart()
msg['From']=from_address
msg['To']=toaddress
msg['Subject']="subject"
body="ur message"
msg.attach(MIMEText(body,'plain'))
filename="name of file to be attached"
attachment=open(" location of file upto file","rb")
p=MIMEBase('application','octet-stream')

att = MIMEApplication(attachment.read(),_subtype="type of file zip or txt")
attachment.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)


mail= smtplib.SMTP_SSL('smtp.gmail.com:465')

mail.ehlo()

mail.login(from_address,'password')
text=msg.as_string()

mail.sendmail(from_address,i,text)
mail.quit()
