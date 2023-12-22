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

# ? где типизация
def find_next_train() -> str:
    query: dict = get_query()
    # ? какой тип данных возвращает
    trains: list[dict] = query['segments']
    now: datetime.datetime = datetime.now()
    # Зачем?
    next_train: None | dict = None
 
    for train in trains:
        # ?
        train_departure: str = train["departure"]
        train_datetime: datetime.datetime = datetime.strptime(train_departure.split("+")[0], "%Y-%m-%dT%H:%M:%S")
        if train_datetime > now + timedelta(minutes=20):
            next_train = train
            break

    if next_train:
        route: str = next_train["thread"]["title"]
        departure_time = datetime.strptime(next_train["departure"].split("+")[0], "%Y-%m-%dT%H:%M:%S").strftime("%H:%M")
        result: str = f"{departure_time} - {route}"
        return result
    else:
        return "Нет доступных электричек с запасом в 20 минут"

result: str = find_next_train()
print(result)