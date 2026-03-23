from flask import Flask, request
import requests
import json
from datetime import datetime

app = Flask(__name__)

# Ваш входящий вебхук (токен)
BITRIX_WEBHOOK = 'https://drlk.rfs.ru/rest/205/euti36505v9h07wx/'
print(f"Вебхук загружен: {BITRIX_WEBHOOK}")

# ========== МАРШРУТ ДЛЯ РОБОТА (ЕГО ВЫЗЫВАЕТ БИТРИКС) ==========
@app.route('/webhook', methods=['POST'])
def webhook():
    print("=" * 60)
    print(f"[{datetime.now()}] ПОЛУЧЕН ЗАПРОС ОТ БИТРИКС24!")
    
    # Получаем данные, которые прислал Битрикс24
    data = request.form.to_dict()
    print("Данные от Битрикс:", data)
    
    # Из данных достаем ID сделки (он может быть в разных ключах)
    deal_id = None
    if 'data[FIELDS][ID]' in data:
        deal_id = data['data[FIELDS][ID]']
    elif 'id' in data:
        deal_id = data['id']
    
    if deal_id:
        print(f"Получен ID сделки: {deal_id}")
        
        # Теперь запрашиваем полные данные сделки через входящий вебхук
        try:
            url = f"{BITRIX_WEBHOOK}crm.deal.get.json"
            params = {'id': deal_id}
            response = requests.get(url, params=params)
            deal_data = response.json()
            
            print(f"Полные данные сделки {deal_id}:")
            print(json.dumps(deal_data, indent=2, ensure_ascii=False))
            
        except Exception as e:
            print(f"Ошибка при получении данных сделки: {e}")
    else:
        print("ID сделки не найден в полученных данных")
    
    print("=" * 60)
    return "OK", 200

# ========== ГЛАВНАЯ СТРАНИЦА ДЛЯ ПРОВЕРКИ ==========
@app.route('/')
def home():
    return "Сервер работает. Робот настроен на /webhook"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
