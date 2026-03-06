# 7-Day Weather Data Example
import os

import requests
from datetime import datetime, timedelta

# Calculate date
today = datetime.now()
seven_days_ago = today - timedelta(days=7)

# Format dates as strings
start_date = seven_days_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

def get_seven_day_weather_data(latitude, longitude):
    # Open-Meteo API endpoint for historical weather data
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        weather_data = response.json()
        print(f"7-day weather data for latitude: {latitude}, longitude: {longitude} is as follows: {weather_data}")
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    

# Use pandas to display the data in a tabular format
import pandas as pd

def display_weather_data(weather_data, city_name):
    if weather_data and "daily" in weather_data:
        daily_data = weather_data["daily"]
        # Convert the daily data into a DataFrame for better visualization
        df = pd.DataFrame({
            "time": daily_data.get("time", []),
            "temperature_2m_max": daily_data.get("temperature_2m_max", []),
            "temperature_2m_min": daily_data.get("temperature_2m_min", [])  
        })
        #print(f"\n7-day weather data for {city_name}:")
        print(df)
    else:
        print(f"No weather data available for {city_name}.")


# Example usage
# Fetch and print 7-day weather data for New York City (latitude: 40.7128, longitude: -74.0060)
new_york_weather = get_seven_day_weather_data(40.7128, -74.0060)
# Fetch and print 7-day weather data for London (latitude: 51.5074, longitude: -0.1278)
london_weather = get_seven_day_weather_data(51.5074, -0.1278)
# Fetch and print 7-day weather data for Tokyo (latitude: 35.6895, longitude: 139.6917)
tokyo_weather = get_seven_day_weather_data(35.6895, 139.6917)
# Fetch and print 7-day weather data for Sydney (latitude: -33.8688, longitude: 151.2093)
sydney_weather = get_seven_day_weather_data(-33.8688, 151.2093)
# Fetch and print 7-day weather data for Mumbai (latitude: 19.0760, longitude: 72.8777)
mumbai_weather = get_seven_day_weather_data(19.0760, 72.8777)   

# Display the data in a tabular format
display_weather_data(new_york_weather, "New York City")
display_weather_data(london_weather, "London")
display_weather_data(tokyo_weather, "Tokyo")
display_weather_data(sydney_weather, "Sydney")
display_weather_data(mumbai_weather, "Mumbai")

# Visualize the data using matplotlib
import matplotlib.pyplot as plt

def visualize_weather_data(weather_data, city_name):
    if weather_data and "daily" in weather_data:
        daily_data = weather_data["daily"]
        dates = daily_data.get("time", [])
        max_temps = daily_data.get("temperature_2m_max", [])
        min_temps = daily_data.get("temperature_2m_min", [])
        
        plt.figure(figsize=(10, 5))
        plt.plot(dates, max_temps, label="Max Temperature (°C)", marker='o')
        plt.plot(dates, min_temps, label="Min Temperature (°C)", marker='o')
        plt.title(f"7-Day Weather Forecast for {city_name}")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.tight_layout()
        
        # create a directory to save the plots if it doesn't exist
        import os   
        if not os.path.exists("weather_plots"):
            os.makedirs("weather_plots")
        plt.savefig(f"weather_plots/{city_name}_7_day_weather.png")  # Save the plot as an image file 

        plt.show()
    else:
        print(f"No weather data available for {city_name}.")

# Visualize the data for each city
visualize_weather_data(new_york_weather, "New York City")
visualize_weather_data(london_weather, "London")
visualize_weather_data(tokyo_weather, "Tokyo")
visualize_weather_data(sydney_weather, "Sydney")
visualize_weather_data(mumbai_weather, "Mumbai")

# Export the data to a CSV file
def export_weather_data_to_csv(weather_data, city_name):
    if weather_data and "daily" in weather_data:
        daily_data = weather_data["daily"]
        df = pd.DataFrame({
            "time": daily_data.get("time", []),
            "temperature_2m_max": daily_data.get("temperature_2m_max", []),
            "temperature_2m_min": daily_data.get("temperature_2m_min", [])  
        })

        if not os.path.exists("weather_plots_csv"):
            os.makedirs("weather_plots_csv")

        df.to_csv(f"weather_plots_csv/{city_name}_7_day_weather.csv", index=False)  # Save the DataFrame to a CSV file
        print(f"Weather data for {city_name} exported to {city_name}_7_day_weather.csv")
    else:
        print(f"No weather data available for {city_name}.")

# Export the data for each city to a CSV file
export_weather_data_to_csv(new_york_weather, "New York City")
export_weather_data_to_csv(london_weather, "London")
export_weather_data_to_csv(tokyo_weather, "Tokyo")
export_weather_data_to_csv(sydney_weather, "Sydney")
export_weather_data_to_csv(mumbai_weather, "Mumbai")


