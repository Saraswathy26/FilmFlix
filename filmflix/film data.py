from filmconnect import *
import readfilms
import time

def filmData():
    with open("filmflix/tblfilms.sql") as filmDataFile:
        sqlInsertData = filmDataFile.read()
        cursor.executescript(sqlInsertData)
        time.sleep(3)
        readfilms.readfilms()

if __name__ == "__main__":
    filmData()


