import tkinter as tk
import requests
import json

# Function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    api_key = "2b8aefcd7dc3bbe081e8fe045860bb4f"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = json.loads(response.text)
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        weather = data["weather"][0]["main"]

        result_text = f"Weather: {weather}\n"
        result_text += f"Temperature: {temperature}°C\n"
        result_text += f"Humidity: {humidity}%\n"
        result_text += f"Pressure: {pressure} hPa\n"
        result_text += f"Wind Speed: {wind_speed} m/s"

        result_label.config(text=result_text)
    else:
        result_label.config(text="Error occurred while fetching weather data.")

# Create the main window
window = tk.Tk()
window.title("Weather Forecasting Tool")

# Set the window size
window.geometry("400x300") 

window.configure(bg="#ECECEC")  # Set background color

# Create the GUI components
label = tk.Label(window, text="Enter City:", bg="#ECECEC", fg="#333333", font=("Arial", 14, "bold"))
label.pack(pady=10)

city_entry = tk.Entry(window, font=("Arial", 12))
city_entry.pack(pady=5)

button = tk.Button(window, text="Fetch Weather", command=fetch_weather, font=("Arial", 12, "bold"), bg="#4CAF50", fg="#FFFFFF")
button.pack(pady=10)

result_label = tk.Label(window, text="", bg="#ECECEC", fg="#333333", font=("Arial", 12), justify="left")
result_label.pack()

# Run the GUI main loop
window.mainloop()