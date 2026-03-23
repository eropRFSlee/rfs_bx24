import datetime
from flask import Flask, request
import requests

WEBHOOK = "https://drlk.rfs.ru/rest/205/l1slr5kjtd5vujiq/"
app = Flask(__name__)

@app.route('/outhookfromb24/', methods=['POST', 'GET'])
def outhookfromb24():
    # Записываем в лог факт вызова
    with open('wh_saver.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} Вызвали этот адрес: https://rfs-bx24-final-pls.onrender.com/outhookfromb24/ \r")
    
    # Получаем данные от Битрикс24
    data = request.json
    with open('wh_saver.txt', 'a') as f:
        f.write(f"Данные: {data}\r\n")
    
    # Извлекаем ID сделки
    deal_id = None
    if data:
        deal_id = data.get('data', {}).get('FIELDS', {}).get('ID')
        if not deal_id:
            deal_id = data.get('data', {}).get('FIELDS_ID')
    
    if deal_id:
        with open('wh_saver.txt', 'a') as f:
            f.write(f"Найден ID сделки: {deal_id}\r\n")
        
        # Меняем название сделки
        try:
            response = requests.post(
                f"{WEBHOOK}crm.deal.get",
                json={"id": deal_id}
            )
            deal = response.json().get("result")
            
            if deal:
                old_title = deal.get("TITLE", "")
                new_title = f"[РОБОТ] {old_title}"
                
                requests.post(
                    f"{WEBHOOK}crm.deal.update",
                    json={
                        "id": deal_id,
                        "fields": {"TITLE": new_title}
                    }
                )
                with open('wh_saver.txt', 'a') as f:
                    f.write(f"Название изменено на: {new_title}\r\n")
        except Exception as e:
            with open('wh_saver.txt', 'a') as f:
                f.write(f"Ошибка: {e}\r\n")
    
    return "Outhookfromb24"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
