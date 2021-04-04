import time

class Registration():

    def __init__(self,nick, password):
        self.nick = nick
        self.password = password

    def data(self):
        (self.nick + " " + self.password)

print("*Registration*")
print("Enter your nickname:")
name = str(input())

print("Enter your password:")
pas = str(input())

registration = Registration(name, pas)

print("*Login*")
print("Enter your nickname:")
your_name = str(input())

print("Enter your password:")
your_pas = str(input())

login = Registration(your_name, your_pas)

if login.data() == registration.data():
    x = input("Write what u gonna buy:")
    shopping_list = x.split(',')
    

    mobile_app = [i for i in shopping_list]

    print("Hey, do not forget to buy:", mobile_app, "\n" , "Great day")
else:
    print("Wrong password, try again")

    
time.sleep(3)


  
