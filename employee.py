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