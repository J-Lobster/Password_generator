import secrets, string
import array as arr

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

def input_err_handler(length):
  while length == 8:
    digit_input = int(input("Enter a number of digits you wish to use: "))
    special_input = int(input("Enter a number of special characters you wish to use: "))
    if digit_input <= 1:
      print(f"{digit_input} does not meet the minimum requirement. Please try again.")
      continue
    elif digit_input >= 9:
      print (f"{digit_input} exceeds the maximum number of digits permitted. Please try again.")
      continue
    if special_input <= 1:
      print(f"{special_input} does not meet the minimum requirement. Please try again.")
      continue
    elif special_input >= 9:
      print(f"{special_input} exceeds the maximum number of special characters permitted. Please try again.")
      continue
    break
  return digit_input, special_input

length = usr_pwd_length()
digit_input, special_input = input_err_handler(length)

def generator():
  pwd = ''
  for i in range(length):
    pwd += ''.join(secrets.choice(alpha))

  while sum(char in special_chars for char in pwd) != special_input or sum(char in digits for char in pwd) != digit_input:
    pwd = ''
    for i in range(length):
      pwd += ''.join(secrets.choice(alpha))

  return pwd


pwd = generator()
print(digit_input)
print(special_input)
print(pwd)