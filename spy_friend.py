import sys
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import Spy, ChatMessage

friends = []
#Default list of Friends of our spy
Friend_one = Spy('agentx', 'Mr.', 25, 4.9)
Friend_two = Spy('agenty', 'Ms.', 21, 4.39)
Friend_three = Spy('agentz', 'Dr.', 37, 4.89)

friends = [Friend_one, Friend_two, Friend_three]


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
      friend_choice = raw_input("Choose from your friends")
      friend_choice_position = int(friend_choice) - 1

      return friend_choice_position

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
    