def input_err_handler(digit_input,special_input):
  while True:
    digit_input = int(input("Enter a number of digits you wish to use: "))
    special_input = int(input("Enter a number of special characters you wish to use: "))
    if digit_input or special_input <= 1:
      print("Both inputs require a minimum of 2 characters. Please try again.")
      continue
    elif digit_input or special_input >= 9:
      print ("Both inputs cannot exceed 8 characters. Please try again.")
      continue
    else:
      break
  return digit_input, special_input