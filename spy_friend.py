import sys
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import Spy, ChatMessage
import csv


friends = []

def add_friend():
      friend_name = raw_input("What is your friend's name? ")
      friend_salutation = raw_input("salutation? (MR., Ms., Dr., Mrs.) ")
      friend_age = int(raw_input("What is the age of your friend?: "))
      friend_rating = float(raw_input("Enter rating(0-5): "))

      if friend_name.isalpha() == False: #checking whether name entered is valid or not
            print "Invalid name"
            sys.exit(0)

      if friend_age <= 12 or friend_age >= 50:
            print "Invalid age"
            sys.exit(0)
 
      new_friend = Spy(friend_name, friend_salutation, friend_age, friend_rating)
      friends.append(new_friend)

      print("Here is the updated list of friends")
      counter = 0
      for f in friends:
              counter += 1
              print '%d. %s' % (counter, f.name)

#Select friend to whom message is to be sent
def select_friend():
      counter = 0

      #Printing all the friends of a user
      for f in friends:
          counter += 1
          print '%d. %s' % (counter, f.name)
          

      #Asking the user to select a friend
      friend_choice = int(raw_input("Choose from your friends: "))
      friend_choice -= 1

      return friend_choice

def send_message():
      print "Choose the friend to whom you want to send the message"
      friend_choice = select_friend()

      original_image = raw_input("Enter the name of the image: ")
      output_path = 'output.jpg'
      text = raw_input("Enter the message to be concealed ")
      Steganography.encode(original_image, output_path, text)

      new_chat = ChatMessage(text, True)


      friends[friend_choice].chats.append(new_chat)
      print "Your secret message has been sent to %s" %friends[friend_choice].name


def read_message():
        print "Choose the friend whose message you want to read"
        sender = select_friend()

        if len(friends[sender].chats) == 0:
                print "You have no conversation with %s" %friends[sender].name
        else:
                for i in range(len(friends[sender].chats)):
                      print(friends[sender].chats[i].message)

        output_path = raw_input('what is the name of the file? ')
        secret_text = Steganography.decode(output_path)

        new_chat = ChatMessage(secret_text, False)

        friends[sender].chats.append(new_chat)
        print "Your secret message has beem saved\n" 
        print "Your message is '%s'" %secret_text
    

def load_friend():
  read_object = open("spy_friends.csv", 'r')
  reader  = csv.reader(read_object)
  for row in reader:
          name = row[0]
          salutation = row[1]
          age = int(row[2])
          rating = float(row[3])
          is_online = bool(row[4])
          new_friend = Spy(name, salutation, age, rating)
          friends.append(new_friend)
          print row
  read_object.close()

def save_friends():
  write_object = open("spy_friends.csv", 'w')
  writer = csv.writer(write_object)
  for i in range(len(friends)):
        name = friends[i].name
        salutation = friends[i].salutation
        age = friends[i].age
        rating = friends[i].rating
        is_online = friends[i].is_online
        writer.writerow([name,salutation,age,rating,is_online])
  write_object.close()


def read_chat_history():
  read_for = select_friend()
  print '\n'
  #navigating in all chats of a particular friend
  for chat in friends[read_for].chats:
    #checking if the chat message was sent by me
    if chat.sent_by_me:
      #assigning the time, time of type 1 April 2018, Sun 8:01
      time = chat.time.strftime("%d %B %Y, %a %H:%M")
      #spy = Spy(name, salutation)
      message = chat.message
      #printing the message with time details
      print '[%s]  %s' % (time, message)
    else:
      #assigning the time, time of type 1 April 2018, Sun 8:01
      time = chat.time.strftime("%d %B %Y, %a %H:%M")
      #spy = friends[read_for]
      print '[%s] %s' % (time, message)