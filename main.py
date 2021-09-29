from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
        "username": "hey",
        "uid": "fasf324",
        "tids": ["sgsg", "sf3400", "gfdb994", "234fdg"],
        "rating": 15
    }
# Hello there
#AUTHENTICATION ROUTES
@app.route("/register", methods=["POST"])
def register():
    #add code later
    return 0

@app.route("/login", methods=["POST"])
def login():
    #add code later
    return 0

@app.route("/unauth")
def unauth():
    #add code later
    return 0

#TASK ROUTES
@app.route("/get_task/<uid>")
def get_task():
    #add code later
    return 0

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
    #add code later
    return 0

#ADMIN ROUTES
@app.route("/admin/add_task", methods=["POST"])
def add_task():
    #add code later
    return 0

@app.route("/admin/delete_task/<tid>")
def delete_task():
    #add code later
    return 0

@app.route("/admin/stop_lesson")
def stop_lesson():
    #add code later
    return 0
