from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index_work.html")

@views.route("/login", methods=["GET", "POST"])
def login():
    correct_length = False
    has_upper = False
    has_lower = False
    has_digit = False
    if request.method == "POST":
        # Handle form submission
        email = request.form.get("email")
        password = request.form.get("password")
        # Perform login authentication here
        while(correct_length == False or has_upper == False or has_lower == False or has_digit == False):
            if len(password() > 7):
                correct_length = True
            elif email == "mattkilp5@gmail.com" and password == "mattkilp5@gmail.com":
                return "Logged in successfully"  # You can customize this response
            else:
                return "Invalid email or password"  # You can customize this response
            for each_character in password:
                if each_character.isdigit():
                    has_digit = True
                elif each_character.islower():
                    has_lower = True
                elif each_character.isupper():
                    has_upper = True
        return "Logged in successfully"  # You can customize this response
    else:
        # Render login page for GET request
        return render_template("login.html")
