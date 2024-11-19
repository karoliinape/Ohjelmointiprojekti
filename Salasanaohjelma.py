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

def is_strong_password(password):
    # Vähintään 8 merkkiä pitkä
    if len(password) < 8:
        return False
    
    # Sisältää pieniä ja isoja kirjaimia, numeroita ja erikoismerkkejä
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@$!%*?&]', password):
        return False
    
    return True

def generate_password(length):
    # Luo satunnainen vahva salasana
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


encrypted_passwords = []
websites = []
usernames = []

def add_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Tarkistetaan, onko salasana vahva
    if not is_strong_password(password):
        print("Warning: The password is weak. Use stronger one.")
        choice = input("Do you want to generate a random strong password? (yes/no): ")
        if choice.lower() == "yes":
            password = generate_password(12)  # Luo 12-merkkinen vahva salasana

    # Salasanan salaus
    shift = 3 
    encrypted_password = caesar_encrypt(password, shift)

    
    websites.append(website)
    usernames.append(username)
    encrypted_passwords.append(encrypted_password)

    print(f"Password for {website} added successfully!")

def get_password():
    website = input("Enter website to retrieve password: ")
    
    if website in websites:
        index = websites.index(website)
        decrypted_password = caesar_decrypt(encrypted_passwords[index], 3) 
        print(f"Username: {usernames[index]}")
        print(f"Password: {decrypted_password}")
    else:
        print("Website not found.")

def save_passwords():
    data = {
        "websites": websites,
        "usernames": usernames,
        "encrypted_passwords": encrypted_passwords
    }
    
    with open("vault.txt", "w") as file:
        json.dump(data, file)
    print("Passwords saved successfully!")

    
def load_passwords():
    global websites, usernames, encrypted_passwords
    try:
        with open("vault.txt", "r") as file:
            data = json.load(file)
            websites = data["websites"]
            usernames = data["usernames"]
            encrypted_passwords = data["encrypted_passwords"]
        print("Passwords loaded successfully!")
    except FileNotFoundError:
        print("No saved passwords found.")



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
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        save_passwords()
    elif choice == "4":
        passwords = load_passwords()
        print("Passwords loaded successfully!")
    elif choice == "5":
        break
    else:
        print("Wrong. Please try again.")


if __name__ == "__main__":
    main()