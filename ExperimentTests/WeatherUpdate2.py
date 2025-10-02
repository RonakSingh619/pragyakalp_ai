# OG and working

# import requests

# def get_location():
#     response = requests.get("http://ip-api.com/json/")
#     data = response.json()
#     print("Location data: ",data)
#     return data.get("city"), data.get("country"), data.get("lat"), data.get("lon")

# def get_weather(lat, lon, api_key):
#     url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
    
#     if response.status_code == 200:
#         temp = data["main"]["temp"]
#         desc = data["weather"][0]["description"]
#         humidity = data["main"]["humidity"]
#         wind = data["wind"]["speed"]
#         return temp, desc, humidity, wind
#     else:
#         raise Exception(data.get("message", "Weather fetch failed"))

# # Run it
# api_key = "6baaef20e7401f64200817c086973017"  # Replace this with your OpenWeatherMap API key
# city, country, lat, lon = get_location()
# temp, desc, humidity, wind = get_weather(lat, lon, api_key)

# print(f"📍 Location: {city}, {country}")
# print(f"🌤️ Weather: {desc}")
# print(f"🌡️ Temperature: {temp}°C")
# print(f"💧 Humidity: {humidity}%")
# print(f"🌬️ Wind Speed: {wind} m/s")


#-----------------------------------------------------------------------------------------------------------------------------------------


import requests

def get_location():
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    # print("Location data: ",data)
    return data.get("city"), data.get("country"), data.get("lat"), data.get("lon")

def get_weather(lat, lon, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        return temp, desc, humidity, wind
    else:
        raise Exception(data.get("message", "Weather fetch failed"))

# Run it
api_key = "6baaef20e7401f64200817c086973017"  # Replace this with your OpenWeatherMap API key
city, country, lat, lon = get_location()
temp, desc, humidity, wind = get_weather(lat, lon, api_key)

print(f"📍 Location: {city}, {country}")
print(f"🌤️ Weather: {desc}")
print(f"🌡️ Temperature: {temp}°C")
print(f"💧 Humidity: {humidity}%")
print(f"🌬️ Wind Speed: {wind} m/s")