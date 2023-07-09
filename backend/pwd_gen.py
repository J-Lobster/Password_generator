import secrets, string, random
from tables import alpha_tables, non_alpha_tables
from flask import request

def usr_inputs(length, letters, digits, specials):
  max_alpha_limit = alpha_tables()
  max_nonalpha_limit = non_alpha_tables()

  error_messages = []

  while True:
    if length < 8 or length > 20:
        error_messages.append(f"{length} does not meet the requirements. Please select from a range of 8-20.")
        continue
    else:
      break

  while True:
    if not letters.isalpha():
      error_messages.append("Invalid entry, letters only!")
    elif len(letters) <= 1 or len(letters) > max_alpha_limit.get_max_letters[length]:
      error_messages.append(f"Invalid entry. Create a word up to {max_alpha_limit.get_max_letters[length]} letters long.")
      continue
    else:
      print(letters)
      break

  while True:
    if digits <= 0 or specials <= 0 or (digits, specials) not in max_nonalpha_limit.get_max_nonalphas(length).get(len(letters)):
      error_messages.append(f"One or both of your choices is an invalid entry. \nDigits: {digits} \nSpecials: {specials} \nPlease select from the following {max_nonalpha_limit.get_max_nonalphas(length).get(len(letters))}")
      continue
    else:
      break
    print(digits, specials)
  return length, letters, digits, specials, error_message

#length, letters, digits, specials, error_message = usr_inputs(length, letters, digits, specials)

def generator(length,letters,digits,specials):
  
  nums = string.digits
  spls = string.punctuation
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
