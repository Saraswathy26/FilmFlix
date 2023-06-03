from filmconnect import*

def readfilms():
    cursor.execute("\nselect * from tblfilms\n")
    records = cursor.fetchall()
    for arecord in records:
        print(arecord)

    # cursor.execute("select title from tblfilms")
    # records = cursor.fetchall()
    # for arecord in records:
    #     print(arecord)
    
    # genreField = input("Enter genre to display: ").title()
    # cursor.execute("select * from tblfilms where genre = 'genreField'")
    # records = cursor.fetchall()
    # for arecord in records:
    #     print(arecord)
    
    # cursor.execute("select rating from tblfilms")
    # records = cursor.fetchall()
    # for arecord in records:
    #     print(arecord)


if __name__ == "__main__":
    readfilms()