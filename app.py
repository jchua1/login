from flask import Flask, render_template, request

app = Flask(__name__)
user = "jeff"
pw = "password"

@app.route("/")
@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/authenticate/", methods = ["POST"])
def auth():
    username = request.form["username"]
    password = request.form["password"]
    if (username == user and password == pw):
        return "Login successful."
    return "Login failed."

if __name__ == "__main__":
    app.debug = True
    app.run()
