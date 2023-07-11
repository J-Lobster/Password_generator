import secrets, string, random
from pwd_gen import generator
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

        if not letters.isalpha():
            error_messages.append(f" {letters} is an invalid entry, try again!")
        elif len(letters) <= 1 or len(letters) > max_alpha_limit.get_letter_tables[length]:
            error_messages.append(f"{letters} is {len(letters)} letters long. Create a word up to {max_alpha_limit.get_letter_tables[length]} letters long.")
        elif (digits, specials) not in max_nonalpha_limit.get_nonalpha_table(length).get(len(letters)):
            error_messages.append(f"{(digits, specials)} is an invalid entry. Choose from the following: {max_nonalpha_limit.get_nonalpha_table(length).get(len(letters))}")

        if error_messages:
            return render_template('index.html', error_messages=error_messages)

        password = generator(length, letters, digits, specials)

        return render_template('index.html', password=password)

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)