from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.htm')

@app.route('/fb')
def fb():
    return render_template('facebook.htm')

app.run(debug=True) 