from english_words import get_english_words_set
import secrets, string

def pwd_length():
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

length = pwd_length()

def letter_count():  
  while length == 8:   
    try:
      word_input = int(input("Choose the number of letters you desire in your word: "))
      if word_input == 0:
        print(f"{word_input} is not a valid entry. Please select a higher letter count.")
        continue
      elif word_input >= 4:
        print(f"{word_input} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break

  while length == 9:   
    try:
      word_input = int(input("Choose the number of letters you desire in your word: "))
      if word_input == 0:
        print(f"{word_input} is not a valid entry. Please select a higher letter count.")
        continue
      elif word_input >= 5:
        print(f"{word_input} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break

  while length == 10:   
    try:
      word_input = int(input("Choose the number of letters you desire in your word: "))
      if word_input == 0:
        print(f"{word_input} is not a valid entry. Please select a higher letter count.")
        continue
      elif word_input >= 6:
        print(f"{word_input} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break  

  while length == 11:   
    try:
      word_input = int(input("Choose the number of letters you desire in your word: "))
      if word_input == 0:
        print(f"{word_input} is not a valid entry. Please select a higher letter count.")
        continue
      elif word_input >= 7:
        print(f"{word_input} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break  
  
  while length == 12:   
    try:
      word_input = int(input("Choose the number of letters you desire in your word: "))
      if word_input == 0:
        print(f"{word_input} is not a valid entry. Please select a higher letter count.")
        continue
      elif word_input >= 8:
        print(f"{word_input} is too many letters. Choose a number lower than 5")
        continue
    except ValueError:
        print("This is not a valid entry. Only numbers are allowed.")  
    else:
      break

  return word_input

letters = letter_count()

def word_gen():
  word_list = list(get_english_words_set(['web2'], alpha=True))
  for word in word_list:
    if len(word) > letters:
      continue
    else:
      if len(word) == letters:
        print(word)
        break
  return word

word = word_gen()
digits = string.digits
special_chars = string.punctuation
non_alpha = digits + special_chars