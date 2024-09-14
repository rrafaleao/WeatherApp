from tkinter import *
import datetime as dt
import requests

class Time:
    def __init__(self):
        pass

class Weather:
    def __init__(self):
        pass

class Interface:
    def __init__(self, root):
        self.root = root
        self.city = Weather()
        self.search_frame = Frame(root)
        self.search_frame.pack()
        self.search_frame.configure(bg="#306BA9")

        weather_label = Label(self.search_frame, bg="#306BA9", text="Weather App", font=("Gulim",30), width=11,height=2)
        weather_label.pack(pady=30)

        def temp_text(e):
            self.Search_city.delete(0,"end")

        self.Search_city = Entry(self.search_frame, bg="white", width=50, borderwidth=2,font="Arial")
        self.Search_city.insert(0, "Search for a city: ")
        self.Search_city.pack(pady=10)
        self.Search_city.bind("<FocusIn>", temp_text)
        Search_Button = Button(self.search_frame, text="Search", borderwidth=2, width=10,font="Arial", command= self.main_frame)
        Search_Button.pack()

    def main_frame(self):
        self.search_frame.pack_forget()
        main_frame = Frame(root)
        main_frame.pack()
        city = self.Search_city.get()
            
        Base_url = "http://api.openweathermap.org/data/2.5/weather?"
        Api_key = "afdd6ba7ada0a6d4ec2e85cae94e1bea"
        url = Base_url + "appid=" + Api_key + "&q=" + city
        response = requests.get(url).json()
        print(response)

root = Tk()
App = Interface(root)
root.geometry("800x600")
root.configure(bg="#306BA9")
root.title("Weather App")
root.mainloop()