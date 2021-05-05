import pandas as pd
import hashlib
import csv


class User:
    def __init__(self, username, password,varity):
        self.username = username
        self.password = password
        self.kind = varity

    @staticmethod
    def register():
        file_path = "account.csv"
        df_account = pd.read_csv(file_path)
        lst_username = list(df_account["username"])
        varities = ["normal", "student", "employee", "admin"]
        username = input("enter your username:")
        if username in lst_username:
            print("invalid username")
            return

        password = input("enter your password:")
        hash_password = hashlib.sha256(password.encode("utf8")).hexdigest()

        for v in varities:
            print(str(varities.index(v)) + "." + v)
        v = int(input("please enter your varity number: "))
        if(v < 0 or v > 3):
            print("no such varity")
            return
        obj_user = User(username, hash_password,varities[v])

        row_account = [[obj_user.username, obj_user.password, varities[v]]]
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)

    def showEvents(self):
        #showing events based on is she admin or not
        pass
    def buy(self):
        #buying events
        pass
    def addEvent(self):
        #addingEvents
        pass

class Event:
    def __init__(self, date, location, capacity, cost):
        self.date = date
        self.location = location
        self.capacity = capacity
        self.cost = cost
        with open("event.csv" ,'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            csv_writer.writerows([date,location,capacity,cost])



