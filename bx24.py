from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK = "https://drlk.rfs.ru/rest/205/euti36505v9h07wx/"

def get_all_emails():
    emails = []
    start = 0
    
    while True:
        r = requests.post(f"{WEBHOOK}crm.company.list", json={
            "select": ["ID", "EMAIL"],
            "start": start
        })
        data = r.json()
        
        for company in data["result"]:
            email = company.get("EMAIL")
            if email:
                emails.append(email)
        
        if not data.get("next"):
            break
        start = data["next"]
    
    return emails

@app.route('/check_email', methods=['POST'])
def check_email():
    data = request.get_json()
    email_to_check = data.get('email', '')
    
    if not email_to_check:
        return jsonify({'found': False})
    
    all_emails = get_all_emails()
    found = email_to_check in all_emails
    
    return jsonify({'found': found})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
