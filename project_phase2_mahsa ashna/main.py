from login import User
import os
import pandas as pd
import hashlib
print("please enter one item  \n1_login\n2_signup :")
selection_item = int(input("your selection "))
if selection_item == 1:
    os.system('clear')
    l = pd.read_csv("account.csv")
    username = input("enter username")
    password = input("enter password")
    hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
    if(list(l['username']).index(username) == list(l['password']).index(hash_password)):
        kinds = list(l['kind'])
        index = list(l['username']).index(username)
        kind = kinds[index]
        usr = User(username,hash_password,kind)
        usr.showEvents()
        if(usr.kind == 'admin'):
            choice = int(input("1.if you want to buy events \n2.if you want to add events"))
            if(choice == 1):
                usr.buy()
            elif(choice == 2):
                usr.addEvent()
            else:
                print("INVALID CHOICE")
        else:
            choice = int(input("1.if your want to buy events"))
            if(choice == 1):
                usr.buy()
            else:
                print("INVALID CHOICE")
elif selection_item == 2:
    User.register()
else:
    print("invalid")
