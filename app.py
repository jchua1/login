from flask import Flask, render_template, request
import hashlib
from utils import auth

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/authenticate/", methods = ["POST"])
def authenticate():
    username = request.form["username"]
    password = request.form["password"]
    m = auth.authenticate(username, password)
    return render_template("auth.html", message = m)

@app.route("/register/", methods = ["POST"])
def reg():
    username = request.form["username"]
    password = request.form["password"]
    m = auth.register(username, password)
    return render_template("auth.html", message = m)

if __name__ == "__main__":
    app.debug = True
    app.run()
