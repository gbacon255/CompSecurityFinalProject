#imports modules
import getpass
from pickle import FALSE
import sys
import crypt
import json
import os
import re
from cryptography.fernet import Fernet
from Crypto.Hash import SHA256

def commandLoop():
    print('Type "help" for commands\n')
    while(1):
        menuInput = input('SecureDrop>')
        if(menuInput ==  'exit'):
            break
        if(menuInput == 'add'):
            addContact()
        if(menuInput == 'help'):
            helpMenu()

def helpMenu():
    print('"add"  ->  Add a new contact')
    print('"list" ->  List all online contacts')
    print('"send" ->  Transfer file to contact')
    print('"exit" ->  Exit SecureDrop')

def write_json(ContactData, filename="UserInfo.json"):
    with open (filename, 'w') as file:
        json.dump(ContactData, file, indent=4)
    file.close()


def addContact():
    contactName = input("Enter Full Name: ")
    contactEmail = input("Enter Email Address: ")
    #insert pass to json here
    with open ("UserInfo.json") as file:
        pData = json.load(file)
        temp = pData['Contacts']
        y = {"ContactName": contactName, "ContactEmail": contactEmail}
        temp.append(y)
    write_json(pData)
    print("Contact Added.")

def passwordValidation(passwd) -> bool:
    l, u, p, d = 0, 0, 0, 0
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if(len(passwd) >= 8 ):
        for i in passwd:
            if (i.islower()):
                l += 1
            if (i.isupper()):
                u += 1
            if (i.isdigit()):
                p += 1
    if(regex.search(passwd) is not None):
        d =+ 1

    return bool(l >= 1 and u >= 1 and p >= 1 and d >= 1)

def getPassword():

    attemptsCounter = 3
    Password = ''
    while(attemptsCounter != 0):
        # prompts user to enter password
        print('\nPlease Enter a New Password')
        # I implemented the getpass library here to grab the user imput as ******, password contained as normal string
        userPassword1 = getpass.getpass()
        # prompts user to enter second password
        print('Please Re-enter Password')
        userPassword2 = getpass.getpass()

        if(attemptsCounter == 1):
            print("Maximum number of attempts exceeded.")
            print("Exiting SecureDrop.\n")
            exit()
        elif (userPassword1 != userPassword2):
            print("Passwords don't match")
            attemptsCounter -= 1
        else:
            if(passwordValidation(userPassword1)):
                password = userPassword1
                break
            else:
                print("The password needs to have the following:")
                print("8 characters")
                print("1 uppercase character")
                print("1 lowercase character")
                print("1 special character")
                print("Please try again")

    return password


def encryptInit():
    keyIn = open('key', 'rb')
    key = keyIn.read()
    return key

# formats user data into a json string and appends to a json file
def jsonPrint(userName, userEmail, password):
    data = {
                "Name":userName,
                "Email":userEmail,
                "Password":password,
                "Contacts":[
                    {
                        "ContactName": 'NULL',
                        "ContactEmail":'NULL'
                    }
                ]
            }
    # formats the json string
    jsonFormat = json.dumps(data, indent = 4)
    #opens file to append mode and appends data
    with open("UserInfo.json", "a+") as file:
        file.write(jsonFormat)

def registerUsername():
    userRegister = input('Do you want to register a new account?: (y/n): ')
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
        print("Exiting SecureDrop.\n")

# sets salt for password hashing
hash_object = SHA256.new(data=b'Test')
salt = hash_object.hexdigest()
#Password
# prompts the user to choose yes or no to creating new account
# to handle user input in this program, the input function was used.
if(os.path.exists("UserInfo.json")):
    with open('UserInfo.json', 'r') as file:
        data= json.load(file)
    while (1): 
        userEmail = input('Enter Email Address:\n')
        userPassword = getpass.getpass()

        entered_pw = crypt.crypt(userPassword, salt)
        if(userEmail == data["Email"] and entered_pw == data["Password"]):
            print("Welcome\n")
            commandLoop();
            break;
        else:
            print("Incorrect user")
        
else:
    print("No users are registered with this client\n")
    registerUsername();
    
