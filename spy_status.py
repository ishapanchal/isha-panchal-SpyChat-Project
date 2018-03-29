import sys
import spy_friend
from spy_details import Spy, ChatMessage

STATUS_MESSAGE = []
def add_status(current_status_message):
    
    #Print the current status message
    if current_status_message == None:
        print "You do not have any current status message" 
    else:
        print "Your current status message is " +current_status_message

    update_choice = raw_input("Do you want to select from older status(y/n)?: ")
    if update_choice.upper() == 'N':
        new_status_message = raw_input("Enter new status message: ")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGE.append(updated_status_message)

    elif update_choice.upper() == 'Y':
        for i in range(len(STATUS_MESSAGE)):
            print(str(i+1) + " " + STATUS_MESSAGE[i])

        message_selection = int(raw_input("\n Choose from the older messages "))
        if len(STATUS_MESSAGE) > message_selection:
            updated_status_message = STATUS_MESSAGE[message_selection-1] 

            return updated_status_message