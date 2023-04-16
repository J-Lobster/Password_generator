import secrets, string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphas = letters + digits + special_chars

def pwd_length():
  while True:
    try:
      length = int(input("Choose your password length: "))
      if length <= 5:
        print("The length must exceed 5 characters. Please try again.")
        continue
    except ValueError:
      print("This is not a valid entry. You must only enter a number.")
    else:
      break
  return length

length = pwd_length()

def secrets_generator(length):
  while True:
    pwd = ''
    for i in range(length):
      pwd += ''.join(secrets.choice(alphas))

    if (any(char in special_chars for char in pwd) and 
        sum(char in digits for char in pwd)>=2):
          break
  print(pwd)

secrets_generator(length)