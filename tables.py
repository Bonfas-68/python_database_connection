import mysql.connector
import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("400x250") 
my_connect = mysql.connector.connect(
host="localhost",
user="root", 
passwd="",
database="softwares"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM employee limit 0,10")
i=0
for student in my_conn: 
    for j in range(len(student)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
        i=i+1
my_w.mainloop()