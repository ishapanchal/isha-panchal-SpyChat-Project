import sys
import spy_status
import spy_friend
import csv

#Import the default spy object
from spy_details import Spy
from spy_details import Spy, ChatMessage

print "Welcome to spychat Application"

profile_choice=raw_input("Do you want to proceed with default settings(y/n)?: ")
if profile_choice.upper() == 'Y': #verifying choice
    spy = Spy("Mick", "Mr.", 25, 5.0)

    
else: #taking input from the user
        name = raw_input("Enter your name: ")
        salutation = raw_input("What should we call you? (Mr., Ms., Mrs., Dr.) ")
        age = int(raw_input("What is your age?: "))
        rating = float(raw_input("What is your rating?: "))
        is_online = True
       
#Validation of name and age
        if name.isalpha() == False:
                print "Invalid name"
                sys.exit(0)

        if age <= 12 or age >= 50:
                print "Invalid age"
                sys.exit(0)

        spy = Spy(name, salutation, age, rating)

print "\nHello %s %s " %(spy.salutation, spy.name)
print "We have successfully created your account"  


def start_chat():
    show_menu = True
    while show_menu == True:
        menu_choice = raw_input("1. Add a status update\n2. Add Friend\n3. Send message to a friend\n4. Read secret messages of a friend\n 5. Exit Application")
        if menu_choice == '1':
            #update the status
            print "\nYou have chosen to add a status"
            spy.current_status_message = spy_status.add_status(spy.current_status_message)
        elif menu_choice == '2':
            print "\nYou have chosen to add a friend"
            spy_friend.add_friend()
        elif menu_choice == '3':
            print "\nYou have chosen to send a secret message to a friend"
            spy_friend.send_message()
        elif menu_choice == '4':
            print "\nYou have chosen to read a secret message of a friend"
            spy_friend.read_message()
        elif menu_choice == '5':
            print "\nYou have chosen to close the Application"
            spy_friend.save_friends()
            show_menu = False
        else:
            print "\nInCorrect Choice" 

spy_friend.load_friend()
start_chat()
spy_friend.save_friends()