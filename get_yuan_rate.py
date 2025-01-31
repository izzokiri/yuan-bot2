import requests

def get_yuan_rate():
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, нет ли ошибки
        data = response.json()
        return data["Valute"]["CNY"]["Value"]
    except Exception as e:
        print(f"Ошибка при получении курса: {e}")
        return None
