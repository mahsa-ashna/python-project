type_of_person = ['admin', 'student', 'Employee', 'user']


class Discount:
    def __init__(self, type_discount, percent):
        self.type_discount = type_discount
        self.percent = percent

        return
    
    ##############
    def get_percent(self):
        return str(self.percent)



class Person:
    def __init__(self, type_person, amountـmoney, discount_code):
        self.type_person = type_person
        self.amountـmoney = amountـmoney
        self.discount_code = discount_code

    ################## create person
    def create_person(self):
        print("""
        Enter the type of person from this list:
        ['admin', 'student', 'Employee', 'user']
        """)
        type_person = input()
        while True:
            if type_person.lower in type_person:
                self.type_person = type_person.lower
                break
            else:
                print('format is incorrect try again')
        
        while True:
            try:
                amountـmoney = int(input('Enter your amount of money'))
                break
            except:
                print('wrong format of input try again')
        self.amountـmoney = int(amountـmoney)
        self.discount_code = 0
        print('object successfully created !!')
    
    ################# Buy Ticket
    def buy_ticket(self, price):
        if self.amountـmoney < price:
            print("you don't have enough money")
        else:
            self.amountـmoney =- price
            print('nice BUY!!!! :)')

    ################# get type person
    def get_type(self):
        return self.type_person

    #################






#########################################
#########################################
class Event:
    def __init__(self, ID, date, time, location, total_capacity, re_capacity, price):
        self.ID = ID
        self.date = date
        self.time = time
        self.location = location
        self.total_capacity = total_capacity
        self.re_capacity = re_capacity
        self.price = price

        return


    ############################### create event
    def create_event(self, person_obj):
        if person_obj.get_type().lower == 'admin':
            day = 0
            month = 0
            year = 0
            hour = 0
            minute = 0
            capacity = 0
            ############# year
            while True:
                while True:
                    try:
                        year = int(input('Enter year of event'))
                        break
                    except:
                        print('wrong format of year')
                if year > 2000 and year< 2100:
                    break
                else:
                    print('year most be between 2000 to 2100')

            #########month
            while True:
                while True:
                    try:
                        month = int(input('Enter month of event'))
                        break
                    except:
                        print('wrong format of month')
                if month > 0 and month < 13:
                    break
                else:
                    print('month most be between 1 to 12')

            #########day
            while True:
                while True:
                    try:
                        day = int(input('Enter day of event'))
                        break
                    except:
                        print('wrong format of day')
                if day > 0 and day < 31:
                    break
                else:
                    print('day most be between 1 to 30')
        
            ########create date
            date = str(day) + ' ' + str(month) + ' ' + str(year)
            self.date = date


            ######### hour
            while True:
                while True:
                    try:
                        hour = int(input('Enter hour of event'))
                        break
                    except:
                        print('wrong format of hour')
                if hour > -1 and hour < 24:
                    break
                else:
                    print('hour most be between 0 to 24')
        
            ######## minute
            while True:
                while True:
                    try:
                        minute = int(input('Enter minute of event'))
                        break
                    except:
                        print('wrong format of minute')
                if minute > -1 and minute < 60:
                    break
                else:
                    print('hour most be between 0 to 59')
        
            ########create Time
            time = str(hour) + ' ' +str(minute)
            self.time = time


            ##########create location
            location = input('Enter the name of street of event')
            self.location = location


            ########## craete capacity
            while True:
                try:
                    capacity = int(input('Enter capacity of event'))
                    break
                except:
                    print('wrong format of capacity')
            self.capacity = capacity
            self.re_capacity = capacity


            ########## create price
            while True:
                try:
                    price = int(input('Enter price of event'))
                    break
                except:
                    print('wrong format of price')
            self.price = price


            print('object suusecfully created !!')
            return
        
        else:
            print('you dont hava permision to create Event')
    

    ################################ calculate discount
    def cal_discount(self, percent):
        return self.price - ((self.price * percent) / 100)


    ################################# buy Ticket
    def buy_ticket(self, person_obj):
        flag_discount = 0
        print('Do you have discount_code? \n(1)yes (2)no')
        while True:
            try:
                flag_discount = int(input())
                break
            except:
                print('try gain wrong format')
            
        if flag_discount == 1:
            if person_obj.discount_code.get_percent == 0:
                print('you dont have discount code')
                print(f'final price after discount is {self.price}')
                person_obj.buy_ticket(self.price)
            
            else:
                print('discount code successfully added!!')
                print(f'final price after discount is {self.cal_discount(person_obj.discount_code.get_percent)}')
                person_obj.buy_ticket(self.cal_discount(person_obj.discount_code.get_percent))
        return








print("""
(1)registration
(2)login
(3)log out
(4)create Event
(5)Buy Ticket
""")
while True:
    choice = ''
    try:
        choice = int(input('Enter your choice'))
        # if choice == 1:
        #     p1 = Person()
    except:
        print('wrong format entered')
