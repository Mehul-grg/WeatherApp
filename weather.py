import tkinter as tk
from tkinter.constants import ANCHOR
import requests
import time
# from PIL import ImageTk,background="salmon" 


def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        city + "&appid=8ea28302c987f4c5df5862cd08901c75"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    visibility = json_data['visibility']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(
        json_data['sys']['sunrise']+19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(
        json_data['sys']['sunset']+19800))
    feel_like=int(json_data['main']['feels_like']-273.15)

    final_info = condition+"\n"+str(temp)+"°C"
    feel="Feels like"+str(feel_like)+"°C"
    final_data = "\n" + "Max Temp: " + str(max_temp)+" °C"+"\n"+"Min Temp: "+str(min_temp)+" °C"+"\n" + "Pressure: " + str(
        pressure)+"\n"+"Humidity: "+str(humidity)+"%"+"\n"+"Wind Speed: " + str(wind)+" km/h"+"\n"+"Sunrise: " + str(sunrise)+" A.M"+"\n" + "Sunset: "+str(sunset)+" P.M"+"\n" + "Visibility: "+str(visibility/1000)+" km"
    label1.config(text=final_info)
    label3.config(text=feel)
    label2.config(text=final_data)


canvas = tk.Tk()
# canvas=tk.Canvas(canvas,bg='salmon', height=600, width=500)
canvas.geometry("600x500")
canvas.title("Weather App")
canvas.configure(bg="aliceblue")
# image=ImageTk.PhotoImage(file="C:\\Users\\mehul\\Documents\\Python\\Wallpaper.jpg")
# canvas.create_image(10,10,image=image,ANCHOR=NW)
# myimg = PhotoImage(file='Wallpaper.jpg')
# canvas.create_image(10, 10, image=myimg, anchor='nw')

f = ("Times New Roman", 15, "bold")
t = ("Comic Sans MS", 35, "bold")


textfield = tk.Entry(canvas,bg="honeydew", font=t)
textfield.pack(pady=20)
button=tk.Button(canvas,text='clear', width=25, command=canvas.destroy)
button.pack()
# button.grid(column=1,row=0)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas,justify="center" ,bg='aliceblue',font=t)
label1.pack()
label3=tk.Label(canvas, justify="center",background="aliceblue" ,font=f)
label3.pack()
label2 = tk.Label(canvas, bg="aliceblue",font=f)
label2.pack()


canvas.mainloop()
