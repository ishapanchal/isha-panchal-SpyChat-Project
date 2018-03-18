import sys
import default

print "Welcome to spychat"

choice=raw_input("Enter 1 if you want default settings ")
if choice == '1': #verifying choice

    spy_name = default.spy_name
    spy_salutation = default.spy_salutation
    spy_age = default.spy_age
    spy_rating = default.spy_rating
    print "hello" +spy_salutation + spy_name
    print "your age is "+ spy_age
    print "your rating is "+ spy_rating
    
else: #taking input from the user
    spy_name = raw_input ("Enter your name ") 
    if spy_name.isalpha() == False: #checking whether name entered is valid or not
       print "Please Enter a valid name. "
       print "Name should be only in alphabets (A-Z or a-z)"
       sys.exit(0) #if name is not valid exit

    spy_salutation = raw_input("Enter your Salutation (Mr. , Ms. or Mrs.):")
    
    spy_age = raw_input("Enter your age ")
    if type(spy_age)   == int: #validating the age of the spy
        if int(spy_age) <= 12: 
    	   print "you are too young to become a spy"
    	   sys.exit(0)
        if int(spy_age) >= 50:
            print "you are too old to be a spy"
            sys.exit(0)
    spy_rating = raw_input("Enter your rating (A, B or C) ")  
    print "hello " + spy_salutation + spy_name #printing welcome message
    print "your age is "+ spy_age
    print "your rating is "+ spy_rating

    if spy_rating == 'A':    #compairing ratings
        print "you are a 3 star spy"
    elif spy_rating =='B':
        print "you are a 2 star spy"
    elif spy_rating == 'C':
        print "you are a 1 star spy"     
    else:
    	print "you have entered incorrect rating"
    	sys.exit(0)
    #print ("hello" + spy_salutation + spy_name)
    #print ("your age is " + spy_age)
    #print ("your rating is " + spy_rating)	
    
