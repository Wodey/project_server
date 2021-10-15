import os
from datetime import date
from db import get_db
from flask import Flask, request
from hashlib import md5
app = Flask(__name__)


db = get_db()

@app.route("/")
def hello_world():
    return {
        "username": "hey",
        "uid": "fasf324",
        "tids": ["sgsg", "sf3400", "gfdb994", "234fdg"],
        "rating": 15
    }
#AUTHENTICATION ROUTES
@app.route("/register", methods=["POST"])
def register():
    #add code later
    return 0

@app.route("/login", methods=["POST"])
def login():
    return 0
@app.route("/unauth")
def unauth():
    #add code later
    return 0

#TASK ROUTES
@app.route("/get_tasks/<uid>")
def get_task(uid):
        collection = db.userss
        collection.insert_one({'db': 'sdf'})
        cursor = collection.find({})

        return "1"

@app.route("/skip_task/<uid>/<tid>")
def skip_task():
    #add code later
    return 0

@app.route("/ask_help", methods=["POST"])
def ask_help():
    #add code later
    return 0

@app.route("/deliver_task/<uid>", methods=["POST"])
def deliver_task():
    #add code later
    return 0

#RESULTS ROUTES
@app.route("/get_results")
def get_results():
    return 0

#ADMIN ROUTES
@app.route("/admin/add_task", methods=["POST"])
def add_task():
    try:
        data = request.get_json()
        return "1"
    except:
        return "0"

@app.route("/admin/delete_task/<tid>")
def delete_task():
    #add code later
    return 0

@app.route("/admin/stop_lesson")
def stop_lesson():
    #add code later
    return 0


app.run(debug=True)