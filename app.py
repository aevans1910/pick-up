import os
from flask import Flask, render_template,request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.PickUp
pickups = db.pickups

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trashpickup', methods=['GET'])
def trashpickup():
    return render_template('trashpickup.html')

@app.route('/pickups_submit', methods=['POST'])
def pickups_submit():
    """Submit a new trash pick up"""
    pickup = {
        'username': request.form.get('username'),
        'pick_up': request.form.get('pick-up'),
        'drop_off': request.form.get('drop-off'),
    }
    pickup_id = pickups.insert_one(pickup).inserted_id
    return redirect(url_for('pickup_new', pickup_id=pickup_id))

@app.route('/pickup_new/<pickup_id>', methods=['GET'])
def pickup_new(pickup_id):
    print(pickup_id)
    pickup = pickups.find_one({'_id': ObjectId(pickup_id)})
    print(pickup)
    return render_template('pickup_new.html', pickup=pickup)

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup_submit', methods=['POST'])
def signup_submit():
    """Sign up as a form, later will be user authentication"""
    signup = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'username': request.form.get('username'),
        'password': request.form.get('password'),
    }
    signup_id = pickups.insert_one(signup).inserted_id
    return redirect(url_for('signedup', signup_id=signup_id))

@app.route('/signedup/<signup_id>', methods=['GET'])
def signedup(signup_id):
    print(signup_id)
    signup = pickups.find_one({'_id': ObjectId(signup_id)})
    print(signup)
    return render_template('signedup.html', signup=signup)

@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))