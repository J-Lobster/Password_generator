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