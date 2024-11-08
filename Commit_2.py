#COMMIT 2
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Automobili")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)