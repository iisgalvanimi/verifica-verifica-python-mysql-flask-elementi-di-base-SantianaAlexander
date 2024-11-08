#COMMIT 5
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

mycursor = mydb.cursor()
try:
    selectParticolare = int(input("Qual è l'anno di cui vuoi vedere le automobili?: "))
    mycursor.execute("USE DatabaseVerifica")
    sql = "SELECT * FROM Automobili  WHERE Anno = %s"
    mycursor.execute(sql, (selectParticolare,))
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
except ValueError:
    print("Errore: Valore non valido. Rirpova")


