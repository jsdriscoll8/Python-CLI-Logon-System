# The three subclasses of Employee represent the three specified required roles:
# Admin, Engineer, and Intern.
class Employee:
    # Declare a new Employee.
    def __init__(self, username=None, password=None):
        if username is not None:
            self.username = username
        else:
            self.username = "DEFAULT_USER"

        if password is not None:
            self.password = password
        else:
            self.password = "PASSWORD"

    # Activate the user terminal.
    def terminal(self):
        # Provide a greeting and selections menu.
        print(f"Welcome {type(self).__name__} {self.username}...")
        print("Please provide a selection: \n"
              "\t 1. Personal timesheet \n"
              "\t 2. Project documents \n"
              "\t 3. Payroll and workforce management \n")

        # Get the menu selection.
        selection = self.__main_menu_selection()

        # Match the selection. If a user lacks the necessary privileges, rebuff and obtain another selection.
        while selection != 4:
            match selection:
                case 1:
                    print("\t Accessing personal timesheet...")
                case 2:
                    if type(self).__name__ != "Admin" and type(self).__name__ != "Engineer":
                        print("\t Access denied - Admin or Engineer privileges required.")
                    else:
                        print("\t Access granted - loading project documents...")
                case 3:
                    if type(self).__name__ != "Admin":
                        print("\t Access denied - Admin privileges required.")
                    else:
                        print("\t Access granted - loading workforce management software...")

            selection = self.__main_menu_selection()

    # Menu screen function - catches non-integer and out-of-range data.
    def __main_menu_selection(self) -> int:
        selection = 0
        while (selection < 1 or selection > 3) and selection != 4:
            try:
                selection = int(input("Enter selection here, or type 4 to quit: ").strip())
            except ValueError:
                print("Invalid selection - not an integer.")
            else:
                if selection < 1 or selection > 4:
                    print("Invalid selection - out of range")

        return selection


# Admin class: full management privileges.
class Admin(Employee):
    # Create a new, default Admin.
    def __init__(self, username=None, password=None):
        super().__init__(username, password)


# Engineer class: access to project documents & personal timesheet, but not internal
# accounting or management operations.
class Engineer(Employee):
    # Create a new Engineer.
    def __init__(self, username=None, password=None):
        super().__init__(username, password)


# Intern class: access only to personal timesheet, not live project documents or accounting.
class Intern(Employee):
    # Create a new Intern
    def __int__(self, username=None, password=None):
        super().__init__(username, password)
