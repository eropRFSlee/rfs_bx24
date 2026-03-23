from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Сервер работает. Перейдите на /send-webhook для отправки теста"

@app.route('/send-webhook')
def send_webhook():
    try:
        # Отправляем запрос на webhook.site
        response = requests.post(
            'https://webhook.site/730c442c-cbf6-4c4e-a0ea-68d6b49390d7',
            json={
                'test': 'Привет от render.com',
                'time': 'проверка связи',
                'status': 'ok'
            }
        )
        
        return f"Запрос отправлен. Статус ответа: {response.status_code}"
    
    except Exception as e:
        return f"Ошибка: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
