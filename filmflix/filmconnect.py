import sqlite3 as sql # import sqlite3 module
# print(dir(sql))
#create connection object
conn = sql.connect("filmflix/filmflix.db")

# create a cursor object
cursor = conn.cursor()

