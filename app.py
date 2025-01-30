import os
import functools

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = "abcd1234"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///crochet.db")
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, hashpassword TEXT NOT NULL)")
if not db.execute("SELECT * FROM users WHERE username = ?", "admin"):
    db.execute("INSERT INTO users (username, hashpassword) VALUES (?, ?)", "admin", generate_password_hash("2411"))
db.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, product TEXT NOT NULL, quantity INTEGER DEFAULT 1)")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/amigurumi")
def amigurumi():
    return render_template("amigurumi.html")

@app.route("/decor")
def decor():
    return render_template("decor.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            print("Username is required")
            flash("Username is required!", "danger")
            print("Redirecting to /login")
            return redirect("/login")
        elif not password:
            print("Password is required")
            flash("Password is required!", "danger")
            print("Redirecting to /login")
            return redirect("/login")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1 or not check_password_hash(rows[0]["hashpassword"], password):
            print("Invalid username and/or password")
            flash("Invalid username and/or password!", "danger")
            print("Redirecting to /login")
            return redirect("/login")
        session["user_id"] = rows[0]["id"]
        return redirect("/")
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            flash("Username is required!", "danger")
            return redirect("/register")
        elif db.execute("SELECT * FROM users WHERE username = ?", username):
            flash("Username already exists!", "danger")
            return redirect("/register")
        elif not password:
            flash("Password is required!", "danger")
            return redirect("/register")
        elif not request.form.get("confirmation") or password != request.form.get("confirmation"):
            flash("Passwords do not match!", "danger")
            return redirect("/register")
        db.execute("INSERT INTO users (username, hashpassword) VALUES (?, ?)", username, generate_password_hash(password))
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1:
            flash("Registration failed!", "danger")
            return redirect("/register")
        session["user_id"] = rows[0]["id"]
        flash("Registration successful!", "success")
        return redirect("/")
    else:
        return render_template("register.html")
    
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        if not request.form.get("product"):
            flash("Product is required!", "danger")
            return redirect("/buy")
        username = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0]["username"]
        db.execute("INSERT INTO orders (username, product, quantity) VALUES (?, ?, ?)", username, request.form.get("product"), request.form.get("quantity"))
        flash("Order submitted!", "success")
        return redirect("/")
    else:
        return render_template("buy.html")
    
@app.route("/orders")
@login_required 
def orders():
    orders = db.execute("SELECT * FROM orders")
    if session.get("user_id") == db.execute("SELECT id FROM users WHERE username = ?", "admin")[0]["id"]:  
        return render_template("orders.html", orders=orders)
    else:
        flash("Invalid access!", "danger")
        return redirect("/")

@app.route("/users")
@login_required
def users():
    users = db.execute("SELECT * FROM users")
    if session.get("user_id") == db.execute("SELECT id FROM users WHERE username = ?", "admin")[0]["id"]:
        return render_template("users.html", users=users)
    else:
        flash("Invalid access!", "danger")
        return redirect("/")

@app.route("/edit", methods=["GET", "POST"])
@login_required
def edit():
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        hasholdpassword = db.execute("SELECT hashpassword FROM users WHERE id = ?", session["user_id"])[0]["hashpassword"]
        if not old_password:
            flash("Old password is required!", "danger")
            return redirect("/edit")
        if not check_password_hash(hasholdpassword, old_password):
            flash("Incorrect password!", "danger")
            return redirect("/edit")
        if not new_password:
            flash("New password is required!", "danger")
            return redirect("/edit")
        if new_password != request.form.get("confirmation"):
            flash("Passwords do not match!", "danger")
            return redirect("/edit")
        hashnewpassword = generate_password_hash(new_password)
        db.execute("UPDATE users SET hashpassword = ? WHERE id = ?", hashnewpassword, session["user_id"])
        flash("Password changed!", "success")
        return redirect("/")
    else:
        return render_template("edit.html")

if __name__ == "__main__":
    print("Flask app is starting...")
    app.run()


    