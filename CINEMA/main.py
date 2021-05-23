from login import User
import logging
from colorama import Fore


logging.basicConfig(filename='example.log', level=logging.DEBUG)

while True:
    print(Fore.BLUE + "*-*-*-*-*-*-*-*-*-* WELCOME  *-*-*-*-*-*-*-*-*-*")
    print(Fore.CYAN + "please enter one item  \n1_login \n2_signup ")
    selection_item = int(input("your selection : "))
    if selection_item == 1:
        User.login()
    elif selection_item == 2:
        User.register()
    else:
        print(Fore.LIGHTRED_EX + "invalid choice")
