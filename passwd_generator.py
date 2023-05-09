import secrets, string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alpha = letters + digits + special_chars

def pwd_length():
  while True:
    try:
      len = int(input("Choose your password length: "))
      if len <= 7:
        print("The length must exceed 8 characters. Please try again.")
        continue
      elif len >= 21:
        print("You may not exceed a length of 21. Please try again.")
        continue
    except ValueError:
      print("This is not a valid entry. Only numbers are allowed.")
    else:
      break
  return len

length = pwd_length()

def digit_count():
  while True:
    try:
      min_digits = int(input("Enter a number of digits you wish to use: "))
      if min_digits <= 0:
        print(f"{min_digits} does not meet the minimum requirement. Please try again.")
        continue
      elif min_digits >= 9:
        print (f"{min_digits} exceeds the maximum number of digits permitted. Please try again.")
        continue
    except ValueError:
      print("This is an invalid entry. Only numbers are allowed.")
      continue
    else:
      break
  return min_digits

def specials_count():
  while True:
    try:
      8
      min_special_chars = int(input("Enter a number of special characters you wish to use: "))
      if min_special_chars <= 0:
        print(f"{min_special_chars} does not meet the minimum requirement. Please try again.")
        continue
      elif min_special_chars >= 9:
        print(f"{min_special_chars} exceeds the maximum number of special characters permitted. Please try again.")
        continue
    except ValueError:
      print("This is an invalid entry. Only numbers are allowed.")
      continue
    else:
      break
  return min_special_chars

def input_handler():
    digits_input = digit_count()
    specials_input = specials_count()
    while length == 8:
      try:
        if digits_input and specials_input >= 5:
          print(f"You entered {digits_input} for both inputs. Your inputs cannot be exceed your password length.")
          digits_input = digit_count()
          specials_input = specials_count()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 9:
      try:
        if digits_input and specials_input >= 5:
          print(f"You entered {digits_input} for both inputs. Your inputs cannot be exceed your password length.")
          digits_input = digit_count()
          specials_input = specials_count()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 10:
      try:
        if digits_input and specials_input >= 6:
          print(f"You entered {digits_input} for both inputs. Your inputs cannot be exceed your password length.")
          digits_input = digit_count()
          specials_input = specials_count()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 11:
      try:
        if digits_input and specials_input >= 6:
          print(f"You entered {digits_input} for both inputs. Your inputs cannot be exceed your password length.")
          digits_input = digit_count()
          specials_input = specials_count()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 12:
      try:
        if digits_input and specials_input >= 7:
          print(f"You entered {digits_input} for both inputs. Your inputs cannot be exceed your password length.")
          digits_input = digit_count()
          specials_input = specials_count()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 13:
      try:
        if digits_input and specials_input >= 7:
          print(f"You entered {digits_input} for both inputs. Your inputs cannot be exceed your password length.")
          digits_input = digit_count()
          specials_input = specials_count()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 14:
      try:
        if digits_input and specials_input >= 8:
          print(f"You entered {digits_input} for both inputs. Your inputs cannot be exceed your password length.")
          digits_input = digit_count()
          specials_input = specials_count()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 15:
      try:
        if digits_input and specials_input >= 8:
          print(f"You entered {digits_input} for both inputs. Your inputs cannot be exceed your password length.")
          digits_input = digit_count()
          specials_input = specials_count() 
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break
    return digits_input, specials_input

def generator():
  digit, special = input_handler()
  while True:
    pwd = ''
    for i in range(length):
      pwd += ''.join(secrets.choice(alpha))

    if (sum(char in special_chars for char in pwd) == special and 
        sum(char in digits for char in pwd) == digit):
          break
  print(pwd)

generator()