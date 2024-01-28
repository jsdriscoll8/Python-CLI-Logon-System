# The three subclasses of Employee represent the three specified required roles:
# Admin, Engineer, and Intern.
class Employee:
    # Declare a new, default Employee.
    def __init__(self):
        self.username = "DEFAULT_USER"
        self.password = "123456"

    # Declare a new Employee with a user-defined username and password.
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Admin class: full management privileges.
class Admin(Employee):
    # Create a new, default Admin.
    def __init__(self):
        super().__init__()

    # Create a user-defined Admin.
    def __int__(self, username, password):
        super().__init__(username, password)

# Engineer class: access to project documents & personal timesheet, but not internal
# accounting or management operations.
class Engineer(Employee):
    # Create a new, default Engineer.
    def __init__(self):
        super().__init__()

    # Create a user-defined Engineer.
    def __int__(self, username, password):
        super().__init__(username, password)

# Intern class: access only to personal timesheet, not live project documents or accounting.
class Intern(Employee):
    # Create a new, default Intern.
    def __init__(self):
        super().__init__()

    # Create a user-defined Intern.
    def __int__(self, username, password):
        super().__init__(username, password)
