import pandas as pd
from colorama import Fore
import logging
import csv

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def loginPage(self):
        Event.showEvents()
        print(Fore.CYAN + "1.to buy event\n2.to add event")
        choice = int(input())
        if choice == 1:
            self.buyEvent()
        elif choice == 2:
            self.addEvent()
        else:
            print(Fore.LIGHTRED_EX + "No such choice")
            self.loginPage()
    def buyEvent(self):
        events = pd.read_csv('events.csv').values[:,1:]
        choice = int(input(Fore.LIGHTBLUE_EX + "please enter number of event you want to buy : "))
        count = int(input(Fore.LIGHTBLUE_EX + "please enter how many tickets you want to buy : "))
        if choice > len(list(events[:,0])):
            print(Fore.LIGHTRED_EX + "no such event")
            self.loginPage()
        elif events[choice][5] < count:
            print(Fore.LIGHTRED_EX + "no room")
            self.loginPage()
        else:
            events[choice][5] -= count
            print("_________________")
            Ticket(events[choice][0],count, events[choice][6]).showTicket('admin')
            print("_________________")
            pd.DataFrame(data=events,columns=['index','title','date','time','location','capacity','remaining_capacity','price']).to_csv('events.csv')
            self.loginPage()

    def addEvent(self):
        index = len(list(pd.read_csv('events.csv').values[:, 0]))
        title = input(Fore.LIGHTYELLOW_EX + "title: ")
        date = input(Fore.LIGHTYELLOW_EX + "date: ")
        time = input(Fore.LIGHTYELLOW_EX + "time: ")
        location = input(Fore.LIGHTYELLOW_EX + "location: ")
        capacity = input(Fore.LIGHTYELLOW_EX + "capacity: ")
        price = input(Fore.LIGHTYELLOW_EX + "price: ")
        row_account = [[index, title, date, time, location, capacity, capacity, price]]
        file_path = 'events.csv'
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)
            #log
        logging.info(Fore.LIGHTMAGENTA_EX + "event " + title + " has been added")
        print(Fore.LIGHTMAGENTA_EX + "your event successfully added")
        self.loginPage()

class Customer:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def loginPage(self):
        Event.showEvents()
        print(Fore.CYAN + "1.to buy event")
        choice = int(input())
        if choice == 1:
            self.buyEvent()
        else:
            print(Fore.LIGHTRED_EX + "No such choice")
            self.loginPage()

    def buyEvent(self):
        events = pd.read_csv('events.csv').values[:,1:]
        choice = int(input(Fore.LIGHTBLUE_EX + "please enter number of event you want to buy : "))
        count = int(input(Fore.LIGHTBLUE_EX + "please enter how many tickets you want to buy : "))
        if choice >= len(list(events[:,0])):
            print(Fore.LIGHTRED_EX + "no such event")
            self.loginPage()
        elif events[choice][5] < count:
            print(Fore.LIGHTRED_EX + "no room")
            self.loginPage()
        else:
            events[choice][6] -= count
            print(Fore.LIGHTWHITE_EX + "_________________")
            Ticket(events[choice][0], count, events[choice][6]).showTicket(self.role)
            print(Fore.LIGHTWHITE_EX + "_________________")
            self.loginPage()
            logging.info(self.username + " has been bought " + str(count) + " of " + events[choice][0])





class Event:
    def __init__(self,title, date, time, location, capacity, remaining_capacity,price):
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.capacity = capacity
        self.remaining_capacity = remaining_capacity
        self.price = price
    @staticmethod
    def showEvents():
        l = pd.read_csv('events.csv').values
        lastIndex = len(l[:,0])
        for i in range(lastIndex):
            print("index: " + str(i) + "\ntitle: " + str(l[i,1]) + "\ndate: " + str(l[i,2]) + "\ntime: " + str(l[i,3]) + "\nlocation: " + str(l[i,4]) + "\ncapacity: " + str(l[i,5]) + "\nremaining_capacity: " + str(l[i,6]) + "\nprice: " + str(l[i,7]))
            print(Fore.LIGHTWHITE_EX + "______________________________________________________________________________")
            


class Ticket:
    def __init__(self, title,count,price):
        self.price = price
        self.title = title
        self.count = count
    def showTicket(self,role):
        print(Fore.LIGHTCYAN_EX + "you bought " + str(self.count) + "ticket of " + str(self.title) + " with price " + str(self.price * self.count * (1 - Creat_discount.getDiscounts()[role])))



class Creat_discount:
    @staticmethod
    def getDiscounts():
        return {
            'student': 0.1,
            'normal': 0,
            'admin': 0.4,
            "employee": 0.3
        }