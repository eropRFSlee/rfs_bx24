import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Данные отправителя
SMTP_SERVER = "smtp.yandex.ru"
SMTP_PORT = 465
SENDER_EMAIL = "eroproralee@yandex.ru"
SENDER_PASSWORD = "erhsfnfzxbhywnmj"  # Пароль приложения, не пароль от аккаунта!

# Данные получателя
RECIPIENT_EMAIL = "egorka_li@mail.ru"

# Тема и текст письма
SUBJECT = "Тестовое письмо"
BODY = "Привет! Это тестовое письмо, отправленное через Python."

def send_email():
    try:
        # Создаем письмо
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECIPIENT_EMAIL
        msg["Subject"] = SUBJECT
        
        # Добавляем тело письма
        msg.attach(MIMEText(BODY, "plain", "utf-8"))
        
        # Подключаемся к серверу и отправляем
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            
        print("✅ Письмо успешно отправлено!")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при отправке: {e}")
        return False

if __name__ == "__main__":
    send_email()
