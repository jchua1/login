from flask import Flask, render_template, request, url_for, session, redirect
from utils import auth

app = Flask(__name__)
app.secret_key = "asdf"

@app.route("/")
@app.route("/login/")
def login():
    if "user" in session:
        return redirect(url_for("welcome"))
    return render_template("login.html")

@app.route("/register/", methods = ["POST"])
def reg():
    username = request.form["username"]
    password = request.form["password"]
    m = auth.register(username, password)
    return render_template("auth.html", message = m)

@app.route("/authenticate/", methods = ["POST"])
def authenticate():
    username = request.form["username"]
    password = request.form["password"]
    m = auth.authenticate(username, password)
    if (m == "Login successful."):
        session["user"] = username
    return render_template("auth.html", message = m)

@app.route("/welcome/")
def welcome():
    if "user" in session:
        return render_template("welcome.html", name = session["user"])
    else:
        return redirect(url_for("login"))

@app.route("/logout/")
def logout():
    session.pop("user")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.run()
