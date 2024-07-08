import random
import string
from time import sleep
import requests
import subprocess


def menu():
    while True:
        print()
        print("1. Get my IP")
        print("2. Generate Password")
        print("3. Generate .exe build")
        print("Choose something by typing it's number")
        print()
        try:
            menu_choose = int(input())
        except ValueError:
            print("Please, enter a number.")
            continue
        
        if menu_choose == 1:
            getip()
        elif menu_choose == 2:
            pass_gen()
        elif menu_choose == 3:
            exe_build()
        else:
            print("Incorrect Number. Please, enter a valid number")

def getip():
    print()
    print("Welcome to GetIP function!")
    print()
    try:
        ip = requests.get('https://api.ipify.org').text
        print("Your IP is:", ip)
    except Exception as e:
        print(f"Error retrieving public IP: {e}")
    countdown_back_menu(5)

def pass_gen():
    letters = string.ascii_letters 
    numbers = string.digits  
    symbols = string.punctuation  

    print("Enter password length: ")
    try:
        pass_length = int(input())
    except ValueError:
        print("Error")
        return
    
    print("Do you want to use letters/numbers/symbols?")
    print("Enter your choice in this order. For example, if you want to use only numbers: 010")
    print()
    choice = input()
    
    if len(choice) != 3 or not all(c in '01' for c in choice):
        print("Incorrect choice, try again.")
        return
    
    all_chars = ""
    if choice[0] == '1':
        all_chars += letters
    if choice[1] == '1':
        all_chars += numbers
    if choice[2] == '1':
        all_chars += symbols

    if all_chars:
        random_pass = ''.join(random.choice(all_chars) for _ in range(pass_length))
        print("Your random password:", random_pass)
    else:
        print("No character sets selected, try again.")
    
    back_menu_choose()


def exe_build():
    print("This function will create a .exe build that can be routed in this program")
    
    script = "notify_launch.py"
    
    subprocess.run(['pyinstaller', '--onefile', script], check=True)
    
    print(f".exe build created for {script}")




def countdown_back_menu(t):
    while t >= 0:
        print(f"\rBack to the menu in: {t}", end="")
        sleep(1)
        t -= 1
    print()
    menu()

def back_menu_choose():
    print()
    print("Print 99 to back into menu")
    print()
    try:
        back_menu = int(input())
    except Exception as e:
        print("Error")
        back_menu_choose()
    if back_menu == 99:
        menu()
    else:
        print("Incorrect Number. Please, provide correct number.")
        back_menu_choose()

if __name__ == "__main__":
    menu()
