import random
import string

def generate_password(length):
    # Define the character pool for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(password_length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
