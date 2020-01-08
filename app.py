import os
from flask import Flask, render_template,request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.PickUp
pickups = db.pickups

app = Flask(__name__)

def video_url_creator(id_lst):
    videos = []
    for vid_id in id_lst:
        # We know that embedded YouTube videos always have this format
        video = 'https://youtube.com/embed/' + vid_id
        videos.append(video)
    return videos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trashpickup')
def trashpickup():
    return render_template('pickup_new.html')

@app.route('/pickups', methods=['POST'])
def pickups_submit():
    """Submit a new trash pick up"""
    # Grab the video IDs and make a list out of them
    video_ids = request.form.get('video_ids').split()
    # call our helper function to create the list of links
    videos = video_url_creator(video_ids)
    pickup = {
        'account': request.form.get('account'),
        'pick-up': request.form.get('pick-up'),
        'drop-off': request.form.get('drop-off'),
        'videos': videos,
        'video_ids': video_ids
    }
    pickups.insert_one(pickup)
    return redirect(url_for('trashpickup'))

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