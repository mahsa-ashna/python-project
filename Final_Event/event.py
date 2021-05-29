import sys
import pandas as pd
from colorama import Fore
import logging
import csv

class Admin:
    #this class admin can define event and bye event
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def loginPage(self):
        Event.showEvents()
        print(Fore.MAGENTA + "1.to buy event\n2.to add event\n3_exit")
        choice = int(input("select one item:"))
        if choice == 1:
            self.buyEvent()
        elif choice == 2:
            self.addEvent()
        elif choice == 3:
            sys.exit()
        else:
            print(Fore.LIGHTRED_EX + "No such choice")
            self.loginPage()
    def buyEvent(self):
        events = pd.read_csv('events.csv').values[:,1:]
        choice = int(input("pls enter number of event you want to buy:"))
        count = int(input("pls enter how many tickets you want to buy:"))
        if choice > len(list(events[:,0])):
            print("no such event")
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
        index = len(list(pd.read_csv('events.csv').values[: ,0]))
        title = input(Fore.YELLOW + "title: ")
        date = input(Fore.YELLOW + "date: ")
        time = input(Fore.YELLOW + "time: ")
        location = input(Fore.YELLOW + "location: ")
        capacity = input(Fore.YELLOW + "capacity: ")
        price = input(Fore.YELLOW + "price: ")
        row_account = [[index,title,date,time,location,capacity,capacity,price]]
        file_path = 'events.csv'
        with open(file_path, 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            # writing the data row
            csv_writer.writerows(row_account)
            #log
        logging.info("event " + title + " has been added")
        print(Fore.GREEN + "your event successfully added")
        self.loginPage()

class Customer:
    def __init__(self, username, password, role):
        """
        :param username:name of customer
        :param password: password of customer
        :param role: role of customer
        """
        self.username = username
        self.password = password
        self.role = role

    def loginPage(self):
        Event.showEvents()
        print("1.to buy event")
        choice = int(input())
        if choice == 1:
            self.buyEvent()
        else:
            print("No such choice")
            self.loginPage()

    def buyEvent(self):
        events = pd.read_csv('events.csv').values[:,1:]
        choice = int(input("pls enter number of event you want to buy:"))
        count = int(input("pls enter how many tickets you want to buy:"))
        if choice >= len(list(events[:,0])):
            print("no such event")
            self.loginPage()
        elif events[choice][5] < count:
            print(Fore.LIGHTRED_EX + "no room")
            self.loginPage()
        else:
            events[choice][6] -= count
            print("_________________")
            Ticket(events[choice][0],count, events[choice][6]).showTicket(self.role)
            print("_________________")
            self.loginPage()
            logging.info(self.username + " has been bought " + str(count) + " of " + events[choice][0])





class Event:
    def __init__(self,title, date, time, location, capacity, remaining_capacity,price):
        """
        :param title: title of event
        :param date: date of event
        :param time: time of event
        :param location: location of event
        :param capacity: capacity of event
        :param remaining_capacity: remaining capacity of event
        :param price: price of event
        """
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.capacity = capacity
        self.remaining_capacity = remaining_capacity
        self.price = price
    @staticmethod
    def showEvents():
        #this method we can see events
        l = pd.read_csv('events.csv').values
        lastIndex = len(l[:,0])
        for i in range(lastIndex):
            print("index: " + str(i) + "\ntitle: " + str(l[i,1]) + "\ndate: " + str(l[i,2]) + "\ntime: " + str(l[i,3]) + "\nlocation: " + str(l[i,4]) + "\ncapacity: " + str(l[i,5]) + "\nremaining_capacity: " + str(l[i,6]) + "\nprice: " + str(l[i,7]))
            print("______________________________________________________________________________")
            


class Ticket:
    #this class we can see ticket
    def __init__(self, title,count,price):
        """
        :param title: title of event
        :param count: number of event
        :param price: price of event
        """
        self.price = price
        self.title = title
        self.count = count
    def showTicket(self,role):
        #this method we can see ticket purchased
        print("you bought "+ str(self.count) + " of " + str(self.title) + " with price " + str(self.price* self.count * (1 - Creat_discount.getDiscounts()[role])))



class Creat_discount:
    #this class we write percent of discount
    @staticmethod
    def getDiscounts():
        return {
            'student': 0.1,
            'normal': 0.2,
            'admin': 0.3,
            "employee": 0.4,
        }