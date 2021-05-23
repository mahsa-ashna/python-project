from pandas import read_csv, DataFrame
from hashlib import sha256
from csv import writer
import event
from colorama import Fore
import logging

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    @staticmethod
    def login():
        username = input("enter username :")
        password = input("enter password :")
        df_account = read_csv('account.csv').values[:, 1:]
        try:
            l = list(df_account[:,0]).index(username)
        except:
            print(Fore.MAGENTA + "no such username")
            return
        hash_password = sha256(password.encode("utf8")).hexdigest()
        if df_account[l,3] == 3:

            print(Fore.LIGHTRED_EX + "you have been locked")
            return
        elif df_account[l,1] == hash_password:
            logging.info(username + " has been entered")
            df_account[l,3] = 0
            a = DataFrame (data =df_account, columns=['index', 'username', 'password', 'role', 'tries'])
            a.to_csv('account.csv')
            if df_account[l,2] == 'admin':
                event.Admin(username, hash_password).loginPage()
                logging.info("admin " + username + "entered")
            else:
                event.Customer(username, password, df_account[l, 2]).loginPage()
                logging.info(df_account[l,2] + " " + username + "entered")
        else:
            print(Fore.LIGHTRED_EX + 'wrong password')
            df_account[l,3] += 1
            if df_account[l,3] == 3:
                logging.info(username + "has been locked")
            a = DataFrame(data=df_account, columns=['index', 'username', 'password', 'role', 'tries'])
            a.to_csv('account.csv')
            return



    @staticmethod
    def register():
        file_path = "account.csv"
        df_account = read_csv(file_path)
        lst_username = list(df_account.values[:,1])
        index = len(lst_username)
        roles = ["normal", "student", "employee", "admin"]
        username = input(Fore.LIGHTGREEN_EX + "enter your username:")
        if username in lst_username:
            print(Fore.LIGHTRED_EX + "invalid username")
            return

        password = input(Fore.LIGHTGREEN_EX + "enter your password:")
        hash_password = sha256(password.encode("utf8")).hexdigest()

        for v in roles:
            print(str(roles.index(v)) + "." + v)
        v = int(input(Fore.YELLOW + "please enter your role number: "))
        if v < 0 or v > 3:
            print(Fore.LIGHTRED_EX + "no such role")
        else:
            print(Fore.LIGHTYELLOW_EX + "you are added successfully please login")
            return


        row_account = [[index, username, hash_password,roles[v],0]]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)
            #log
        logging.info(username + ' has been registered as a ' + roles[v])
        return


