import secrets, string, random
from pwd_gen import usr_inputs, generator
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        length, letters, digits, specials = usr_inputs()
        password = generator(length, letters, digits, specials)
        
        return render_template('index.html', password=password)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)