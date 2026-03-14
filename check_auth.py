import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("YANDEX_TOKEN")
URL = "https://cloud-api.yandex.net/v1/disk/"

def check_connection():
    headers = {
        "Authorization": f"OAuth {TOKEN}",
    }
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("✅ Связь установлена!")
        print(f"Владелец диска: {data['user']['display_name']}")
        print(f"Свободное место: {data['total_space'] - data['used_space']} байт")
    else:
        print(f"❌ Ошибка! Статус-код: {response.status_code}")
        print(f"Ответ сервера: {response.text}")

if __name__ == "__main__":
    check_connection()