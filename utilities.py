from time import sleep
import requests

print("Welcome, here's some utilities")
print()

def menu():
 print()
 print("1. Get my IP")
 print()
 print("Choose something by typing it's number")
 print()
 menu_choose = int(input())
 if menu_choose == (1):
    getip()
 else:
    print()
    print("Incorrect Number. Please, Enter valid number")
    menu()


def getip():
   print()
   print("Welcome to GetIP function!")
   print()
   try:
        ip = requests.get('https://api.ipify.org').text
        print("Your's IP is:", ip)
        print()
        countdown_back_menu(5) #seconds to leave into menu
        menu()
   except Exception as e:
        print(f"Error retrieving public IP: {e}")
        return None


def countdown_back_menu(t):
    while t >= 0:
        print(f"\rBack to the menu in: {t}", end="")
        sleep(1)
        t -= 1
    print()


def back_menu_choose():
    print()
    print("Print 99 to back into menu")
    print()
    back_menu = int(input())
    if back_menu == 99:
        menu()
    else:
        print("Incorrect Number. Please, provide correct number.")
        back_menu_choose()

if __name__ == "__main__":
    menu()

