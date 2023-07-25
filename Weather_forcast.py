import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    location = entry.get()
    if location:
        api_key = "YOUR_API_KEY"  # Replace with your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"]

                result_text = f"Weather in {location}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}"
                result_label.config(text=result_text)
            else:
                messagebox.showerror("Error", "Unable to retrieve weather data.")

        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Failed to connect to the weather service.")
    else:
        messagebox.showwarning("Warning", "Please enter a location.")

root = tk.Tk()
root.title("Weather Forecast")

label = tk.Label(root, text="Enter a city or zip code:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
