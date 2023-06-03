from filmconnect import * 
from readfilms import *
import time

def deletefilms():
    #idField = input("\nEnter the filmID of the record to be deleted: ")
    
    #cursor.execute(f"\ndelete from tblfilms where filmID = {idField}")
    cursor.execute("drop TABLE tblfilms")
    conn.commit()
    #print(f"\nRecord {idField}: deleted from the tblfilms table")
    time.sleep(4)

    readfilms()

if __name__ == "__main__":
    deletefilms()

