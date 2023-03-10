import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "softwares")
mycursor = mydb.cursor()
mycursor.execute("Select * from employee")
# for i in mycursor:
#     print(i)
###########################
# bonfas = mycursor.fetchall()
# for i in bonfas:
#     print(i)
############################
bonfas = mycursor.fetchone()
for i in bonfas:
    print(i)
    