import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "softwares"
)

# cursorObject = database.cursor()
# cursorObject.execute("CREATE DATABASE softwares")
# print("SOFTWAREs  database is created")
cursorObject = database.cursor()

studentRecord = """
    CREATE TABLE EMPLOYEE(
    ID INT NOT NULL,
    NAME VARCHAR(60) NOT NULL,
    AGE INT NOT NULL,
    ADDRESS VARCHAR(60) NOT NULL,
    SALARY DOUBLE NOT NULL,
    PRIMARY KEY(ID)
    );"""

cursorObject.execute(studentRecord)

database.close()
print("Employee table  is creates in the database")