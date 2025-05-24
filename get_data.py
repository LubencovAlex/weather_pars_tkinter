import requests
from bs4 import BeautifulSoup
from weather import Weather
import random
import re

url = "https://world-weather.ru/"

# Список десктопных users
users = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7"
]

# Выбор случайной строки users
user = random.choice(users)

# Указываем user agent в заголовках запроса перед выполнением запроса
header = {"user-agent": user}

def get_weather_data():
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, 'lxml')

    city_name = soup.find('div', class_="loc-now-t-city").find('a').text
    current_time = soup.find('div', class_="loc-now-t").find('div', class_="loc-now-time").text.split(" ")[2]
    temp_current = soup.find('div', class_="loc-now-b").find('div', class_="loc-now-temp-i").text.strip('\n')
    details = soup.find('div', class_="loc-now-b").find('div', class_="loc-now-temp-atm").text
    data = soup.find('div', class_="loc-now-b").find_all('div', class_="loc-now-data-row")

    presure_text = data[0].text
    match_presure = re.search(r'[0-9].*', presure_text)
    if match_presure:
        presure = match_presure.group()

    wind_text = data[1].text
    match_wind = re.search(r'[0-9].*', wind_text)
    if match_wind:
        wind = match_wind.group()

    humidity_text = data[2].text
    match_humidity = re.search(r'[0-9].*', humidity_text)
    if match_humidity:
        humidity = match_humidity.group()

    return  Weather(city_name, current_time, temp_current, details, presure, wind, humidity)