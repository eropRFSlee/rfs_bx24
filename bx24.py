import requests
from flask import Flask, request  # если используете как вебхук

WEBHOOK = "https://drlk.rfs.ru/rest/205/0dt7zmzm290eqkwz/"
app = Flask(__name__)

def get_company_email(company_id):
    response = requests.post(
        f"{WEBHOOK}crm.company.get",
        json={"id": company_id}
    )
    data = response.json()
    if "result" in data and "EMAIL" in data["result"]:
        return data["result"]["EMAIL"][0]["VALUE"]
    return None

def update_company_email(company_id, email):
    """Обновить email компании"""
    requests.post(
        f"{WEBHOOK}crm.company.update",
        json={"id": company_id, "fields": {"EMAIL": [{"VALUE": email, "VALUE_TYPE": "WORK"}]}}
    )

# Вариант 1: Запуск по расписанию
def scheduled_job():
    # Получаем ID компаний без email
    response = requests.post(
        f"{WEBHOOK}crm.company.list",
        json={"select": ["ID"], "filter": {"EMAIL": ""}}
    )
    companies = response.json().get("result", [])
    
    for company in companies:
        # Здесь ваша логика
        pass

# Вариант 2: Как вебхук (Битрикс24 вызывает этот URL)
@app.route('/bitrix-webhook', methods=['POST'])
def bitrix_webhook():
    data = request.json
    company_id = data.get('data', {}).get('FIELDS', {}).get('ID')
    
    if company_id:
        email = get_company_email(company_id)
        # Здесь ваша логика с email
        
    return {"status": "ok"}

if __name__ == '__main__':
    # Для расписания: запускаем scheduled_job()
    # Для вебхука: запускаем Flask
    app.run(host='0.0.0.0', port=5000)
