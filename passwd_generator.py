import secrets, string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alpha = letters + digits + special_chars

def usr_pwd_length():
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

length = usr_pwd_length()

def usr_digits_length():
  while True:
    try:
      min_digits = int(input("Enter a number of digits you wish to use: "))
      if min_digits <= 1:
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

digits_input = usr_digits_length()

def usr_specials_length():
  while True:
    try:
      8
      min_special_chars = int(input("Enter a number of special characters you wish to use: "))
      if min_special_chars <= 1:
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

specials_input = usr_specials_length()

def generator():
  while True:
    pwd = ''
    for i in range(length):
      pwd += ''.join(secrets.choice(alpha))

    if (sum(char in special_chars for char in pwd) == specials_input and 
        sum(char in digits for char in pwd) == digits_input):
          break
  print(pwd)

generator()