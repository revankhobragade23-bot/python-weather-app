import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()

    city_name = data["name"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n--- Weather Report ---")
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Weather: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
   

else:
   print("API request failed.")
   print("Details:", response.text)
