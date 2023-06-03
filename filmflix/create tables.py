from filmconnect import *
cursor.execute("""
create table "tblfilms" ("filmID" integer not null unique,"Title" text,
"YearReleased" integer, "Rating" text, "Duration" integer, "Genre" text,
PRIMARY KEY("filmID" autoincrement))""")