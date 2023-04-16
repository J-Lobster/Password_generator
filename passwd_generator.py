import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphas = letters + digits + special_chars

def pwd_length():
  while True:
    try:
      pwd_length = int(input("Choose your password length: "))
      if pwd_length <= 5:
        print("The length must exceed 5 characters. Please try again.")
        continue
    except ValueError:
      print("This is not a valid entry. You may enter a number only.")
    else:
      break

pwd_length()