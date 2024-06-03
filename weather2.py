import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        if not location:
            raise ValueError("Invalid city name")

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=b0dbc41cee351d5fafcef62ba93ae169"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=f"{temp}°C")
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry or API Error!")

# search box
Search_image = tk.PhotoImage(file="C:/Users/kumar/Downloads/it's 2024/search.png")
myimage = tk.Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = tk.PhotoImage(file="C:/Users/kumar/Downloads/it's 2024/search_icon.png")
myimage_icon = tk.Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# logo
Logo_image = tk.PhotoImage(file="C:/Users/kumar/Downloads/it's 2024/logo.png")
logo = tk.Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = tk.PhotoImage(file="C:/Users/kumar/Downloads/it's 2024/box.png")
frame_myimage = tk.Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=tk.BOTTOM)

# time
name = tk.Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = tk.Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# label
label1 = tk.Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1AB5EF")
label1.place(x=120, y=400)

label2 = tk.Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1AB5EF")
label2.place(x=250, y=400)

label3 = tk.Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1AB5EF")
label3.place(x=430, y=400)

label4 = tk.Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1AB5EF")
label4.place(x=650, y=400)

t = tk.Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = tk.Label(font=("arial", 15, 'bold'))
c.place(x=400, y=250)

w = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
w.place(x=120, y=430)
h = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
h.place(x=280, y=430)
d = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
d.place(x=450, y=430)
p = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1AB5EF")
p.place(x=670, y=430)

root.mainloop()
