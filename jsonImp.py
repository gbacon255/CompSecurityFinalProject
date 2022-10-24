import getpass
import sys
import crypt
import json
from cryptography.fernet import Fernet
def getPassword():
  # while loop set to run until same strings are entered
  while(1):
    # prompts user to enter password
    print('Please Enter a New Password\n')
    # I implemented the getpass library here to grab the user imput as ******, password contained as normal string
    userPassword = getpass.getpass()
    # prompts user to enter second password
    print('Please Re-enter Password\n')
    password2 = getpass.getpass()
    #compares the two passwords entered and if they are the same, while loop breaks and password is returned
    if userPassword == password2:
        break
  return userPassword

def encryptInit():
    keyIn = open('key', 'rb')
    key = keyIn.read()
    return key

def jsonPrint(userName, userEmail, password):
    data = {
            "Name": userName,
            "Email": userEmail,
            "Password": password
         }   
    jsonFormat = json.dumps(data, indent = 3)
    jsonApp = open("UserInfo.json", "a+")
    json.dump(jsonFormat, jsonApp)

# sets salt for password hashing
salt ='test'
# prompts the user to choose yes or no to creating new account
# to handle user input in this program, the input function was used.
userRegister = input('Do you want to register a new account: (y/n)')
#if user chooses to generate a new account
if(userRegister == 'y') or (userRegister == 'Y'):
    # Grabs user full name
    userFullName = input('Enter Full Name:\n')
    # Grabs User email address
    userEmail = input('Enter Email Address:\n')
    # Grabs user password
    password = getPassword()
    # encrypts password with generated salt
    password = crypt.crypt(password, salt)
    print('Registration Successful\n')
    jsonPrint(userFullName, userEmail,password)
else:
# currently implemented to exit program upon user choosing not to register
   exit()
                    
