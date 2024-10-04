import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
auth_token = ""
account_sid = ""

weather_params = {
    "lat": 16.992500,
    "lon": 73.294197,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        body = "Bring an Umbrella☂️",
        from_='+12525125508',
        to='+917620848378'
    )

    print(message.sid)
