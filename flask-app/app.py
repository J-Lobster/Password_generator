from flask import Flask, render_template, request
from ..backend.pwd_gen import password_generator

app = Flask(__name__)

@app.route('/generator', methods=['POST'])
def generator():
    length = request.args.get('length', type=int)
    letters = request.args.get('letters', type=int)
    digits = request.args.get('digits', type=int)
    specials = request.args.get('specials', type=int)

    password = password_generator(length, letters, digits, specials)
    
    return render_template('index.html')
    return render_template('password.html', password=password)

if __name__ == "__main__":
    app.run(debug=True)
