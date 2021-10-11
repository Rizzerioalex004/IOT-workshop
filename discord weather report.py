import urequests as requests
import ujson as json

url = "https://discord.com/api/webhooks/890543506731446273/ShZkMwZ-fMwA7egdOuGxueSKJyByw204Vt0gYkLkL5xu2TYtEvBiwEMh2ZpKQcNGtAdC"
headers = {
    "Content-Type": "application/json"
}

while True:
    country_code = input("Enter the country code: ")
    city = input("Enter the city name: ")

    weather_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country_code + "&APPID=b190a0605344cc4f3af08d0dd473dd25"
    weather_data = requests.get(weather_url)

    # Location (City and Country code)
    location = "Location: " + weather_data.json().get("name") + " - " + weather_data.json().get("sys").get("country")

    # Weather Description
    description = "Description: " + weather_data.json().get("weather")[0].get("main")

    # Temperature
    raw_temperature = weather_data.json().get("main").get("temp")-273.15
    temperature = "Temperature: " + str(raw_temperature) + "*C"

    # Pressure
    pressure = "Pressure: " + str(weather_data.json().get("main").get("pressure")) + "hPa"

    # Humidity
    humidity = "Humidity: " + str(weather_data.json().get("main").get("humidity")) + "%"

    # Wind
    wind = "Wind: " + str(weather_data.json().get("wind").get("speed")) + "mps " + str(weather_data.json().get("wind").get("deg")) + "*"

    payload = json.dumps({
        "content": "----Weather Report----\n" + location + "\n" + description + "\n" + temperature + "\n" + pressure + "\n" + humidity + "\n" + wind + "",
    })
    response = requests.post(url, headers=headers, data=payload)
    print(response.json)
 
