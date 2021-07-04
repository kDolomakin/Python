from tkinter import *
import http.client
import json
import tkinter as tk
# Створення вікна
root = Tk()
root.title("Covid Status Dolomakin K.")
root.geometry('500x800')
root['bg']='black'

n=20 # Кількість держав, котрі программа візьме з сайту, можна змінити і їх буде більше або меньше

conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
res = conn.getresponse()
data = res.read()
All_Info = data.decode("utf-8")
json = json.loads(All_Info)
# Фрейми, щоб було удобніше розподілити екран
frametop=Frame(root)
framebot=Frame(root)
frametop.pack()
framebot.pack()
# Функція оновлення, видаляє все, що є в полі Текст і заповнює новою інформацією, отриманою на даний момент
def Refresh():
    import json
    TextBox.delete(1.0,END)
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    All_Info = data.decode("utf-8")
    json = json.loads(All_Info)
    TextBox.insert('1.0', '\n')
    TextBox.insert('1.0', '=' * 30)
    for i in range(n):
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[14])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[12])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[10])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[3])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', list(json[i].items())[2])
        TextBox.insert('1.0', '\n')
        TextBox.insert('1.0', '=' * 30)
# Створення клавіші оновлення
Refreshbutton = Button(frametop, text="REFRESH",command=Refresh)
Refreshbutton['bg']='black'
Refreshbutton['fg']='red'
Refreshbutton.pack(side=LEFT)
# Пошук, Программа перевіряє, чи є така держава в json.
def Search():
    j=0
    for i in range(n):
        InputedCountry = EntryCountry.get()
        GetCountry = json[i].get('Country')
        if InputedCountry == GetCountry:
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalRecovered'))
                TextBox.insert('1.0', 'TotalRecovered : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalDeaths'))
                TextBox.insert('1.0', 'TotalDeaths : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('TotalCases'))
                TextBox.insert('1.0', 'TotalCases : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('Continent'))
                TextBox.insert('1.0', 'Continent : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', json[i].get('Country'))
                TextBox.insert('1.0', 'Country : ')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '*' * 30)
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '         We found!')
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '*' * 30)
                TextBox.insert('1.0', '\n')
                TextBox.insert('1.0', '=' * 30)
        else : j+=1
        if j==20:
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '          We didnt found')
            TextBox.insert('1.0', '\n')
            TextBox.insert('1.0', '*' * 30)
# Створення поля вводу
EntryCountry = Entry(frametop, width=50, borderwidth=5)
EntryCountry['bg']='black'
EntryCountry['fg']='red'
EntryCountry.pack(side=LEFT)
# Створення клавіші пошуку
Searchbutton = Button(frametop, text="SEARCH", command=Search)
Searchbutton.pack(side=LEFT)
Searchbutton['bg']='black'
Searchbutton['fg']='red'
# Створення поля тексу для інформації
TextBox = Text(framebot,width=500, height=500)
TextBox['bg']='black'
TextBox['fg']='red'
TextBox.pack()
# Перший виклик функції для заповнення при запуску
Refresh()
root.mainloop()
