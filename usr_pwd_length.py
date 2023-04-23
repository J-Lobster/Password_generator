def usr_pwd_length():
  while True:
    try:
      len = int(input("Choose your password length: "))
      if len <= 5:
        print("The length must exceed 5 characters. Please try again.")
        continue
    except ValueError:
      print("This is not a valid entry. Only numbers are allowed.")
    else:
      break
  return len

length = usr_pwd_length()
print(length)