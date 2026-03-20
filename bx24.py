import requests
from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

WEBHOOK = "https://drlk.rfs.ru/rest/205/l1slr5kjtd5vujiq/"
app = Flask(__name__)

# НАСТРОЙКИ ПОЧТЫ — НУЖНО УТОЧНИТЬ
SMTP_SERVER = "smtp.rfs.ru"  # ИЛИ smtp.mail.ru — УТОЧНИ
SMTP_PORT = 587
SMTP_USER = "li_ea@rfs.ru"
SMTP_PASSWORD = "Pavino16....."

def get_deal_fields(deal_id):
    response = requests.post(
        f"{WEBHOOK}crm.deal.get",
        json={"id": deal_id}
    )
    data = response.json()
    if "result" in data:
        return data["result"]
    return None

@app.route('/bitrix-webhook', methods=['POST'])
def bitrix_webhook():
    data = request.json
    deal_id = data.get('data', {}).get('FIELDS', {}).get('ID')
    
    if not deal_id:
        return {"status": "error", "message": "No deal ID"}, 400
    
    deal = get_deal_fields(deal_id)
    if not deal:
        return {"status": "error", "message": "Deal not found"}, 404
    
    # Получаем поля по их кодам
    surname = deal.get("UF_CRM_DEAL_1773845091277", "")
    name = deal.get("UF_CRM_DEAL_1773845130405", "")
    club_name = deal.get("UF_CRM_DEAL_1773909188274", "")
    club_email = deal.get("UF_CRM_DEAL_1773914938948", "")
    
    # Формируем письмо
    subject = f"Ваше обращение по футболисту {surname} {name} зарегистрировано"
    body = f"Заявка на футболиста {surname} {name} для регистрации в {club_name} принята."
    
    # Отправляем
    if club_email:
        try:
            msg = MIMEMultipart()
            msg['From'] = SMTP_USER
            msg['To'] = club_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
            server.quit()
            print(f"Письмо отправлено на {club_email}")
        except Exception as e:
            print(f"Ошибка: {e}")
    
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
