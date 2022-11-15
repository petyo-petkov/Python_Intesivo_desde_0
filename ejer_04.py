import requests
import json

API_key = '92171b1ea5d6f3174092eb79dbc9f1b4'
city_name = input('Pon el nombre de la ciudad: ')
units = 'metric'
r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units={units}")

datos = r.json
data = json.loads(r.content)

print('Temperatura minima:', data['main']['temp_min'], 'ªC')
print('Temperatura máxima:', data['main']['temp_max'], 'ªC')