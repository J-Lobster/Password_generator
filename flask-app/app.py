import secrets, string, random
from pwd_gen import usr_inputs, generator
from tables import alpha_tables, non_alpha_tables
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def password_generator():
    password = generator()
    return password

if __name__ == '__main__':
    app.run(debug=True)