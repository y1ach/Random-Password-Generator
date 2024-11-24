import random
import string

def createpassword():
    print("Random Password Creator")
    length = int(input("Length of the password: "))
    if length > 0:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ""
            for i in range(length):
                password += random.choice(characters)

            print(f"The Password: {password}")
    else:
            print("It should be more than 0!")

while True:
    createpassword()
