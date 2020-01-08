import os
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trashpickup')
def location():
    return render_template('trashpickup.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))