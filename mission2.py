import requests
from datetime import date, datetime, timedelta

API_KEY = "95dd639c-eb29-48a5-8eeb-3466c13f9cab"
departure_station_code = "s9601675"
arrived_station_code = "s9601835"

def get_query():
    url = "https://api.rasp.yandex.net/v3.0/search/"
    headers = {
    "Content-Type": "application/json"
    }
    params = {
    "apikey": API_KEY,
    "format": "json",
    "from": departure_station_code,
    "to": arrived_station_code,
    "lang": "ru_RU",
    "page": 1,
    "date": date.today(),
    "limit": 1000
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def find_next_train():
    query = get_query()
    trains = query['segments']
    now = datetime.now()
    next_train = None
    for train in trains:
        train_datetime = datetime.strptime(train["departure"].split("+")[0], "%Y-%m-%dT%H:%M:%S")
        if train_datetime > now + timedelta(minutes=20):
            next_train = train
            break

    if next_train:
        route = next_train["thread"]["title"]
        departure_time = datetime.strptime(next_train["departure"].split("+")[0], "%Y-%m-%dT%H:%M:%S").strftime("%H:%M")
        result = f"{departure_time} - {route}"
        return result
    else:
        return "Нет доступных электричек с запасом в 20 минут"
result = find_next_train()
print(result)