import csv
import requests
from requests import Response
from datetime import datetime as dt


def url_weather(city: str, forecast: int) -> str:
    return f'http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={forecast}' \
           f'&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8'


def url_json(url: str) -> Response:
    return requests.get(url).json()


def date_weather(response: Response) -> list:
    result = []
    for dates in response['list']:
        result.append(dt.fromtimestamp(dates['dt']).strftime("%d-%m-%Y"))
    return result


def temp_list(response: Response, key: str) -> list:
    result = []
    for temp in response['list']:
        result.append(temp['temp'][key])
    return result


def average_temp(response: Response) -> list:
    result = []
    for item in response['list']:
        average = round((item['temp']['max'] + item['temp']['min']) / 2, 2)
        result.append(average)
    return result


def temp_collection(d: list, average: list, day: list, night: list) -> list:
    result = []
    for dates, avg, _day, _night in zip(d, average, day, night):
        result.append({'date': dates, 'avg': avg, 'day': _day, 'night': _night})
    return result


def file_name(city: str, forecast: int) -> str:
    result = f'{dt.now().strftime("%d-%m-%Y")} {city.capitalize()} {forecast} days weather forecast.txt'
    return result.replace(' ', '-')


def file_create(name_file: str, data: list):
    with open(name_file, 'w') as f:
        writer = csv.DictWriter(f, delimiter='\t', fieldnames=data[0])
        writer.writeheader()
        for items in data:
            writer.writerow(items)


def main():
    city = str(input("Enter the city: "))
    forecast = int(input("Enter for how many days forecast you want: "))
    url = url_weather(city, forecast)
    file = file_name(city, forecast)
    response = url_json(url)

    dates_list = date_weather(response)
    avg = average_temp(response)
    day = temp_list(response, 'day')
    night = temp_list(response, 'night')
    suma = temp_collection(dates_list, avg, day, night)
    file_create(file, suma)


if __name__ == '__main__':
    main()
