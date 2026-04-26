import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()
    
    current = data['current_condition'][0]
    temp = current['temp_C']
    feels = current['FeelsLikeC']
    desc = current['weatherDesc'][0]['value']
    humidity = current['humidity']
    wind = current['windspeedKmph']
    
    print(f"🌍 Погода в {city}:")
    print(f"🌡️ Температура: {temp}°C")
    print(f"🤔 Відчувається як: {feels}°C")
    print(f"☁️ Опис: {desc}")
    print(f"💧 Вологість: {humidity}%")
    print(f"💨 Вітер: {wind} км/год")

city = input("Введи місто: ").strip().replace("^@", "")
get_weather(city)
