from Register import *

#username

#Defines what username is 
username = ''

# While statement
while username  !=(usercreate):
    print('What is the Username?')
#have to have this otherwise continuously says what is the password
    username = input()
#if statement if the password is incorrect then it will retry otherwise it will say correct then ask for password
    if username !=(usercreate):
        print("Incorrect")
    else:
        print("Correct")

#password



#Defines what username is 
password = ''

# While statement
while password  !=(passcreate):
    print('What is the password?')
#have to have this otherwise continuously says what is the password
    password = input()
    if password !=(passcreate):
        print("Incorrect")
    else:
        print("Correct")
        open("Landing.py","r")

