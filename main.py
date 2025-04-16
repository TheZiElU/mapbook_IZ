from utils.model import users
from utils.controller import get_user_info, add_user, remove_user, update_user, get_map, get_coordinates


def main():
    print(f"Witaj {users[0]["name"]}")

    while True:
        print("=====================Menu====================")
        print("0 - Zakończ pracę programu")
        print("1 - Pokaż co u moich znajomych ")
        print("2 - Dodaj znajomego")
        print("3 - Usuń znajomego")
        print("4 - Aktualizuj dane znajomego")
        print("5 - Wygeneruj mapę dla znajomych")
        print("==============================================")
        choice:str=input("Wybierz opcje Menu: ")
        if choice == "0": break
        if choice == "1": get_user_info(users[1:])
        if choice == "2": add_user(users)
        if choice == "3": remove_user(users)
        if choice == "4": update_user(users)
        if choice == "5": get_map(users)

if __name__ == "__main__":
    main()