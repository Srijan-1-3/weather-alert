import requests
import smtplib


API_KEY = 'fe48c3b7be24dc7eac1717782f16d5b6'


parameters = {
    'q' :'Mumbai',
    'appid' : API_KEY
}

response = requests.get(url='http://api.openweathermap.org/data/2.5/weather',params=parameters)

print(response.json())