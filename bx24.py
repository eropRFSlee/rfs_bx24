from flask import Flask, request
import os

app = Flask(__name__)

# Проверяем, что переменная окружения загрузилась
BITRIX_WEBHOOK = 'https://drlk.rfs.ru/rest/205/euti36505v9h07wx/'
print(f"Вебхук загружен: {BITRIX_WEBHOOK}")

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Получен запрос от Битрикс24!")
    print("Данные:", request.json)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
