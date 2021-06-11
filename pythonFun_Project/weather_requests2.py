import requests
import json

# link = "https://api.openweathermap.org/data/2.5/weather?q=Pittsburgh&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric"
url = "https://api.openweathermap.org/data/2.5/weather"
parameters = {"q":"Pittsburgh","APPID":"b35975e18dc93725acb092f7272cc6b8","units":"metric"}

city = input("Please input a city: ")
parameters ["q"] = city

res = requests.get (url, parameters)
print (res.json())
