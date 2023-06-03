from addfilms import *
from readfilms import *
from updatefilms import *
from deletefilms import *
from ReportMenu import *
import time


def menu():
    options = 0
    optionsList = ["1","2","3","4","5","6"]
    userOptions = "\nFilm Menu Options\n1. View Movie Title. \n2. Add New Movie. \n3. Edit Movie. \n4. Delete Movie. \n5. Film Reports. \n6. Exit."
    while options not in optionsList:
        print(userOptions)
        options = input("\nPlease Enter your Option: ")
        if options not in optionsList:
            time.sleep(1)
            print(f"\nYou selected a wrong option:{options}")
    return options


def reportMenu():
    options = 0
    optionsList = ["1","2","3","4","5"]
    userOptions = "\nFilm Reports\n\n1. Print film details \n2. Genre Details \n3. YearReleased \n4. Rating \n5. Exit"
    while options not in optionsList:
        print(userOptions)
        options = input("\nPlease Enter your Option: ")
        if options not in optionsList:
            print(f"\nYou selected a wrong option:{options}") 
    return options



mainProgram = True
while mainProgram:
    mainoptions = menu()
    if mainoptions == "1":
        time.sleep(1)
        readfilms()
    elif mainoptions == "2":
        time.sleep(1)
        insertfilms()
    elif mainoptions == "3":
        time.sleep(1)
        updatefilms()
    elif mainoptions == "4":
        time.sleep(1)
        deletefilms()
    elif mainoptions == "5":
        reportsProgram = True
        while reportsProgram:
            reportOptions = reportMenu()
            if reportOptions == "1":
               printAll()
            elif reportOptions == "2":
               genreDetails()
            elif reportOptions == "3":
               yearRelease()
            elif reportOptions == "4":
               rating()
            else:
                reportsProgram = False
                print("\nEnter to Exit to Main Menu")
                
                print("\nYou're about to Exit ")
                time.sleep(1)
                print("\nThank you\n")

    else:
        if mainoptions <="0" or mainoptions >="7":
            print("\nEnter 6 to Exit")
        else:
            mainProgram = False  
            time.sleep(2)
            print("\nYou're about to Exit")
            time.sleep(1)
            print("\nThank you")


