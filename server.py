import random 	                # import the random module

# added render_template!
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key = "kobi bean wuz hur"


@app.route('/')
def index():
    if "num" and "guess" not in session:
        session['num'] = random.randint(1, 100)
        # session['guess'] = 0
        return render_template('index.html')
    return render_template('index.html')


@app.route('/guess', methods=['POST'])  # will default to git, but
def guess():
    # putting the request form into session
    session['guess'] = int(request.form['guess'])
    print(type(session['guess']))
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
