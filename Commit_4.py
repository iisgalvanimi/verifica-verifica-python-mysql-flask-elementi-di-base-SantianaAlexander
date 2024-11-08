#COMMIT 4
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

errore = True
while errore:
    mycursor = mydb.cursor()
    mycursor.execute("USE DatabaseVerifica")
    rispId = input("Inserisci l'ID dell' automobile che vuoi eliminare: ")
    sql = "SELECT EXISTS(SELECT 1 FROM Automobili WHERE id = %s)"
    mycursor.execute(sql, (rispId,))
    exists = mycursor.fetchone()[0] 
    if not exists:
        print(f"L'ID {rispId} non è presente nel database. Riprova: ")
    else:
        delete_query = "DELETE FROM Automobili WHERE id = %s"
        mycursor.execute(delete_query, (rispId,))
        mydb.commit()
        errore = False
