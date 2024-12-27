import requests
from twilio.rest import Client

# random place where it's raining at time of creating script
MY_LAT = 59.412153 # Your latitude
MY_LNG = 5.272105 # Your longitude

#openweathermap info
API_KEY = "" # hidden
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

#twilio info
account_sid = "" # hidden
auth_token = "" # hidden

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "units": "metric",
    "cnt":4,
}

response = requests.get(owm_endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    # print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain, bring an umbrella",
        from_="+12315454647",
        to="+32473589575",
    )
    print(message.status)

