import secrets, string


class pwd_generator:
  def __init__(self):
    self.letters = string.ascii_letters
    self.digits = string.digits
    self.special_chars = string.punctuation
    self.alpha = letters + digits + special_chars
 
# Handles password length.
  def usr_pwd_length():
    while True:
      try:
        length_input = int(input("Choose your password length: "))
        if length_input <= 7:
          print("The length must exceed 8 characters. Please try again.")
          continue
        elif length_input >= 21:
          print("You may not exceed a length of 21. Please try again.")
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break
    return length_input
  length = usr_pwd_length()
    
# This block handles digit inputs. 
  def usr_digits_length():
    while True:
      try:
        digit_input = int(input("Enter a number of digits you wish to use: "))
        if digit_input <= 1:
          print(f"{digit_input} does not meet the minimum requirement. Please try again.")
          continue
        elif digit_input >= 9:
          print (f"{digit_input} exceeds the maximum number of digits permitted. Please try again.")
          continue
      except ValueError:
          print("This is not a valid entry. Only numbers are allowed.")
      else:
        break
  digits_input = usr_digits_length()
  
# This block handles special character inputs.
  def usr_specials_length(): 
    while True:
      try:
        special_input = int(input("Enter a number of special characters you wish to use: "))
        if special_input <= 1:
          print(f"{special_input} does not meet the minimum requirement. Please try again.")
          continue
        elif special_input >= 9:
          print(f"{special_input} exceeds the maximum number of special characters permitted. Please try again.")
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break
  specials_input = usr_specials_length()

# These While blocks are meant to avoid inputs that exceed the length of the password. Antecedes against code hangs and generation lag.
  def input_handler():
    while length == 8:
      try:
        if digits_input and specials_input > 4:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 9:
      try:
        if digits_input and specials_input > 4:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 10:
      try:
        if digits_input and specials_input > 5:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 11:
      try:
        if digits_input and specials_input > 5:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 12:
      try:
        if digits_input and specials_input > 6:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 13:
      try:
        if digits_input and specials_input > 6:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 14:
      try:
        if digits_input and specials_input > 7:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 15:
      try:
        if digits_input and specials_input > 7:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 16:
      try:
        if digits_input and specials_input > 8:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 17:
      try:
        if digits_input and specials_input > 8:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 18:
      try:
        if digits_input and specials_input > 8:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 19:
      try:
        if digits_input and specials_input > 8:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break

    while length == 20:
      try:
        if digits_input and specials_input > 8:
          print(f"You entered {digit_input} for both inputs. Your inputs cannot be greater than your length.")
          self.usr_digits_length()
          self.usr_specials_length()
          continue
      except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")
      else:
        break
    return digits_input, specials_input
  handler1, handler2 = input_handler()

  def generator():
    while True:
      pwd = ''
      for i in range(length):
        pwd += ''.join(secrets.choice(alpha))
        
      if (sum(char in special_chars for char in pwd) == specials_input and 
          sum(char in digits for char in pwd) == digits_input):
            break
    print(pwd)
  generator = generator()
