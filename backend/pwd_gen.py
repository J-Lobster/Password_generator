import secrets, string, random

def generator(length, letters, digits, specials):
  nums = string.digits
  spls = string.punctuation
  non_alphas = nums + spls

  alphas = ''.join(secrets.choice([l.upper(), l])for l in letters)
  word = list(alphas)
  random.shuffle(word)
  shuffled_word = ''.join(word)

  while True:
    pwd = shuffled_word
    for i in range(length - len(shuffled_word)):
      pwd += ''.join(secrets.choice(non_alphas))

    if (sum(char in spls for char in pwd) == specials and 
        sum(char in nums for char in pwd) == digits):
          break

  return pwd