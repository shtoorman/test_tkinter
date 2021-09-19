from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import requests
import json
import random

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")
root.geometry("570x40")


# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=55416&distance=5&API_KEY=567F67E9-4295-4115-9BF2-5E7D27A0E2B9


try:
    #random_zipcode = random.randint(29001, 29945)
    random_zipcode = 92322

    print(random_zipcode)
    api_requests = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(random_zipcode) + "&distance=1&API_KEY=567F67E9-4295-4115-9BF2-5E7D27A0E2B9")
    api = json.loads(api_requests.content)
    city = api[0]["ReportingArea"]
    quality = api[0]["AQI"]
    category = api[0]["Category"]["Name"]

    if category == "Good":
        weather_color = "#0C0"
    elif category == "Moderate":
        weather_color = "#FFFF00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "FF9900"
    elif category == "Unhealthy":
        weather_color = "FF0000"
    elif category == "Very Unhealthy":
        weather_color = "990066"
    elif category == "Hazardous":
        weather_color = "660000"

    root.configure(background=weather_color)


except Exception as e:
    api = "Error..."

myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("helvetica", 20),
                background=weather_color)
myLabel.pack()

root.mainloop()
