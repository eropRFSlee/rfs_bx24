import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "egor58241@gmail.com"
SENDER_PASSWORD = "lrmg pate yxhj tkpe"  # твой пароль приложения
RECIPIENT_EMAIL = "eroproralee@yandex.ru"
SUBJECT = "Тестовое письмо"
BODY = "Привет! Это тестовое письмо."

def send_email():
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = SUBJECT
    msg.attach(MIMEText(BODY, "plain", "utf-8"))
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    send_email()
