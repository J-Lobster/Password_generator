from pwd_gen import generator
from error_handler import error_handler
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        length = int(request.form['length'])
        letters = str(request.form['letters'])
        digits = int(request.form['digits'])
        specials = int(request.form['specials'])

        error_messages = error_handler(length, letters, digits, specials)
        if error_messages:
            return render_template('index.html', error_messages=error_messages)

        password = generator(length, letters, digits, specials)
        return render_template('index.html', password=password)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)