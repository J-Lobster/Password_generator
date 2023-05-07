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