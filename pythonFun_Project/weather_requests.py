import requests
import json

link = "https://api.openweathermap.org/data/2.5/weather?q=Pittsburgh&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric"
list1 = "https://api.openweathermap.org/data/2.5/weather?q="
location = "Pittsburgh"
list2 = "&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric"

city = input("Please input a city: ")
location = city
link2 = list1 + location + list2

response = requests.get(link2)
res = response.json()
print (response.json())
print(res["weather"])
print ("Today is", res["weather"][0]["description"])

print ("Tempterature is", res["main"]["temp"], "degrees.")



