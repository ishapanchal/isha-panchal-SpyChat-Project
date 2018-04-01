import sys
import spy_friend
from spy_details import Spy, ChatMessage
import csv


STATUS_MESSAGE = []
                    # ["\nA Good Life is a Collection of Happy Moments",
                    # "\nSometimes we just have to let things go",
                    # "\nSilence is the most loud voice"]

def add_status(current_status_message):
    
    #Print the current status message
    if current_status_message == None:
        print "You do not have any current status message" 
    else:
        print "Your current status message is %s \n" % spy.current_status_message

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

def load_status():
    read_status = open("spy_status.csv", 'r')
    reader = csv.reader(read_status)
    for row in reader:
        message_selection = row[0]
        STATUS_MESSAGE.append(message_selection)
        print row
    spy.current_status_message = STATUS_MESSAGE[-1]
    read_status.close()    


def save_status():
    write_status = open("spy_status.csv", 'w')
    writer = csv.writer(write_status)
    for i in range(len(STATUS_MESSAGE)):
        message_selection = STATUS_MESSAGE[i].message_selection
        updated_status_message = new_status_message
        writer.writerow([current_status_message])
    write_status.close()
