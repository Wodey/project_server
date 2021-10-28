import os
from datetime import date
from db import get_db
from flask import Flask, request
from hashlib import md5
app = Flask(__name__)
from bson.objectid import ObjectId

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
    post = users.insert_one({"username": data["username"], "uncompleted_tasks": [k['_id'] for k in tasks], "score": 0})
    return {
        "uid": str(post.inserted_id)
    }

#TASK ROUTES
@app.route("/get_tasks/<uid>")
def get_tasks(uid):
        tasks = db['tasks']
        users = db['users']
        items = tuple([k for k in tasks.find()])
        user = users.find_one({"_id": ObjectId(uid)})
        result = []
        for i in items:
            for k in user["uncompleted_tasks"]:
                if(str(i["_id"]) == str(k)):
                    result.append({"body": i["body"], "result": i["result"], "uid": str(i["_id"])})
        return {
            "body": result
        }


@app.route("/deliver_task/<uid>", methods=["POST"])
def deliver_task(uid):
    data = request.get_json()
    task = db["tasks"].find_one({"_id": ObjectId(data["_id"])})
    if(task["result"] == data["result"]):
        user = db["users"].find_one_and_update({"_id": ObjectId(uid)}, {"$pull": {"uncompleted_tasks": ObjectId(data["_id"])}})
        return "0"
    return "1"

#RESULTS ROUTES
@app.route("/get_results")
def get_results():
    return 0

#ADMIN ROUTES
@app.route("/admin/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    tasks = db['tasks']
    tasks.insert_one({"body": data["body"], "result": data["result"]})
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