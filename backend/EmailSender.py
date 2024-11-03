import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from oauthlib.oauth2 import WebApplicationClient
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
client = WebApplicationClient(client_id)

BACKEND_HOST = ""

def send_verification_email(email, verification_code):
    sender_email = ''
    sender_name = ''
    subject = 'Email Verification'
    body = f'Your verification code is: {verification_code}'

    smtp_server = 'smtp.gmail.com'
    port = 587

    message = MIMEMultipart()
    message['From'] = f'{sender_name} <{sender_email}>'
    message['To'] = email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP(smtp_server, port)
    smtp.starttls()
    smtp.login(sender_email, os.environ.get('EMAIL_PASSWORD'))
    smtp.sendmail(sender_email, email, message.as_string())
    smtp.quit()


