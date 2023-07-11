import secrets, string, random
from pwd_gen import usr_inputs, generator
from tables import non_alpha_tables, alpha_tables
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        length = int(request.form['length'])
        letters = str(request.form['letters'])
        digits = int(request.form['digits'])
        specials = int(request.form['specials'])

        max_alpha_limit = alpha_tables()
        max_nonalpha_limit = non_alpha_tables()
        error_messages = []

        if length < 8 or length > 20:
            error_messages.append(f"{length} does not meet the requirements. Please select from a range of 8-20.")

        if not letters.isalpha():
            error_messages.append(f" {letters} is an invalid entry, try again!")

        if len(letters) <= 1 or len(letters) > max_alpha_limit.get_max_letters[length]:
            error_messages.append(f"Invalid entry. Create a word up to {max_alpha_limit.get_max_letters[length]} letters long.")

        if digits <= 0 or specials <= 0 or (digits, specials) not in max_nonalpha_limit.get_max_nonalphas(length).get(len(letters)):
            error_messages.append(f"One or both of your choices are an invalid entries. Please select from the following combinations: {max_nonalpha_limit.get_max_nonalphas(length).get(len(letters))}")

        if error_messages:
            return render_template('index.html', error_messages=error_messages)

        password = generator(length, letters, digits, specials)

        return render_template('index.html', password=password)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)