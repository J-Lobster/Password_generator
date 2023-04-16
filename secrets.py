while True:
  pwd = ''
  for i in pwd_length():
    pwd += ''.join(secrets.choice(alphas))

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(pwd)
