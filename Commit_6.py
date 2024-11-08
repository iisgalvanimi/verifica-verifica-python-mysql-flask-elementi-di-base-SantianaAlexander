#COMMIT 2
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)


mycursor = mydb.cursor()

print("""
1) INSERIRE UNA NUOVA AUTOMOBILE
2) ESTRARRE I DATI DAL DB
3) ELIMINARE I DATI DAL DB (specificanfo ID)
4) ESTRARRE I DATI DAL DB CON SELECT PARTICOLARE
""")
inp = int(input())
if inp == 1:
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
    mycursor.execute("SELECT * FROM Automobili")
elif inp == 2:
    mycursor.execute("SELECT * FROM Automobili")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

elif inp == 3:
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
elif inp == 4:
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