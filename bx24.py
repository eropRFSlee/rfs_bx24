import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask
import os

app = Flask(__name__)

SMTP_SERVER = "smtp.yandex.ru"
SMTP_PORT = 465
SENDER_EMAIL = "eroproralee@yandex.ru"
SENDER_PASSWORD = "erhsfnfzxbhywnmj"
RECIPIENT_EMAIL = "egorka_li@mail.ru"
SUBJECT = "Тестовое письмо"
BODY = "Привет! Это тестовое письмо, отправленное через Python."

def send_email():
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = SUBJECT
    msg.attach(MIMEText(BODY, "plain", "utf-8"))
    
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
    
    return "OK"

@app.route('/')
def index():
    return send_email()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
