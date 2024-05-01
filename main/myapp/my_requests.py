import requests

url = 'http://127.0.0.1:8000/api/data/'

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Ошибка при запросе: ", response.status_code)
except requests.exceptions.RequestException as e:
    print("Ошибка при запросе:", e)
