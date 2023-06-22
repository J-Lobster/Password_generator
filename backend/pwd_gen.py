import secrets, string 
from english_words import get_english_words_set
from tables import alpha_tables, non_alpha_tables


def usr_inputs():
  max_letters_limit = alpha_tables()

  max_nonalpha_limit = non_alpha_tables()

  while True:
    try:
      length = int(input("Choose your password length: "))
      if length < 8 or length > 20:
        print(f"{length} does not meet the requirements. Please select from a range of 8-20.")
        continue
    except ValueError:
      print("This is not a valid entry. Only numbers are allowed.")
    else:
      break
    
  while True:
    try:
      letters = int(input(f"Enter the number of letters you wish to use (up to {max_letters_limit.max_letters[length]}): "))
      if letters <= 1 or letters > max_letters_limit.max_letters[length]:
        print(f"Invalid entry. Choose a number up to {max_letters_limit.max_letters[length]}.")
        continue
    except ValueError:
      print("Invalid entry. Only numbers are allowed.")
    else:
      break

  while True:
    try:
      digits = int(input("Enter a number of digits you wish to use: "))
      specials = int(input("Enter a number of special characters you wish to use: "))
      if digits <= 0 or specials <= 0 or (digits, specials) not in max_nonalpha_limit.get_nonalpha(length).get(letters, []):
        print(f"One or both of your choices is an invalid entry. \nDigits: {digits} \nSpecials: {specials} \nPlease select from the following {max_nonalpha_limit.get_nonalpha(length).get(letters, [])}")
        continue
    except ValueError:
      print("This is an invalid entry. Only numbers are allowed.")
    else:
      break

  return length, letters, digits, specials

def password_generator():
  numbers = string.digits
  special_chars = string.punctuation
  non_alpha = numbers + special_chars
  length, letters, digits, specials = usr_inputs()
  word_list = list(get_english_words_set(['web2'], alpha=True))

  for word in word_list:
    if len(word) > letters:
      continue
    else:
      if len(word) == letters:
        print(word)
        break

  while True:
    pwd = ''
    for i in range(length):
      pwd += ''.join(secrets.choice(word + non_alpha))

    if (sum(char in special_chars for char in pwd) == specials and 
        sum(char in numbers for char in pwd) == digits):
          break
  print(pwd)

  return pwd

pwd = password_generator()