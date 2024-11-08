#COMMIT 3
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

mycursor = mydb.cursor()

print("INSERISCI UNA NUOVA AUTOMOBILE")

Marca = input("Inserisci la marca: ")
Modello = input("Inserisci il modello: ")
Anno = int(input("Inserisci l'anno: "))
Tipo_carburante = input("Inserisci il tipo di carburante: ")
Cilindrata = input("Inserisci la cilindrata: ")
sql = "INSERT INTO Automobili (Marca, Modello, Anno, Tipo_carburante, Cilindrata) VALUES (%s, %s,%s,%s,%s)"
val = (Marca, Modello, Anno, Tipo_carburante, Cilindrata)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
