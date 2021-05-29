import pandas as pd
import hashlib
import csv
from event import *
import loggin
from colorama import Fore
#from time import sleep

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    @staticmethod
    def login():
        username= input("enter username")
        password = input("enter password")
        df_account = pd.read_csv('account.csv').values[:,1:]
        try:
            l = list(df_account[:,0]).index(username)
        except:
            print("no such username ")
            return
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()
        if df_account[l,3] == 3:

            print("you have been locked")
            return
        elif df_account[l,1] == hash_password:
            logging.info(username + " has been entered")
            df_account[l,3] = 0
            a = pd.DataFrame(data =df_account, columns=['index','username', 'password', 'role', 'tries'])
            a.to_csv('account.csv')
            if df_account[l,2] == 'admin' :
                Admin(username,hash_password).loginPage()
                logging.info("admin " + username + "entered")
            else:
                Customer(username,password,df_account[l,2]).loginPage()
                logging.info(df_account[l,2] + " " + username + "entered")
        else:
            print('wrong password')
            df_account[l,3] += 1
            if df_account[l,3] == 3 :
                logging.info(username + "has been locked")
            a = pd.DataFrame(data=df_account, columns=['index','username', 'password', 'role', 'tries'])
            a.to_csv('account.csv')
            return



    @staticmethod
    def register():
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account.values[:,1])
        index = len(lst_username)
        roles = ["normal", "student", "employee", "admin"]
        username = input("enter your username:")
        if username in lst_username:
            print("invalid username")
            return

        password = input("enter your password:")
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()

        for v in roles:
            print(str(roles.index(v)) + "." + v)
        v = int(input("please enter your role number: "))
        if v < 0 or v > 3:
            print(Fore.LIGHTRED_EX + "no such role")
        else:
            print(Fore.LIGHTYELLOW_EX + "do you have a dis count cod ? \n 1_yes \n 2_no ")
            select_discount = int(input("select :"))
            if select_discount == 1:
                dis_count = int(input(Fore.GREEN + "please enter your dis count code : "))
                if dis_count == 555:
                    print(Fore.LIGHTBLUE_EX + "wow you have a 10% dis count \n you are added successfully please login")
                elif dis_count == 777:
                    print(Fore.LIGHTBLUE_EX + "wow you have a 30% dis count \n you are added successfully please login")
                elif dis_count == 222:
                    print(Fore.LIGHTBLUE_EX + "wow you have a 40% dis count \n you are added successfully please login")

                else:
                    print(Fore.LIGHTRED_EX + "wrong code")


            elif select_discount == 2:
                print(Fore.CYAN + "ok no matter \n you are added successfully please login")
                return


        row_account = [[index, username, hash_password,roles[v],0]]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)
            #log
        logging.info(username + ' has been registered as a ' + roles[v])
        return


