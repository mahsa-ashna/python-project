import sys
from login import User
from event import *
import os
from colorama import Fore
import logging


logging.basicConfig(filename='example.log', level=logging.DEBUG)
#interest only when diagnosing problems

while True:
    print(Fore.BLUE + "*-*-*-*-*-*-*-*-WELCOME-*-*-*-*-*-*-*-*")
    print(Fore.CYAN + "please enter one item  \n1_login \n2_signup \n3_exit ")
    selection_item = int(input("your selection :  "))
    if selection_item == 1:
        User.login()
    elif selection_item == 2:
        User.register()
    elif selection_item == 3:
        print(Fore.LIGHTMAGENTA_EX + "***thanks for shopping***")
        sys.exit()
    else:
        print(Fore.LIGHTRED_EX + "invalid choice")
