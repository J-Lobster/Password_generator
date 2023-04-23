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

def stop_same_inputs():
    while True:
        if specials_input == digits_input or digits_input == specials_input:
            print ("You cannot have the same number of digits and special characters. Please try again.")
            usr_digits_length()
            usr_specials_length()
            break

stop = stop_same_inputs()