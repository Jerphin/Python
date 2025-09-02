import requests

api_key='5c3d0c77d7760c6806debd04758533da'

user_input=input("Enter city name:")

weather_data= requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")  #permanent its in weather api

#print(weather_data.status_code)      #just to check
#print(weather_data.json())

if weather_data.json()['cod'] == '404':#cod = status code api redurns.json is used to handle data received from api.
    print("No City Found")             #api allows two appln to communicate with each other
else:
    weather = weather_data.json()['weather'][0]['main']  #0th index
    temp = round(weather_data.json()['main']['temp'])    #messier so round the temp
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}%F")
