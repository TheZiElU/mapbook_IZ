import folium
import requests
from bs4 import BeautifulSoup



def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował(a) {user["posts"]} postów.")


def add_user (users_data: list)->None:
    new_name=input("Podaj imię: ")
    new_location=input("Podaj miejsce: ")
    new_posts=input("Podaj liczbę postów: ")
    users_data.append(   {"name": new_name, "location": new_location, "posts": new_posts})


def remove_user(users_data:list[dict]) -> None:
    users_name=input("Podaj imię znajomego do usunięcia: ")
    for user in users_data:
        if user["name"] == users_name:
            users_data.remove(user)

def update_user(users_data:list[dict]) -> None:
    users_name=input("Podaj imię znajomego do aktualizacji: ")
    for user in users_data:
        if user["name"] == users_name:
            user["name"]=input("Podaj nowe imię znajomego: ")
            user["location"]=input("Podaj nową miejscowość: ")
            user["posts"]=int(input("Podaj nową liczbę postów: "))




def get_coordinates(city_name:str)->list:
    address_url:str=f"https://pl.wikipedia.org/wiki/{city_name}"
    response = requests.get(address_url).text
    response_html=BeautifulSoup(response,"html.parser")
    longitude:float=float(response_html.select(".longitude")[1].text.replace("," , "."))
#    print(longitude)
    latitude:float=float(response_html.select(".latitude")[1].text.replace("," , "."))
#    print(latitude)
    return [latitude,longitude]

#for user in users:
#   get_coordinates(city_name=user["location"])
def get_map (users_data:list)->None:
    mapa= folium.Map([52.3, 21.00], zoom_start=6)
    for user in users_data:
        folium.Marker(
            location=get_coordinates(city_name= user["location"]),
            popup=f'{user["name"]}<br/>{user["location"]}<br/>{user["posts"]}<br/>'
                  f'<img src="{user["picture"]}" alt="{user["picture"]}"/>',

        ).add_to(mapa)

    mapa.save("mapa.html")