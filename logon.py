import linecache
import employee

# Global constant definitions
ROLE_COL_POS = 0
USERNAME_COL_POS = 1
PASSWORD_COL_POS = 2
FILE_START = 0


# Main logon program.
def main():
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


if __name__ == '__main__':
    main()
