import string
import random
import username_password_db
from flask import Flask, render_template, request, redirect, url_for, session

# Constants
app = Flask(__name__)
app.secret_key = ''
for char in range(30):
    app.secret_key += random.choice(string.ascii_lowercase)
MAX_LOGIN_ATTEMPTS = 3


# Main logon route
@app.route("/", methods=['GET', 'POST'])
def main_login_screen():
    error = None
    if 'login_attempts' not in session:
        session['login_attempts'] = 0

    # Username, password input handling
    if request.method == "POST":
        # Get input username & password; create database connection
        input_username = request.form['username']
        input_password = request.form['password']
        db_connect = username_password_db.EmployeeDatabase()

        # If the user exists, take them to the page corresponding to their permissions.
        # Otherwise, flash a message indicating they have mis-input their password.
        if session['login_attempts'] >= MAX_LOGIN_ATTEMPTS:
            return 0
        if db_connect.employee_query(input_username, input_password) == "ADMIN":
            return redirect(url_for("admin_logged_on", username=input_username))
        elif db_connect.employee_query(input_username, input_password) == "ENGINEER":
            return redirect(url_for("engineer_logged_on", username=input_username))
        elif db_connect.employee_query(input_username, input_password) == "INTERN":
            return redirect(url_for("intern_logged_on", username=input_username))
        else:
            error = "Invalid username or password!"
            session['login_attempts'] += 1
            if session['login_attempts'] == MAX_LOGIN_ATTEMPTS:
                print("Hello")
                error = "You have reached the maximum number of login attempts!"

    return render_template("login_screen.html", error=error)


# Route to new user registration page
@app.route("/employee_registration", methods=['GET', 'POST'])
def employee_registration_screen():
    message = None
    strong_password = None

    # Username, password input handling
    if request.method == "POST" and "username" in request.form:
        # Get input username & password; create database connection
        input_username = request.form['username']
        input_password = request.form['password']
        db_connect = username_password_db.EmployeeDatabase()
        message = db_connect.add_new_user(input_username, input_password)

    # Post request without username: generate strong password
    if request.method == "POST" and "generate" in request.form:
        strong_password = create_strong_password()
    return render_template("employee_registration.html", message=message, password=strong_password)


# Routes to successful logon pages
@app.route("/admin_logged_on/<username>")
def admin_logged_on(username):
    return render_template("admin_logged_on.html", username=username)


@app.route("/engineer_logged_on/<username>")
def engineer_logged_on(username):
    return render_template("engineer_logged_on.html", username=username)


@app.route("/intern_logged_on/<username>")
def intern_logged_on(username):
    return render_template("intern_logged_on.html", username=username)


# Returns a strong password of length 12
def create_strong_password():
    strong_password = ""
    loop_iterations = 3  # 3 loop iterations * 4 random characters = length 12 password

    for char in range(loop_iterations):
        # Generate a random lowercase letter, uppercase letter, digit, and special character
        rand_lowercase = random.choice(string.ascii_lowercase)
        rand_uppercase = random.choice(string.ascii_uppercase)
        rand_digit = random.choice(string.digits)
        rand_special_character = random.choice(string.punctuation)

        # Add these characters to the password, then shuffle it.
        strong_password += (rand_lowercase + rand_uppercase + rand_digit + rand_special_character)
        strong_password = ''.join(random.sample(list(strong_password), len(strong_password)))

    return strong_password


# Run the flask app
def main():
    app.run()


if __name__ == '__main__':
    main()


"""
    # Global constant definitions
    ROLE_COL_POS = 0
    USERNAME_COL_POS = 1
    PASSWORD_COL_POS = 2
    FILE_START = 0
    
    # Open the stored users file and relay a greeting, asking the user for their username & password.
    users_file = open("users.csv", "r")
    print("Welcome to the company portal!")
    username = input("Enter your username to continue, or type 'quit' to quit: ")
    user_data_line = FILE_START

    # Quit on user command.
    # Otherwise, look through the password file and find their logon information.
    if username != 'quit':
        username_match = False

        # Search through the CSV file. Break from the search if the username is found.
        while not username_match and username != 'quit':
            users_file.seek(FILE_START)
            user_data_line = FILE_START
            for user_line in users_file:
                user_data_line += 1
                user_data = user_line.split(",")[USERNAME_COL_POS]
                if user_data == username:
                    username_match = True
                    break

            # Ask again for
            if not username_match:
                username = input("Username not found. Try again, or type 'quit' to quit: ")

    # If a valid username is entered, continue.
    if username != 'quit':
        # Get the user's role, and ask them for their password.
        user_role = linecache.getline("users.csv", user_data_line).split(",")[ROLE_COL_POS]
        password = input("Please enter your password, or type 'quit' to quit: ")
        while (password != 'quit' and
               password != linecache.getline("users.csv", user_data_line).split(",")[PASSWORD_COL_POS].rstrip()):
            password = input("Invalid password! Try again, or type 'quit' to quit: ")

        # If the user wishes to proceed, continue using their assigned role and corresponding class.
        if password != 'quit':
            user = None

            # Match the user's role.
            match user_role:
                case 'Admin':
                    user = employee.Admin(username, password)
                case 'Engineer':
                    user = employee.Engineer(username, password)
                case 'Intern':
                    user = employee.Intern(username, password)
                case _:
                    print("Invalid role.")

            if user is not None:
                user.terminal()

    # Close the file, relay a farewell.
    users_file.close()
    print("Logging off...")
"""
