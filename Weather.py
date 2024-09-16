from tkinter import *
import requests

class Interface:
    def __init__(self, root):
        self.root = root
        self.search_frame = Frame(root)
        self.search_frame.pack()
        self.search_frame.configure(bg="#306BA9")

        self.logo = PhotoImage(file='images\\logo.png')
        root.iconphoto(True, self.logo)

        weather_label = Label(self.search_frame, bg="#306BA9", text="Weather App", font=("Gulim",30), width=11,height=2)
        weather_label.pack(pady=30)

        def temp_text(e):
            self.Search_city.delete(0,"end")

        self.Search_city = Entry(self.search_frame, bg="white", width=50, borderwidth=2,font="Arial")
        self.Search_city.insert(0, "Enter city: ")
        self.Search_city.pack(pady=10)
        self.Search_city.bind("<FocusIn>", temp_text)
        Search_Button = Button(self.search_frame, text="Search", borderwidth=2, width=10,font="Arial", command= self.main_frame)
        Search_Button.pack()

        

    def main_frame(self):
        self.search_frame.pack_forget()
        self.main_frame = Frame(root)
        self.main_frame.pack()
        city = self.Search_city.get()
        self.main_frame.configure(bg="#306BA9")

        Base_url = "http://api.openweathermap.org/data/2.5/weather?"
        Api_key = "afdd6ba7ada0a6d4ec2e85cae94e1bea"
        url = Base_url + "appid=" + Api_key + "&q=" + city
        response = requests.get(url).json()

        if response['cod'] == '404':
            self.city_not_found()
            return

        unity = "metric" 
        language = "en"
        url_forecast = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={Api_key}&units={unity}&lang={language}"
        response_forecast = requests.get(url_forecast)
        forecast_response = response_forecast.json()

        def kelvin_to_Celsius(kelvin):
            celsius = kelvin - 273
            return celsius
        
        city_name = response['name']
        country = response['sys']['country']
        temp_kelvin = response['main']['temp']
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius = kelvin_to_Celsius(feels_like_kelvin)
        celsius = kelvin_to_Celsius(temp_kelvin)
        description = response['weather'][0]['description']
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']
        weather = response['weather'][0]['main']
        previsoes_filtradas = []

        for forecast in forecast_response['list']:
            data_hora = forecast['dt_txt']
            hora = data_hora.split()[1]
            
            if hora == "12:00:00":
                previsoes_filtradas.append(forecast)

        day1 = previsoes_filtradas[0]
        day2 = previsoes_filtradas[1]
        day3 = previsoes_filtradas[2]
        day4 = previsoes_filtradas[3]
        day5 = previsoes_filtradas[4]
        date_day1, _ = day1['dt_txt'].split()
        date_day2, _ = day2['dt_txt'].split()
        date_day3, _ = day3['dt_txt'].split()
        date_day4, _ = day4['dt_txt'].split()
        date_day5, _ = day5['dt_txt'].split()

        temp_day1 = day1['main']['temp']
        temp_day2 = day2['main']['temp']
        temp_day3 = day3['main']['temp']
        temp_day4 = day4['main']['temp']
        temp_day5 = day5['main']['temp']

        desc_day1 = day1['weather'][0]['description']
        desc_day2 = day2['weather'][0]['description']
        desc_day3 = day3['weather'][0]['description']
        desc_day4 = day4['weather'][0]['description']
        desc_day5 = day5['weather'][0]['description']

        self.clear_sky = PhotoImage(file='images\\clear_sky.png')
        self.broken_clouds = PhotoImage(file='images\\broken_clouds.png')
        self.few_clouds = PhotoImage(file='images\\few_clouds.png')
        self.mist = PhotoImage(file='images\\mist.png')
        self.rain = PhotoImage(file='images\\rain.png')
        self.scattered_clouds = PhotoImage(file='images\\scattered_clouds.png')
        self.shower_rain = PhotoImage(file='images\\shower_rain.png')
        self.snow = PhotoImage(file='images\\snow.png')
        self.thunderstorm = PhotoImage(file='images\\thunderstorm.png')


        change_city_button = Button(self.main_frame, text="Change city", bg="#306BA9", fg="White", font=("Arial",10), command= self.change_city)
        change_city_button.pack(side= TOP, padx=200)
        
        City_label = Label(self.main_frame, text=(city_name + ", " + country), font=("Arial", 20), bg=("#306BA9"),fg="White")
        City_label.pack(pady=20)
        temp_label = Label(self.main_frame, text= "%.2fºC" % celsius, font=("Arial", 40), bg="#306BA9", fg="White") 
        temp_label.pack()
        if weather == 'Clear':
            clear_sky_label = Label(self.main_frame, image=self.clear_sky, width=50, height=50, bg="#306BA9")
            clear_sky_label.pack(pady=10)
        if weather == 'Clouds':
            clear_sky_label = Label(self.main_frame, image=self.few_clouds, width=50, height=50, bg="#306BA9")
            clear_sky_label.pack(pady=10)
        if weather == 'Mist':
            clear_sky_label = Label(self.main_frame, image=self.mist, width=50, height=50, bg="#306BA9")
            clear_sky_label.pack(pady=10)
        if weather == 'Rain':
            clear_sky_label = Label(self.main_frame, image=self.rain, width=50, height=50, bg="#306BA9")
            clear_sky_label.pack(pady=10)
        if weather == 'Drizzle':
            clear_sky_label = Label(self.main_frame, image=self.shower_rain, width=50, height=50, bg="#306BA9")
            clear_sky_label.pack(pady=10)
        if weather == 'Snow':
            clear_sky_label = Label(self.main_frame, image=self.snow, width=50, height=50, bg="#306BA9")
            clear_sky_label.pack(pady=10)
        if weather == 'Thunderstorm':
            clear_sky_label = Label(self.main_frame, image=self.thunderstorm, width=50, height=50, bg="#306BA9")
            clear_sky_label.pack(pady=10)


        feels_like_label = Label(self.main_frame, text="Feels like: %.2fºC" % feels_like_celsius, bg="#306BA9", fg="white", font=("Arial", 10))
        feels_like_label.pack()
        description_label = Label(self.main_frame, text="Description: " + description, bg="#306BA9", fg="white", font=("Arial", 10))
        description_label.pack()
        humidity_label = Label(self.main_frame, text="Humidity: %.2f%%" % humidity, bg="#306BA9", fg="white", font=("Arial", 10))
        humidity_label.pack()
        wind_speed_label = Label(self.main_frame, text="Wind Speed: %.2f m/s" % wind_speed, bg="#306BA9", fg="white", font=("Arial", 10))
        wind_speed_label.pack()

        forecast_label = Label(self.main_frame,text="5 Day Forecast", bg="#306BA9", fg="White", font=("Arial",20))
        forecast_label.pack(pady=20)

        day1 = Label(self.main_frame,text=f"{date_day1} | {temp_day1}ºC | {desc_day1}", font=("Arial", 10), bg="#306BA9",fg="white")
        day1.pack()
        day2 = Label(self.main_frame,text=f"{date_day2} | {temp_day2}ºC | {desc_day2}", font=("Arial", 10), bg="#306BA9",fg="white")
        day2.pack()
        day3 = Label(self.main_frame,text=f"{date_day3} | {temp_day3}ºC | {desc_day3}", font=("Arial", 10), bg="#306BA9",fg="white")
        day3.pack()
        day4 = Label(self.main_frame,text=f"{date_day4} | {temp_day4}ºC | {desc_day4}", font=("Arial", 10), bg="#306BA9",fg="white")
        day4.pack()
        day5 = Label(self.main_frame,text=f"{date_day5} | {temp_day5}ºC | {desc_day5}", font=("Arial", 10), bg="#306BA9",fg="white")
        day5.pack()

    def change_city(self):
        if hasattr(self, 'error_frame'):
            self.error_frame.pack_forget()
        if hasattr(self, 'main_frame'):
            self.main_frame.pack_forget()
        self.search_frame.pack()

    def city_not_found(self):
        self.main_frame.pack_forget()
        self.error_frame = Frame(root)
        self.error_frame.pack()
        self.error_frame.configure(bg="#306BA9")
        
        error_label = Label(self.error_frame, text="City not found!", font=("Arial", 20), bg="#306BA9", fg="white")
        error_label.pack(pady=20)
        
        try_again_button = Button(self.error_frame, text="Try again", bg="#306BA9", fg="white", font=("Arial", 15), command=self.change_city)
        try_again_button.pack(pady=20)

root = Tk()
App = Interface(root)
root.geometry("800x600")
root.configure(bg="#306BA9")
root.title("Weather App")
root.mainloop()