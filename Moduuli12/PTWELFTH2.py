import requests
import json

paikkakunta = str(input("Anna paikkakunnan nimi: "))

pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit={1}&appid="
vastaus = requests.get(pyyntö).json()

lat = vastaus[0]["lat"]
lon = vastaus[0]["lon"]

pyyntö2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid="
vastaus2 = requests.get(pyyntö2).json()

celsius = round(vastaus2["main"]["temp"] - 273.15, 0)
säätila = vastaus2["weather"][0]["main"]

print(f"Paikkakunnan {paikkakunta} lämpötila on {celsius}°C ja Säätila on {säätila}")