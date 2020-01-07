from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')