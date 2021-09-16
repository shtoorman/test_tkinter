from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import requests
import json

root = Tk()
root.title("learn To Code")
root.iconbitmap("icone.ico")
root.geometry("530x40")
root.configure(background="green")

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=55416&distance=5&API_KEY=567F67E9-4295-4115-9BF2-5E7D27A0E2B9


try:
    api_requests = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=55416&distance=5&API_KEY=567F67E9-4295-4115-9BF2-5E7D27A0E2B9")
    api = json.loads(api_requests.content)
    city = api[0]["ReportingArea"]
    quality = api[0]["AQI"]
    category = api[0]["Category"]["Name"]
except Exception as e:
    api = "Error..."

myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("helvetica", 20),
                background="green")
myLabel.pack()

root.mainloop()
