import linecache

import employee
import io

# Main logon program.
def main():
    # Open the stored users file and relay a greeting, asking the user for their username & password.
    users_file = open("users.csv", "r")
    print("Welcome to the company portal!")
    username = input("Enter your username to continue, or type 'quit' to quit: ")
    user_data_line = 0

    # Quit on user command.
    # Otherwise, look through the password file and find their logon information.
    if username != 'quit':
        user_data = None
        username_match = False

        # Search through the CSV file. Break from the search if the username is found.
        while not username_match and username != 'quit':
            user_data_line = 0
            for user_line in users_file:
                user_data_line += 1
                user_data = user_line.split(",")[1]
                if user_data == username:
                    username_match = True
                    break

            # Ask again for
            if not username_match:
                username = input("Username not found. Try again, or type 'quit' to quit: ")

    # If a valid username is entered, continue.
    if username != 'quit':
        # Get the user's role, and ask them for their password.
        user_role = linecache.getline("users.csv", user_data_line).split(",")[0]
        password = input("Please enter your password, or type 'quit' to quit: ")
        while password != 'quit' and password != linecache.getline("users.csv", user_data_line).split(",")[2].rstrip():
            password = input("Invalid password! Try again, or type 'quit' to quit: ")

        if password != 'quit':
            match user_role:
                case 'Admin':
                    admin = employee.Admin(username, password)


    # Close the file, relay a farewell.
    users_file.close()
    print("Logging off...")


if __name__ == '__main__':
    main()