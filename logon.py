import linecache
import employee
import username_password_db
from flask import Flask, render_template, request, redirect, url_for, flash

# Flask app
app = Flask(__name__)
app.secret_key = "al;ksjdflak;sdhnasdclbaeupqo2erhpq2o3854"


# Main logon route
@app.route("/", methods=['GET', 'POST'])
def main_login_screen():
    error = None
    # Username, password input handling
    if request.method == "POST":
        # Get input username & password; create database connection
        input_username = request.form['username']
        input_password = request.form['password']
        db_connect = username_password_db.EmployeeDatabase()

        # If the user exists, take them to the page corresponding to their permissions.
        # Otherwise, flash a message indicating they have mis-input their password.
        if db_connect.employee_query(input_username, input_password) == "ADMIN":
            return redirect(url_for("admin_logged_on"))
        else:
            error = "Invalid username or password!"
    return render_template("login_screen.html", error=error)


@app.route("/admin_logged_on")
def admin_logged_on():
    return render_template("admin_logged_on.html")


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
