import secrets, string, random
from tables import alpha_tables, non_alpha_tables

nums = string.digits
spls = string.punctuation

def usr_inputs():
  max_alpha_limit = alpha_tables()
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
      letters = str(input(f"Enter a word that are up to {max_alpha_limit.get_max_letters[length]} letters long: "))
      if not letters.isalpha():
        print("Invalid entry, letters only!")
        continue
      elif len(letters) <= 1 or len(letters) > max_alpha_limit.get_max_letters[length]:
        print(f"Invalid entry. Create a word up to {max_alpha_limit.get_max_letters[length]} letters long.")
        continue
    except ValueError:
      print("Invalid entry. Only numbers are allowed.")
    else:
      break

  while True:
    try:
      digits = int(input("Enter a number of digits you wish to use: "))
      specials = int(input("Enter a number of special characters you wish to use: "))
      if digits <= 0 or specials <= 0 or (digits, specials) not in max_nonalpha_limit.get_max_nonalphas(length).get(len(letters)):
        print(f"One or both of your choices is an invalid entry. \nDigits: {digits} \nSpecials: {specials} \nPlease select from the following {max_nonalpha_limit.get_max_nonalphas(length).get(len(letters))}")
        continue
    except ValueError:
      print("This is an invalid entry. Only numbers are allowed.")
    else:
      break

  return length, letters, digits, specials

def generator():
  length, letters, digits, specials = usr_inputs()
  non_alphas = nums + spls

  alphas = ''.join(secrets.choice([l.upper(), l])for l in letters)
  word = list(alphas)
  random.shuffle(word)
  shuffled_word = ''.join(word)

  while True:
    pwd = shuffled_word
    for i in range(length - len(shuffled_word)):
      pwd += ''.join(secrets.choice(non_alphas))

    if (sum(char in spls for char in pwd) == specials and 
        sum(char in nums for char in pwd) == digits):
          break

  return pwd

pwd = generator()
