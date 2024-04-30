#!/usr/bin/python

import sqlite3
import os
import time

# Clean Exit
def exitClean():
    cursor.close()
    clear()
    exit()

# Password Check
def password_check(passwd):
     
    SpecialSym =['$', '@', '#', '%']
    val = True
     
    if len(passwd) < 8:
        print('length should be at least 8')
        val = False
         
    if len(passwd) > 20:
        print('length should be not be greater than 20')
        val = False
         
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
         
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
         
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
         
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

# Clear Page
def clear():
    print("\033c", end="", flush=True)

# File Locations
path = "credentials.db"

# Connect to database
conn = sqlite3.connect('credentials.db')

# Create Curser
cursor = conn.cursor() 

# Check for database file
def dbCheck():
    print("testing")
    if os.path.isfile(path):
        print(".")
        clear()
    try:
        sqlite_create_table_query = ''' CREATE TABLE credentials ( 
                                        FNAME TEXT NOT NULL, 
                                        LNAME TEXT NOT NULL, 
                                        URI TEXT NOT NULL, 
                                        PASSWORD CHAR(50) );'''
        
        cursor.execute(sqlite_create_table_query)
        print("Successfully Connected to SQLite")
        conn.commit()
        print("SQLite table created")
        conn.close()
        clear()
    except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
            clear()

# Info Input
def infoInput():
        conn
        clear()
        uri = input("Enter Company URI: ")
        clear()
        fname = input("Enter First Name: ")
        clear()
        lname = input("Enter Last Name: ")
        clear()
        passwd = input("Enter Password: ")
        if not (password_check(passwd)):
             print("Try Again")
             input()
             clear()
        else:
            try:
                clear()
                sql_insert_query = """INSERT INTO credentials (FNAME, LNAME, URI, PASSWORD) VALUES (?, ?, ?, ?);"""
                data_tuple = (fname, lname, uri, passwd)
                cursor.execute(sql_insert_query, data_tuple)
                conn.commit()
                time.sleep(3)
                print("Information Imported Successfully")
            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)

#Info Read
def infoRead():
        clear()
        uri = input("Enter Company URI: ")
        clear()
        passwd = input("Enter Password: ")
        clear()
        try:
            conn
            sql_select_query = """SELECT * from credentials where URI = ? AND PASSWORD = ?;"""
            cursor.execute(sql_select_query, (uri, passwd))
            records = cursor.fetchall()
            print("Printing for URI", uri)
            time.sleep(2)
            for row in records:
                time.sleep(0.25)
                print("First Name = ", row[0])
                time.sleep(0.25)
                print("Last Name  = ", row[1])
                time.sleep(0.25)
                print("Password  = ", row[3])
            input()
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)