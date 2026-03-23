from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Сервер работает. Перейдите на /get-deal для проверки"

@app.route('/get-deal')
def get_deal():
    try:
        # Правильный GET-запрос к методу crm.deal.get
        url = 'https://drlk.rfs.ru/rest/205/euti36505v9h07wx/crm.deal.get.json'
        params = {'id': 3555}
        
        response = requests.get(url, params=params)
        
        # Форматируем ответ для читаемости
        data = response.json()
        return f"""
        <pre>
        Статус: {response.status_code}
        Ответ:
        {json.dumps(data, indent=2, ensure_ascii=False)}
        </pre>
        """
    
    except Exception as e:
        return f"Ошибка: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
