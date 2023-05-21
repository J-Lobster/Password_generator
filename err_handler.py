def usr_inputs():
  max_letters_limit = {
    8: 3,
    9: 4,
    10: 5,
    11: 6,
    12: 7,
    13: 8,
    14: 9,
    15: 10,
    16: 11,
    17: 12,
    18: 13,
    19: 14,
    20: 15
  }

  max_others_limit = {
    2: [(3, 3), (2, 4), (4, 2), (1, 5), (5, 1)],
    3: [(1, 4), (4, 1), (2, 3), (3, 2)],
    4: [(1, 4), (4, 1), (2, 3), (3, 2)],
    5: [(1, 4), (4, 1), (2, 3), (3, 2)],
    6: [(1, 4), (4, 1), (2, 3), (3, 2)],
    7: [(1, 4), (4, 1), (2, 3), (3, 2)],
    8: [(1, 4), (4, 1), (2, 3), (3, 2)],
    9: [(1, 4), (4, 1), (2, 3), (3, 2)],
    10: [(1, 4), (4, 1), (2, 3), (3, 2)],
    11: [(1, 4), (4, 1), (2, 3), (3, 2)],
    12: [(1, 4), (4, 1), (2, 3), (3, 2)],
    13: [(1, 4), (4, 1), (2, 3), (3, 2)],
    14: [(1, 4), (4, 1), (2, 3), (3, 2)],
    15: [(1, 4), (4, 1), (2, 3), (3, 2)]
  }

  while True:
    try:
      length = int(input("Choose your password length: "))
      if length < 8 or length > 20:
        print(f"{length} does not meet the requirements. Please select from a range of 8-20.")
        continue
    except ValueError:
      print("This is not a valid entry. Only numbers are allowed.")
    else:
      break
    
  while True:
    try:
      letters = int(input(f"Choose the number of letters you desire in your word (up to {max_letters_limit[length]}): "))
      if letters <= 1 or letters > max_letters_limit[length]:
        print(f"Invalid entry. Choose a number up to {max_letters_limit[length]}.")
        continue
    except ValueError:
      print("Invalid entry. Only numbers are allowed.")
    else:
      break

  while True:
    try:
      digits = int(input("Enter a number of digits you wish to use: "))
      specials = int(input("Enter a number of special characters you wish to use: "))
      if digits <= 0 or specials <= 0 or (digits, specials) not in max_others_limit[letters]:
        print(f"One or both of your choices: ({digits}, {specials}) \nExceeds the allowed values for either category. \nYou can choose from the following: {max_others_limit[letters]}")
        continue
    except ValueError:
      print("This is an invalid entry. Only numbers are allowed.")
    else:
      break

  return length, digits, specials, letters

length, digits, specials, letters = usr_inputs()