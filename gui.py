from tkinter import *
from get_data import get_weather_data

def update_weather():
    weather_update = get_weather_data()
    label_city.config(text=f"Город: {weather_update.city_name}")
    label_time.config(text=f"Время: {weather_update.current_time}")
    label_temp.config(text=f"Температура: {weather_update.temp_current}")
    label_details.config(text=weather_update.details)
    label_presure.config(text=f"Давление: {weather_update.presure}")
    label_wind.config(text=f"Ветер: {weather_update.wind}")
    label_humidity.config(text=f"Влажность: {weather_update.humidity}")

weather = get_weather_data()

screen = Tk()
screen.title("Weather")
screen.geometry('300x200')

# canvas = Canvas(bg="white", width=250, height=150)
# canvas.pack(anchor=CENTER, expand=1)

label_city = Label(screen, text=f"Город: {weather.city_name}")
label_city.grid(row=0, column=0)

label_time = Label(screen, text=f"Время: {weather.current_time}")
label_time.grid(row=1, column=0)

label_temp = Label(screen, text=f"Температура: {weather.temp_current}")
label_temp.grid(row=2, column=0)

label_details = Label(screen, text=weather.details)
label_details.grid(row=3, column=0)

label_presure = Label(screen, text=f"Давление: {weather.presure}")
label_presure.grid(row=4, column=0)

label_wind = Label(screen, text=f"Ветер: {weather.wind}")
label_wind.grid(row=5, column=0)

label_humidity = Label(screen, text=f"Влажность: {weather.humidity}")
label_humidity.grid(row=6, column=0)

update_weather()

screen.mainloop()