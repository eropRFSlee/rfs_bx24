from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_email', methods=['POST'])
def check_email():
    data = request.get_json()
    email = data.get('email', '') if data else ''
    
    # Просто возвращаем успешный ответ
    return jsonify({'found': False, 'received': email}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
