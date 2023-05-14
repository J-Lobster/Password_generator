import secrets, string
from english_words import get_english_words_set

def length_input():
  while True:
    try:
      length = int(input("Choose your password length: "))
      if length < 8:
        print("The length must exceed 7. Please try again.")
        continue
      elif length > 20:
        print("You cannot not exceed a length of 20. Please try again.")
        continue
    except ValueError:
      print("This is not a valid entry. Only numbers are allowed.")
    else:
      break
  return length

def digits_input():
  while True:
    try:
      digits = int(input("Enter a number of digits you wish to use: "))
      if digits < 1:
        print(f"{digits} does not meet the minimum requirement. Please try again.")
        continue
      elif digits > 8:
        print (f"{digits} exceeds the maximum number of digits permitted. Please try again.")
        continue
    except ValueError:
      print("This is an invalid entry. Only numbers are allowed.")
      continue
    else:
      break
  return digits



def specials_input():
  while True:
    try:
      specials = int(input("Enter a number of special characters you wish to use: "))
      if specials < 1:
        print(f"{specials} does not meet the minimum requirement. Please try again.")
        continue
      elif specials > 8:
        print(f"{specials} exceeds the maximum number of special characters permitted. Please try again.")
        continue
    except ValueError:
      print("This is an invalid entry. Only numbers are allowed.")
      continue
    else:
      break
  return specials

def letters_input():  
  while length == 8:   
    try:
      letters = int(input("Choose the number of letters you desire in your word: "))
      if letters <= 0:
        print(f"{letters} is not a valid entry. Please select a higher letter count.")
        continue
      elif letters >= 4:
        print(f"{letters} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break

  while length == 9:   
    try:
      letters = int(input("Choose the number of letters you desire in your word: "))
      if letters <= 0:
        print(f"{letters} is not a valid entry. Please select a higher letter count.")
        continue
      elif letters >= 5:
        print(f"{letters} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break

  while length == 10:   
    try:
      letters = int(input("Choose the number of letters you desire in your word: "))
      if letters <= 0:
        print(f"{letters} is not a valid entry. Please select a higher letter count.")
        continue
      elif letters >= 6:
        print(f"{letters} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break  

  while length == 11:   
    try:
      word_input = int(input("Choose the number of letters you desire in your word: "))
      if letters <= 0:
        print(f"{letters} is not a valid entry. Please select a higher letter count.")
        continue
      elif letters >= 7:
        print(f"{letters} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break  
  
  while length == 12:   
    try:
      letters = int(input("Choose the number of letters you desire in your word: "))
      if letters <= 0:
        print(f"{letters} is not a valid entry. Please select a higher letter count.")
        continue
      elif letters >= 8:
        print(f"{letters} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break
  return letters

def word_gen():
  letters = letters_input()
  word_list = list(get_english_words_set(['web2'], alpha=True))
  for word in word_list:
    if len(word) > letters:
      continue
    else:
      if len(word) == letters:
        print(word)
        break
  return word

def input_handler():
    input_d = digits_input()
    input_s = specials_input()
    inputs = input_d + input_s
    while word == 3:
      try:
        if inputs == 5:
          break
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
          print(f"You entered {inputs} for both inputs. Your inputs cannot be exceed your password length.")
          input_d = digits_input()
          input_s = specials_input()
          continue

    while word == 3:
      try:
        if inputs == 5:
          break
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
          print(f"You entered {inputs} for both inputs. Your inputs cannot be exceed your password length.")
          input_d = digits_input()
          input_s = specials_input()
          continue

    while word == 3:
      try:
        if inputs == 5:
          break
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
          print(f"You entered {inputs} for both inputs. Your inputs cannot be exceed your password length.")
          input_d = digits_input()
          input_s = specials_input()
          continue

    while word == 3:
      try:
        if inputs == 5:
          break
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
          print(f"You entered {inputs} for both inputs. Your inputs cannot be exceed your password length.")
          input_d = digits_input()
          input_s = specials_input()
          continue

    while word == 3:
      try:
        if inputs == 5:
          break
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
          print(f"You entered {inputs} for both inputs. Your inputs cannot be exceed your password length.")
          input_d = digits_input()
          input_s = specials_input()
          continue

    while word == 3:
      try:
        if inputs == 5:
          break
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
          print(f"You entered {inputs} for both inputs. Your inputs cannot be exceed your password length.")
          input_d = digits_input()
          input_s = specials_input()
          continue

    while word == 3:
      try:
        if inputs == 5:
          break
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
          print(f"You entered {inputs} for both inputs. Your inputs cannot be exceed your password length.")
          input_d = digits_input()
          input_s = specials_input()
          continue

    while word == 3:
      try:
        if inputs == 5:
          break
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
          print(f"You entered {inputs} for both inputs. Your inputs cannot be exceed your password length.")
          input_d = digits_input()
          input_s = specials_input()
          continue
    return input_d, input_s



def password_generator():
  digit, special = input_handler()
  while True:
    pwd = ''
    for i in range(length):
      pwd += ''.join(secrets.choice(word + non_alpha))

    if (sum(char in special_chars for char in pwd) == special and 
        sum(char in digits for char in pwd) == digit):
          break
  print(pwd)


special_chars = string.punctuation
digits = string.digits
non_alpha = digits + special_chars
length = length_input()
word = word_gen()
password = password_generator()