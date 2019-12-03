import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 800

def format_response(weather):
	try:
		name = weather["name"]
		desc = weather["weather"][0]["description"]
		temp = weather["main"]["temp"]

		final_str = "City: %s \nConditions: %s \nTemperature (°C): %s" % (name, desc, temp)
	except:
		final_str = "There was a problem retrieving that information"

	return final_str

# URL = https://api.openweathermap.org/data/2.5/weather
# weather key = a8960f074f9f3a0c7317ed7c8d5da73d

def get_weather(city):
	weather_key = "a8960f074f9f3a0c7317ed7c8d5da73d"
	url = "https://api.openweathermap.org/data/2.5/weather"
	params = {"APPID": weather_key, "q": city, "units": "Metric"}
	response = requests.get(url, params=params)
	weather = response.json()

	label["text"] = format_response(weather)

root = tk.Tk()

root.title("Daily Weather")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

BACKGROUND_IMAGE = tk.PhotoImage(file='Image/background.png')
BACKGROUND_LABEL = tk.Label(root, image=BACKGROUND_IMAGE)
BACKGROUND_LABEL.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Pristina", 20))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Search", font=20, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=("Pristina", 20), anchor="nw", justify="left", bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
