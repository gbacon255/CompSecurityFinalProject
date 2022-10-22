import getPass


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
  print('Registration Successful\n')
  # Opens file for user data storage, currently implemented with basic text file
  file = open('UserInfo.txt', 'wb')
  # prints plaintext user data to file format "Full Name Email Password")
  file.print(userFullName, ' ', userEmail, ' ', password)
else:
   # currently implemented to exit program upon user choosing not to register
   exit();
    
    
# function to grab user password, returns password    
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
