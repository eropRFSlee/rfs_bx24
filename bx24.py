import requests
from flask import Flask, request

WEBHOOK = "https://drlk.rfs.ru/rest/205/l1slr5kjtd5vujiq/"
app = Flask(__name__)

@app.route('/bitrix-webhook', methods=['POST'])
def bitrix_webhook():
    # Получаем данные от Битрикс24
    data = request.json
    
    # Извлекаем ID сделки (в зависимости от события может быть в разных местах)
    deal_id = data.get('data', {}).get('FIELDS', {}).get('ID')
    if not deal_id:
        deal_id = data.get('data', {}).get('FIELDS_ID')
    
    if not deal_id:
        return {"error": "No deal ID"}, 400
    
    # Получаем текущее название сделки
    response = requests.post(f"{WEBHOOK}crm.deal.get", json={"id": deal_id})
    deal = response.json().get("result")
    
    if deal:
        old_title = deal.get("TITLE", "")
        # Меняем название, добавляя пометку
        new_title = f"[РОБОТ] {old_title}"
        requests.post(f"{WEBHOOK}crm.deal.update", json={
            "id": deal_id,
            "fields": {"TITLE": new_title}
        })
    
    return {"ok": True}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
