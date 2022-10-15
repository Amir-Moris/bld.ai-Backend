import sqlite3

def createDataBase():
    try:
        sqliteConnection = sqlite3.connect('DataBase.db')
        cursor = sqliteConnection.cursor()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

createDataBase()

def executeQuery(sqliteQuery):
    try:
        sqliteConnection = sqlite3.connect('DataBase.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(sqliteQuery)
        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)

create_table_queries = [
    '''CREATE TABLE school (
        schoolID INT PRIMARY KEY,
        name VARCHAR(32),
        no_students INT
        );''',
    '''CREATE TABLE manager (
        ManagerID INT,
        mySchoolID INT,
        firstname VARCHAR(32),
        lastname VARCHAR(32),
        FOREIGN KEY (mySchoolID) REFERENCES school (schoolID)
        );''',
    '''CREATE TABLE class (
        classID INT PRIMARY KEY,
        mySchoolID INT,
        noStudents INT,
        FOREIGN KEY (mySchoolID) REFERENCES school (schoolID)
        );''',
    '''CREATE TABLE student (
        ID INT PRIMARY KEY,
        myClassID INT,
        firstname VARCHAR(32),
        lastname VARCHAR(32),
        age INT CHECK (age >= 18),
        CONSTRAINT name UNIQUE (firstname, lastname),
        FOREIGN KEY (myClassID) REFERENCES class (classID)
        );'''
]

for str in create_table_queries:
    executeQuery(str)