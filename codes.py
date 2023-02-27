# Importing required Libraries
import pandas as pd
from email.mime.application import MIMEApplication
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Enter your email ID and password
email = 'useyouremailid@gmail.com'
password = 'password'

#enter the address to which email need to be sent
send_to_email = ['abc@gmaill.com']
cc_to_email=['123@gmaill.com']
subject = 'Testing'

# mention the location of attachment or send a dataframe as attachment
data1=pd.read_csv("C:/file_location/file.csv")

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = ", ".join(send_to_email)
msg['Cc'] = ", ".join(cc_to_email)
msg['Subject'] = subject

# Setup the attachment
filename1='data1.csv'
# Attach the dataframe to the MIMEMultipart object
textStream = StringIO()
data1.to_csv(textStream,index=False)
part1 = MIMEApplication(textStream.getvalue(), Name=filename1)
msg.attach(part1)

# Customizing the body of email using HTML
html = """<html><head>Hi,<br><br>Greetings and Welcome.</head></html>"""
part1 = MIMEText(html, 'html')
msg.attach(part1)
        
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
send_to_email.extend(cc_to_email)
server.sendmail(email,send_to_email,msg.as_string())
server.quit()
