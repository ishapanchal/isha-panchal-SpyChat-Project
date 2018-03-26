import sys
import default
import spy_status
import spy_friend
      
def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True

    while show_menu == True:
        menu_choice = raw_input("1. Add a status update\n2. Add Friend\n3. Exit Application")
        if menu_choice == '1':
            #update the status
            print "You have chosen to add a status"
            current_status_message = spy_status.add_status(current_status_message)
        elif menu_choice == '2':
            print "You have chosen to add a friend"
            spy_friend.add_friend()
        elif menu_choice == '3':
            show_menu = False 

print "Welcome to spychat Application"

choice=raw_input("Do you want to proceed with default settings(y/n)?: ")

spy = {}
if choice.upper() == 'Y': #verifying choice
    spy['name'] = default.spy['name']
    spy['age'] = default.spy['age']
    spy['rating'] = default.spy['rating']
    spy['is_online'] = default.spy['is_online']
    
else: #taking input from the user
    spy['name'] = raw_input("Enter your name: ")
    spy['age'] = int(raw_input("What is your age?: "))
    spy['rating'] = float(raw_input("What is your rating?: "))
    spy['is_online'] = True
       
#Validation of name and age
if spy['name'].isalpha() == False:
    print "Invalid name"
    sys.exit(0)

if spy['age'] <= 12 or spy['age'] >= 50:
    print "Invalid age"
    sys.exit(0)

print "Hello" + spy['name'] + ". "  
start_chat(spy['name'], spy['age'], spy['rating'])

