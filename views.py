from flask import Blueprint, render_template, request, redirect, url_for
import csv
views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index_work.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Handle form submission
        email = request.form.get("email")
        password = request.form.get("password")
        # Perform login authentication here
        # Password validation
        if email == "mattkilp5@gmail.com" and password == "matt":
            return "Login successful"  # Indicate successful login
        else:
            return "Invalid email or password"  # You can customize this response

    else:
        # Render login page for GET request
        return render_template("login.html")
    