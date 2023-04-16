import secrets, string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphas = letters + digits + special_chars

def pwd_length():
  while True:
    try:
      len = int(input("Choose your password length: "))
      if len <= 5:
        print("The length must exceed 5 characters. Please try again.")
        continue
    except ValueError:
      print("This is not a valid entry. You must only enter a number.")
    else:
      break
  return len

length = pwd_length()

def generator():
  while True:
    pwd = ''
    for i in range(length):
      pwd += ''.join(secrets.choice(alphas))

    if (any(char in special_chars for char in pwd) and 
        sum(char in digits for char in pwd)>=2):
          break
  print(pwd)

generator()