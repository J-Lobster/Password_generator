import secrets, string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alpha = letters + digits + special_chars

# Acts as the centralized input manager for the generator 
def input_handler():
  # Handles password length.
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
    
    # This block handles digit and special character inputs. 
    while True:
        try:
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
        except ValueError:
          print("This is not a valid entry. Only numbers are allowed.")
        else:
          break
    
    # These While blocks are meant to avoid inputs that exceed the length of the password. Antecedes against code hangs and generation slow down.
    while length == 8:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break

    while length == 9:
        if digit_input and special_input > 5:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break

    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break

    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break
    
    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break
    
    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break
    
    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break

    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break
    
    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break

    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break
    
    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break
    
    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break

    while length == 9:
        if digit_input and special_input > 4:
          print(f"You entered {digit_input} for both inputs. You inputs cannot be greater than your length.")
          continue
        else:
          break

    return length, digit_input, special_input

length, digit_input, special_input = input_handler()

def generator():
  while True:
    pwd = ''
    for i in range(length):
      pwd += ''.join(secrets.choice(alpha))

    if (sum(char in special_chars for char in pwd) == special_input and 
        sum(char in digits for char in pwd) == digit_input):
          break
  print(pwd)

generator()