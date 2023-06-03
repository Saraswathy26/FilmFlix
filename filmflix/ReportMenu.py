from filmconnect import *
from readfilms import *
import time



    
def printAll():
    cursor.execute(f"\nselect * from tblfilms")  
    records = cursor.fetchall()
    for arecord in records:
        print(arecord)    
def genreDetails():
    genreField = input("\nEnter the Genre to display: ").title()
    genreField = "'" + genreField + "'"
    print(f"\nYou Selected {genreField} as Genre\n")
    time.sleep(1)
    cursor.execute(f"\nselect * from tblfilms where Genre = {genreField}")
    records = cursor.fetchall()
    for arecord in records:
        print(arecord)
def yearRelease():    
    yearField = input("\nEnter the Year to display: ").title()
    yearField = "'" + yearField + "'"
    print(f"\nFilms Released in {yearField} is displayed Below\n")
    time.sleep(1)
    cursor.execute(f"\nselect * from tblfilms where YearReleased = {yearField}")         
    records = cursor.fetchall()
    for arecord in records:
        print(arecord)
def rating():
    ratingField = input("\nEnter the Rating of the Film to display: ").title()
    ratingField = "'" + ratingField + "'"
    print(f"\nFilms under Rating {ratingField} is displayed Below\n")
    time.sleep(1)
    cursor.execute(f"\nselect * from tblfilms where Rating = {ratingField}")  
    records = cursor.fetchall()
    for arecord in records:
        print(arecord) 
    
        

if __name__ == "__main__":
    printAll()
    genreDetails()
    yearRelease()
    rating()

