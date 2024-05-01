import sqlite3

EMPLOYEE_DB_FILE = "./instance/var/db/employee.db"
PERMS_COL = 2


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
                           ("jsdri", "Janu28Tw3nty24!", "ADMIN"),
                           ("jeddy", "Pr0f3550r_", "ENGINEER"),
                           ("fshman", "password", "INTERN")
                        """

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
    def employee_query(self, username, password):
        # Connect to the database; create cursor; set up query
        db_connection = sqlite3.connect(EMPLOYEE_DB_FILE)
        db_cursor = db_connection.cursor()
        query = ("SELECT * FROM employee_accounts "
                 "WHERE username = ? AND pw_hash = ?")

        # Parameterize, execute query.
        account = db_cursor.execute(query, (username, password)).fetchall()

        # Close cursor, connection
        db_cursor.close()
        db_connection.close()

        # Return true if this username & password exist.
        if len(account) == 0:
            return False
        return account[0][PERMS_COL]



employee_db = EmployeeDatabase()
# Run setup employee_db.setup()
