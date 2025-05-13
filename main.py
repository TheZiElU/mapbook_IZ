from binascii import a2b_qp
from cProfile import label
from tkinter import *

import tkintermapview

users:list = []

class User:
    def __init__(self, name, surname, location, posts):
        self.name =  name
        self.surname = surname
        self.location = location
        self.posts = posts
        self.coordinates= self.get_coordinates()

    def get_coordinates(self,) -> list:
        import requests
        from bs4 import BeautifulSoup
        address_url: str = f"https://pl.wikipedia.org/wiki/{self.location}"
        response = requests.get(address_url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude: float = float(response_html.select(".longitude")[1].text.replace(",", "."))
        #    print(longitude)
        latitude: float = float(response_html.select(".latitude")[1].text.replace(",", "."))
        #    print(latitude)
        return [latitude, longitude]



def add_users():
    imie = entry_name.get()
    nazwisko = entry_surname.get()
    posty= entry_posts.get()
    miejscowosc = entry_location.get()
    tmp_user = (User(name= imie , surname= nazwisko, location= miejscowosc, posts=posty))
    users.append(tmp_user)
    map_widget.set_marker(tmp_user.coordinates[0],tmp_user.coordinates[1], text=tmp_user.location)
    print(users)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_posts.delete(0, END)
    entry_location.delete(0, END)
    entry_name.focus()
    show_users()

def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f"{idx+1}. {user.name} {user.surname} {user.location} {user.posts} ")

def delete_user():
    idx=listbox_lista_obiektow.index(ACTIVE)
    users.pop(idx)
    show_users()

def user_details():
    idx=listbox_lista_obiektow.index(ACTIVE)
    label_name_szczegoły_obiektu_wartosc.configure(text=users[idx].name)
    label_surname_szczegoły_obiektow.configure(text=users[idx].surname)
    label_location_szczegoły_obiektu.configure(text=users[idx].location)
    label_posts_szczegoły_obiektow.configure(text=users[idx].posts)

def edit_user():
    idx=listbox_lista_obiektow.index(ACTIVE)
    entry_name.insert(0, users[idx].name)
    entry_surname.insert(0, users[idx].surname)
    entry_location.insert(0, users[idx].location)
    entry_posts.insert(0, users[idx].posts)

    Button_dodaj_obiekt.configure(text="Zapisz", command=lambda:update_users(idx))

def update_users(idx):
    name=entry_name.get()
    surname=entry_surname.get()
    location=entry_location.get()
    posts=entry_posts.get()


    users[idx].name=name
    users[idx].surname=surname
    users[idx].location=location
    users[idx].posts=posts

    Button_dodaj_obiekt.configure(text="Dodaj", command=add_users)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_posts.delete(0, END)
    entry_location.delete(0, END)
    show_users()




root = Tk()
root.title("MapBook_IZ")
root.geometry("1024x768")

# RAMKI
Ramka_lista_obiektów=Frame(root)
Ramka_formularz=Frame(root)
Ramka_szczeguly_obiektow=Frame(root)
Ramka_mapa=Frame(root)


Ramka_lista_obiektów.grid(row=0, column=0)
Ramka_formularz.grid(row=0, column=1)
Ramka_szczeguly_obiektow.grid(row=1, column=0)
Ramka_mapa.grid(row=2, column=0, columnspan=2)


#RAMKA LISTA OBIEKTÓW
label_lista_obiektow= Label(Ramka_lista_obiektów,text="Lista obiektów: ")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow=Listbox(Ramka_lista_obiektów)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly= Button(Ramka_lista_obiektów, text="Pokaż Szczegóły: ", command=user_details)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt= Button(Ramka_lista_obiektów, text="Edytuj obiekt: ", command=edit_user)
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt= Button(Ramka_lista_obiektów, text="Usuń obiekt: ", command=delete_user)
button_usun_obiekt.grid(row=2, column=2)



#RAMKA FORMULARZ
label_formularz= Label(Ramka_formularz,text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name= Label(Ramka_formularz,text="Imię: ")
label_name.grid(row=1, column=0, sticky=W)
label_surname= Label(Ramka_formularz,text="Nazwisko: ")
label_surname.grid(row=2, column=0,sticky=W)
label_posts= Label(Ramka_formularz,text="Liczba postów: ")
label_posts.grid(row=3, column=0, sticky=W)
label_location= Label(Ramka_formularz,text="Miejscowość: ")
label_location.grid(row=4, column=0, sticky=W)



entry_name= Entry(Ramka_formularz)
entry_name.grid(row=1, column=1)
entry_surname= Entry(Ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_posts= Entry(Ramka_formularz)
entry_posts.grid(row=3, column=1)
entry_location= Entry(Ramka_formularz)
entry_location.grid(row=4, column=1)

Button_dodaj_obiekt= Button(Ramka_formularz,text="Dodaj" ,command=add_users)
Button_dodaj_obiekt.grid(row=5, column=1,columnspan=2)


#RAMKA SZCZEGÓŁY OBIEKTÓW
label_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Szczegóły użytkownika: ")
label_szczegoły_obiektu.grid(row=0, column=0)

label_name_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Imię: ")
label_name_szczegoły_obiektu.grid(row=1, column=0)

label_name_szczegoły_obiektu_wartosc= Label(Ramka_szczeguly_obiektow, text="....")
label_name_szczegoły_obiektu_wartosc.grid(row=1, column=1)

label_surname_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="Nazwisko: ")
label_surname_szczegoły_obiektow.grid(row=1, column=2)

label_surname_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="....")
label_surname_szczegoły_obiektow.grid(row=1, column=3)

label_posts_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text=" Liczba postów: ")
label_posts_szczegoły_obiektow.grid(row=1, column=4)

label_posts_szczegoły_obiektow= Label(Ramka_szczeguly_obiektow, text="....")
label_posts_szczegoły_obiektow.grid(row=1, column=5)

label_location_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="Miejscowość: ")
label_location_szczegoły_obiektu.grid(row=1, column=6)

label_location_szczegoły_obiektu= Label(Ramka_szczeguly_obiektow, text="....")
label_location_szczegoły_obiektu.grid(row=1, column=7)


# #RAMKA MAPA
map_widget= tkintermapview.TkinterMapView(Ramka_mapa, width=1024, height=400)
map_widget.set_position(52.23, 21)
map_widget.set_zoom(5)
map_widget.grid(row=0, column=0, columnspan=8)





root.mainloop()