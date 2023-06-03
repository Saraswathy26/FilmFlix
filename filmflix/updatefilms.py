from filmconnect import *
from readfilms import *
import time

def updatefilms():
    idField = input("\nEnter filmID of the film to be updated: ")
    fieldName = input("\nEnter the Title/YearReleased/Rating/Duration/Genre as fieldName:  ").title()
    newFieldValue = input(f"\nEnter the value for the {fieldName}: ")
    print(newFieldValue)

    newFieldValue = "'" + newFieldValue + "'"
    print(newFieldValue)

    cursor.execute(f"\nupdate tblfilms set {fieldName} = {newFieldValue} where filmID = {idField} ")
    conn.commit()
    print(f"\nRecord {idField} updated in the tblfilms table")
    time.sleep(3)

    readfilms()

if __name__ == "__main__":
    updatefilms()
