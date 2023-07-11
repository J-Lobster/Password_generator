from tables import alpha_tables, non_alpha_tables

def error_handler(length, letters, digits, specials):
  max_alpha_limit = alpha_tables()
  max_nonalpha_limit = non_alpha_tables()
  error_messages = []
  if not letters.isalpha():
    error_messages.append(f" {letters} is an invalid entry, try again!")
  elif len(letters) <= 1 or len(letters) > max_alpha_limit.get_letter_tables[length]:
    error_messages.append(f"{letters} is {len(letters)} letters long. Create a word up to {max_alpha_limit.get_letter_tables[length]} letters long.")
  elif (digits, specials) not in max_nonalpha_limit.get_nonalpha_table(length).get(len(letters)):
    error_messages.append(f"{(digits, specials)} is an invalid entry. Choose from the following: {max_nonalpha_limit.get_nonalpha_table(length).get(len(letters))}")
  return error_messages