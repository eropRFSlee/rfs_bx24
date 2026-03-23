from flask import Flask, request
import requests
import json

app = Flask(__name__)

BITRIX_WEBHOOK = 'https://drlk.rfs.ru/rest/205/euti36505v9h07wx/'
print(f"Вебхук загружен: {BITRIX_WEBHOOK}")

@app.route('/webhook', methods=['POST'])
def webhook():
    print("=" * 50)
    print("Получен запрос от Битрикс24!")
    
    if request.is_json:
        data = request.json
        print("Формат JSON:", json.dumps(data, indent=2, ensure_ascii=False))
    else:
        data = request.form.to_dict()
        print("Формат FORM:", data)
    
    print("=" * 50)
    return "OK", 200

# НОВЫЙ ТЕСТОВЫЙ МАРШРУТ
@app.route('/test-webhook', methods=['GET'])
def test_webhook():
    try:
        response = requests.post(
            'https://webhook.site/730c442c-cbf6-4c4e-a0ea-68d6b49390d7',
            json={'test': 'Hello from render.com', 'source': 'rfs-bx24'}
        )
        return f"Test sent. Status: {response.status_code}", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
