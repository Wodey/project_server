from flask import Flask
from hashlib import md5
import redis
r_user = redis.StrictRedis(
    host='127.0.0.1',
    port=5000,
    password='lgqXU5Dwxs2j3sVMqvl207fWoTQclhVX',
    charset="utf-8",
    decode_responses=True
)
r_task = redis.StrictRedis(
    host='127.0.0.1',
    port=5000,
    password='wYjpWimMui3JEsbJcXSxVl8q9mtEsEly',
    charset="utf-8",
    decode_responses=True
)
r_results=redis.StrictRedis(
    host='127.0.0.1',
    port=5000,
    password='agdKAJHSJKhdhJKAK31ljDAlasQqefsn',
    charset="utf-8",
    decode_responses=True
)

app = Flask(__name__)


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
    try:
        if r_user.get(login)==None:
            r_user.set(login,md5(login.encode()).hexdigest(),300)#300 sec
        else:
            return r_user.get(login)
    except:
        return 0

@app.route("/unauth")
def unauth():
    #add code later
    return 0

#TASK ROUTES
@app.route("/get_task/<uid>")
def get_task():
    try:
        if r_task.get(uuid)==None:
        r_task.set(uuid,md5(uuid.encode()).hexdigest())
    else:
        return r_task.get(uuid)
    except:
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
    try:
        return r_results.get(f"best_result_{uuid}")
    except:
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
