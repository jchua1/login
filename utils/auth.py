import csv, hashlib

def hash(password):
    return hashlib.sha512(password).hexdigest()

def checkUser(user):
    r = csv.reader(open("data/users.csv"))
    for row in r:
        if row[0] == user:
            return row[1]
    return ""

def register(user, password):
    if checkUser(user) != "":
        return "User already exists."
    else:
        w = csv.writer(open("data/users.csv", "a"))
        w.writerow([user, hash(password)])
        return "Registration successful."

def authenticate(user, password):
    if checkUser(user) == "":
        return "User does not exist."
    elif checkUser(user) != hash(password):
        return "Incorrect password."
    else:
        return "Login successful."
        
    
