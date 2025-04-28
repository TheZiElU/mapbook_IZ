from cProfile import label
from tkinter import *

import tkintermapview

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
Ramka_mapa.grid(row=2, column=0)


#RAMKA LISTA OBIEKTÓW
label_lista_obiektow= Label(Ramka_lista_obiektów,text="Lista obiektów: ")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow=Listbox(Ramka_lista_obiektów)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly= Button(Ramka_lista_obiektów, text="Pokaż Szczegóły: ")
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt= Button(Ramka_lista_obiektów, text="Edytuj obiekt: ")
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt= Button(Ramka_lista_obiektów, text="Usuń obiekt: ")
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

Button_dodaj_obiekt= Button(Ramka_formularz,text="Dodaj")
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
# map_vidget= tkintermapview.TkinterMapView(Ramka_mapa, width=1024, height=400)
# map_vidget.set_position(52.23, 21)
# map_vidget.set_zoom(5)
# map_vidget.grid(row=0, column=0, columnspan=8)





root.mainloop()