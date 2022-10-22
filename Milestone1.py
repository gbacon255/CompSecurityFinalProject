import getPass



userRegister = input("Do you want to register a new account: (y/n)")
#if user chooses to generate a new account
if(userRegister == 'y') or (userRegister == 'Y'):
  # Grabs user full name
  userFullName = input('Enter Full Name:\n')
  # Grabs User email address
  userEmail = input('Enter Email Address:\n')
  # Grabs user password
  password = getPassword()
  print('Registration Successful\n')
  file = open('UserInfo.txt', 'wb')
  file.print(userFullName, ' ', userEmail, ' ', password);
else:
   exit();
    
    
    
def getPassword():
  while(1):
    print('Please Enter a New Password\n')
    userPassword = getpass.getpass()
    print('Please Re-enter Password\n')
    password2 = getpass.getpass()
    if userPassword == password2:
      break
  return userPassword
