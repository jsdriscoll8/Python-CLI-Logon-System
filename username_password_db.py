import sqlite3

EMPLOYEE_DB_FILE = "./instance/var/db/employee.db"


# Database class for employee portal
class EmployeeDatabase:
    # Create employee table command
    CREATE_EMPLOYEE_TABLE = """CREATE TABLE IF NOT EXISTS employee_accounts (
                                username TEXT PRIMARY KEY,
                                pw_hash TEXT NOT NULL,
                                employee_role TEXT NOT NULL,
                                CONSTRAINT chk_role CHECK (employee_role IN ("ADMIN", "ENGINEER", "INTERN")));
                            """

    INSERT_DEF_VALUES = """INSERT INTO employee_accounts VALUES
                           ("jsdri", "Janu28Tw3nty24!", "ADMIN"),
                           ("jeddy", "Pr0f3550r_", "ENGINEER"),
                           ("fshman", "password", "INTERN")
                        """

    # Run the setup to create the employee
    def setup(self):
        db_connection = sqlite3.connect(EMPLOYEE_DB_FILE)
        db_cursor = db_connection.cursor()

        db_cursor.execute(self.CREATE_EMPLOYEE_TABLE)
        db_cursor.execute(self.INSERT_DEF_VALUES)

        test_results = db_cursor.execute("SELECT * FROM employee_accounts")
        print(test_results.fetchall())


# Run setup
employee_db = EmployeeDatabase()
employee_db.setup()
