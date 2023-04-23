def usr_digits_special_length():
  while True:
    try:
      min_special_chars = int(input("Enter a number of special characters you wish to use: "))
      min_digits = int(input("Enter a number of digits you wish to use: "))
      if min_special_chars <= 0:
        print(f"{min_special_chars} does not exceed 0. Please try again.")
        continue
      elif min_digits <= 1:
        print(f"{min_digits} does not exceed 1. Please try again.")
        continue
    except ValueError:
      print("This is an invalid entry. Only numbers are allowed.")
      continue
    else:
      break
    return min_special_chars and min_digits

usr_digits_special_length()


