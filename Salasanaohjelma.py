import json
import re
import random
import string


def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

websites = []
usernames = []
encrypted_passwords = []

def add_password(website, username, password):
    is_valid = is_strong_password(password)
    if not is_valid:
        return False

    shift = 3
    encrypted_password = caesar_encrypt(password, shift)

    websites.append(website)
    usernames.append(username)
    encrypted_passwords.append(encrypted_password)
    print(f"Password for {website} added successfully!")
    return True

def get_password(website):
    if website in websites:
        index = websites.index(website)
        decrypted_password = caesar_decrypt(encrypted_passwords[index], 3)
        return usernames[index], decrypted_password
    else:
        return None, None

def save_passwords(filename="vault.txt"):
    data = {
        "websites": websites,
        "usernames": usernames,
        "encrypted_passwords": encrypted_passwords
    } 
    with open(filename, "w") as file:
        json.dump(data, file)
    
def load_passwords(filename):
    global websites, usernames, encrypted_passwords
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            websites = data["websites"]
            usernames = data["usernames"]
            encrypted_passwords = data["encrypted_passwords"]
            return data
    except FileNotFoundError:
        websites = []
        usernames = []
        encrypted_passwords = []
        return {"websites": [], "usernames": [], "encrypted_passwords": []}

# password validation
def is_strong_password(password):
    if len(password) < 10: #at least 10 characters
        print("Password is too short. Must be at least 10 characters long.")
        return False
    elif not re.search("[A-Z]", password):  #at least one uppercase letter.
        print("Password must contain at least one uppercase letter.")
        return False
    elif not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter.") #at least one lowercse letter
        return False
    elif not re.search("[0-9]", password): #at least one digit.
        print("Password must contain at least one digit")
        return False
    else:
        return True


def main():


  while True:
    print("\nPassword Manager Menu:")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Save Passwords")
    print("4. Load Passwords")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
            website = input("Enter website: ")
            username = input("Enter username: ")
            is_valid = False
            print("Please note that password must be at least 10 characters, contain at least one uppercase letter and contain at least one digit.")
            while is_valid == False:     
              password = input("Enter password: ")
              is_valid = is_strong_password(password)
              if is_valid:
                print("Valid Password.")
              else:
                print("Password does not meet requirements. Add new password.")

            add_password(website, username, password)

    elif choice == "2":
        website = input("Enter website to retrieve password: ")
        username, password = get_password(website)
        if username:
            print(f"Username: {username}")
            print(f"Password: {password}")
        else:
            print("Website not found.")

    elif choice == "3":
        save_passwords()
        print("Passwords saved successfully!")

    elif choice == "4":
        filename = "vault.txt"
        load_passwords(filename)
        print("Passwords loaded successfully!")

    elif choice == "5":
        break

    else:
            print("Wrong. Please try again.")


if __name__ == "__main__":
    main()