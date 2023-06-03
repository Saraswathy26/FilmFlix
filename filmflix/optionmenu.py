from readfilms import * 
import time
import tkinter as tk


class window:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master)

        self.values = ["Title", "YearReleased", "Rating", "Duration", "Genre"]
        self.var = tk.StringVar(value = self.values[0])

        self.menu = tk.OptionMenu(self.frame, self.var, *self.values, command = self.optionsmenu)
        self.menu.pack(padx = 50,pady = 50)

        self.frame.pack()



    def optionsmenu(self,value):
        while value != self.values:
             if value == self.values[0]:
                 cursor.execute("select title from tblfilms")
                 records = cursor.fetchall()
                 for arecord in records:
                     print(arecord)
   
             elif value == self.value[1]:
                  cursor.execute("select YearReleased from tblfilms")
                  records = cursor.fetchall()
                  for arecord in records:
                      value = arecord
                      print(arecord)       
   
             elif value == self.value[2]:
                 cursor.execute("select Rating from tblfilms")
                 records = cursor.fetchall()
                 for arecord in records:
                     value = arecord
                     print(arecord)       
             elif value == self.value[3]:
                 cursor.execute("select Duration from tblfilms")
                 records = cursor.fetchall()
                 for arecord in records:
                     value = arecord
                     print(arecord)
             elif value == self.value[4]:
                 cursor.execute("select Genre from tblfilms")
                 records = cursor.fetchall()
                 for arecord in records:
                     value = arecord
                     print(arecord)
    
        return value
        


root = tk.Tk()
root.geometry('200x150')
window = window(root)
root.mainloop()