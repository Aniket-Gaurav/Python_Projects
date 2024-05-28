import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = "768abe60a80d3d018c404486e3287509"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = round(data["main"]["temp"] - 273.15, 2)

            weather_label.config(text=f"Weather: {weather_description}")
            temperature_label.config(text=f"Temperature: {temperature}°C")
        elif data["cod"] == "404":
            messagebox.showerror("Error", f"City '{city}' not found. Please try again.")
            weather_label.config(text="")
            temperature_label.config(text="")
        else:
            weather_label.config(text="An error occurred")
            temperature_label.config(text="")
    except requests.exceptions.RequestException:
        weather_label.config(text="Error: Could not connect to the API")
        temperature_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")  # Set the initial size of the window
root.resizable(False, False)  # Disable window resizing

# Create a label and entry field for the city
city_label = tk.Label(root, text="Enter city name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Create a button to get the weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Create labels to display the weather information
weather_label = tk.Label(root, text="")
weather_label.pack(pady=5)

temperature_label = tk.Label(root, text="")
temperature_label.pack(pady=5)

# Start the main event loop
root.mainloop()