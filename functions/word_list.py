from english_words import get_english_words_set
import secrets, string

def usr_pwd_length():
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

length = usr_pwd_length()

def word_gen():
  word_list = list(get_english_words_set(['web2'], alpha=True))
  for word in word_list:
    if len(word) >= length:
      continue
    else:
      break
      secrets.choice(word)    
  print(word)
  return word

word = word_gen()
digits = string.digits
special_chars = string.punctuation
non_alpha = digits + special_chars

def gen(alpha, len):
    while True:
        pwd = ''
        for i in range (len):
            pwd += ''.join(secrets.choice(word + non_alpha))

        if (any(char in special_chars for char in pwd) > word and 
        sum(char in digits for char in pwd) > word):
          continue
        else:
          break
    print (pwd)

gen(non_alpha, length)
