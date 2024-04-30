#!/usr/bin/python
import time
import definitions

# Startup Check
definitions.dbCheck()                                                   # checks database "credentials" exists else creates file & table
print("Initialising")
time.sleep(5)                                                           # for aesthetics

# Menu
while True:
    definitions.clear()
    print("Option Select")                                              
    print("1. Store Credentials\n2. View Credentials\n3. Exit")         # display options for user

    option = int(input("Choose an Operation: "))                        
    if option == 3:                                                     # Exit Cleanly
        definitions.exitClean()

# Operations
    if option == 1:                                                     # Store Credentials Function
        definitions.infoInput()
        print("1. Menu\n2. Exit")
        inOption = int(input("Choose an Operation: "))
        if inOption == 1:
            continue
        if inOption == 2:
            definitions.exitClean()
    elif option == 2:                                                   # View Credentials Function
        definitions.clear()
        print("Option Select")
        print("1. Forgot URI\n2. Input Department URI")
        reOption = int(input("Choose an Operation: "))
        if reOption == 1:                                               # Forgot URI Function
            definitions.clear()
            print("Please Contact your Supervisor")
            print("1. Menu\n2. Exit")
            forgOption = int(input("Choose an Operation: "))
            if forgOption == 1:
                continue
            if forgOption == 2:
                definitions.exitClean()
        if reOption == 2:                                               # Read User Info Function
            definitions.infoRead()
    else:
        definitions.clear()                                             # Failover Function
        print("Task Failed")
        input()