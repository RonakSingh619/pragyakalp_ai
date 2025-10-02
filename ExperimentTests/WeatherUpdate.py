import requests
import json

def get_weather(city, api_key):
    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use Celsius for temperature
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse the JSON response
        data = response.json()
        
        # Extract relevant weather information
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

        return weather
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data: {str(e)}"}
    except KeyError:
        return {"error": "Invalid response from API. Check city name or API key."}

def main():
    # Replace with your OpenWeatherMap API key
    api_key = "6baaef20e7401f64200817c086973017"
    city = "India"  # Example city, can be changed dynamically

    # Get weather data
    weather_data = get_weather(city, api_key)
    
    # Print results
    if "error" in weather_data:
        print(weather_data["error"])
    else:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description'].capitalize()}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")

# For Pyodide compatibility
import platform
import asyncio

if platform.system() == "Emscripten":
    async def async_main():
        main()
    asyncio.ensure_future(async_main())
else:
    if __name__ == "__main__":
        main()