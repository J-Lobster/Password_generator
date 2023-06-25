import secrets, string, random
from pwd_gen import usr_inputs, generator
from tables import alpha_tables, non_alpha_tables
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    inputs = usr_inputs
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generated_password():
    length = request.form.get('length')
    letters = request.form.get('letters')
    digits = request.form.get('digits')
    specials = request.form.get('specials')
    return render_template('generator.html', generated_password=generated_password)

if __name__ == '__main__':
    app.run(debug=True)