# Weather API Example without API Key
# This example demonstrates how to fetch weather data from a public API that does not require an API key. We will use the Open-Meteo API, which provides weather forecasts and historical data.

import requests
def get_weather_data(latitude, longitude):
    # Open-Meteo API endpoint for current weather data
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        weather_data = response.json()
        # print(f"Weather data for latitude: {latitude}, longitude: {longitude} is as follows: {weather_data}")
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Example usage
def fetch_and_print_weather(latitude, longitude, city_name):
    weather_data = get_weather_data(latitude, longitude)
    if weather_data:
        current_weather = weather_data.get("current_weather", {})
        temperature = current_weather.get("temperature")
        wind_speed = current_weather.get("windspeed")
        print(f"Current weather in {city_name}:")
        print(f"* Current temperature: {temperature}°C")
        print(f"* Current wind speed: {wind_speed} km/h")

# Fetch and print weather data for New York City (latitude: 40.7128, longitude: -74.0060)
new_york_weather = fetch_and_print_weather(40.7128, -74.0060, "New York City")

# Fetch and print weather data for London (latitude: 51.5074, longitude: -0.1278)
london_weather = fetch_and_print_weather(51.5074, -0.1278, "London")

# Fetch and print weather data for Tokyo (latitude: 35.6895, longitude: 139.6917)
tokyo_weather = fetch_and_print_weather(35.6895, 139.6917, "Tokyo")

# Fetch and print weather data for Sydney (latitude: -33.8688, longitude: 151.2093)
sydney_weather = fetch_and_print_weather(-33.8688, 151.2093, "Sydney")

# Fetch and print weather data for Mumbai (latitude: 19.0760, longitude: 72.8777)
mumbai_weather = fetch_and_print_weather(19.0760, 72.8777, "Mumbai")
