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
    data = request.get_json()
    users = db['users']
    tasks = db['tasks'].find()
    if users.find_one({"username": data["username"]}):
        return "1"
    post = users.insert_one({"username": data["username"], "uncompleted_tasks": [k._id for k in tasks], "score": 0})
    return {
        "uid": str(post.inserted_id)
    }

#TASK ROUTES
@app.route("/get_tasks/<uid>")
def get_task(uid):
        tasks = db['tasks']
        users = db['users']
        items = tuple([k for k in tasks.find()])
        user = users.find_one({"uid": uid})
        return {
            "body": items
        }

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