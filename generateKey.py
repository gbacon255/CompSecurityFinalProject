from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = open('key', 'wb')
f.write(key)
