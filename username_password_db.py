import sqlite3
import hashlib
import string
import random

# Constant definitions
EMPLOYEE_DB_FILE = "./instance/var/db/employee.db"
PW_COL = 1
PERMS_COL = 2
SALT_LENGTH = 40
DEFAULT_PERMS = "INTERN"


# Database class for employee portal
class EmployeeDatabase:
    # Create employee table command
    CREATE_EMPLOYEE_TABLE = """
                                CREATE TABLE IF NOT EXISTS employee_accounts (
                                username TEXT PRIMARY KEY,
                                pw_hash TEXT NOT NULL,
                                employee_role TEXT NOT NULL,
                                CONSTRAINT chk_role CHECK (employee_role IN ("ADMIN", "ENGINEER", "INTERN")));
                            """

    INSERT_DEF_VALUES = """
                           INSERT INTO employee_accounts VALUES
                           ("jsdri", "DqPxdKU1S1fnpkWgZopBdhgujhqFYVaYMFgm95DC2b34ed7d0626395a93d4a2050d71060468deb7e4", "ADMIN"),
                           ("jeddy", "tWPoPE75pjiFNKG5Xsh4GSX5HxI2pu5fMdvPlQ6W29257cb4f28083aa289a132712b3f547078e6d78", "ENGINEER"),
                           ("fshman", "6IKN44WsbrrIOubU1kbYPzBO8555VsNEPrh6FBHHf0e83429212632df4385ae734fac0a580d9e01bb", "INTERN")
                        """

    # Generate the hashed version of a password
    def hash_pw(self, plain_text) -> str:
        # Helper function: generate a random salt
        def randomword(length) -> str:
            letters_and_digits = string.ascii_letters + string.digits
            return ''.join(random.choice(letters_and_digits) for i in range(length))

        # Generate a salt, hash the password + salt, and return the salt + hashed(salt + pw)
        salt = randomword(SALT_LENGTH)
        hashable = salt + plain_text  # concatenate salt and plain_text
        hashable = hashable.encode('utf-8')  # convert to bytes
        this_hash = hashlib.sha1(hashable).hexdigest()  # hash w/ SHA-1 and hexdigest
        salted_hashed_pw = salt + this_hash
        return salted_hashed_pw

    # Authenticate an input password against the stored hash.
    def authenticate(self, stored_password: str, input_password: str) -> bool:
        # Get the stored salt & hash. Use the salt to compare the stored password to the input password.
        salt = stored_password[:SALT_LENGTH]  # extract salt from stored value
        stored_hash = stored_password[SALT_LENGTH:]  # extract hash from stored value
        hashable = salt + input_password  # concatenate hash and plain text
        hashable = hashable.encode('utf-8')  # convert to bytes
        this_hash = hashlib.sha1(hashable).hexdigest()  # hash and digest

        # Return the result of this comparison
        return this_hash == stored_hash

    # Verify a new password with all specified constrants
    def verify_password_integrity(self, password: str):
        if len(password) < 8:
            return "Password must be at least 8 characters."
        if len(password) > 25:
            return "Password must be no longer than 25 characters."
        lowers = [c for c in password if c.islower()]
        if len(lowers) == 0:
            return "Password must contain a lowercase letter."
        uppers = [c for c in password if c.isupper()]
        if len(uppers) == 0:
            return "Password must contain an uppercase letter."
        digits = [c for c in password if c.isnumeric()]
        if len(digits) == 0:
            return "Password must contain a number."
        special_chars = [c for c in password if c in string.punctuation]
        if len(special_chars) == 0:
            return "Password must contain a special character."
        return None

    # Add a new user to the system, if this user does not already exist.
    def add_new_user(self, new_username, new_password):
        # Verify password integrity
        password_message = self.verify_password_integrity(new_password)
        if password_message is not None:
            return password_message

        # Connect to db, build lookup query.
        db_connection = sqlite3.connect(EMPLOYEE_DB_FILE)
        db_cursor = db_connection.cursor()
        query = ("SELECT * FROM employee_accounts "
                 "WHERE username = ?")

        # Parameterize, execute lookup query. If this query is not empty, the user already exists - abort.
        account = db_cursor.execute(query, (new_username,)).fetchall()
        if len(account) != 0:
            db_cursor.close()
            db_connection.close()
            return "User already exists!"

        # Otherwise, build the insert query and insert the new username & hashed password.
        hashed_password = self.hash_pw(new_password)
        insert_user_query = ("INSERT INTO employee_accounts "
                             "VALUES (?, ?, ?);")
        db_cursor.execute(insert_user_query, (new_username, hashed_password, DEFAULT_PERMS))

        # Commit the new account, return a success message.
        db_cursor.close()
        db_connection.commit()
        db_connection.close()
        return "Successfully added new user!"

    # Run the setup to create the employee table
    def setup(self) -> None:
        # Connect to the database; create cursor
        db_connection = sqlite3.connect(EMPLOYEE_DB_FILE)
        db_cursor = db_connection.cursor()

        # Destroy, re-create employee table & insert default values
        db_cursor.execute("DROP TABLE IF EXISTS employee_accounts")
        db_cursor.execute(self.CREATE_EMPLOYEE_TABLE)
        db_cursor.execute(self.INSERT_DEF_VALUES)

        # Test proper functionality - get default values & print back
        test_results = db_cursor.execute("SELECT * FROM employee_accounts")
        print(test_results.fetchall())

        # Close the cursor; commit changes & close connection
        db_cursor.close()
        db_connection.commit()
        db_connection.close()

    # Perform a parameterized query on the database.
    # If this user exists, return their permissions; otherwise return False
    def employee_query(self, username: str, input_password: str):
        # Connect to the database; create cursor; set up query
        db_connection = sqlite3.connect(EMPLOYEE_DB_FILE)
        db_cursor = db_connection.cursor()
        query = ("SELECT * FROM employee_accounts "
                 "WHERE username = ?")

        # Parameterize, execute query. If there are no results, the account does not exist.
        account = db_cursor.execute(query, (username,)).fetchall()
        if len(account) == 0:
            return False

        # Otherwise, get the hashed password.
        hashed_password = account[0][PW_COL]

        # Close cursor, connection
        db_cursor.close()
        db_connection.close()

        # Return false if the passwords do not match; return the user's permissions level otherwise.
        if not self.authenticate(hashed_password, input_password):
            return False
        return account[0][PERMS_COL]


employee_db = EmployeeDatabase()
# Run setup
# employee_db.setup()

print(employee_db.add_new_user("fshman44", "_45Assadfs!"))
