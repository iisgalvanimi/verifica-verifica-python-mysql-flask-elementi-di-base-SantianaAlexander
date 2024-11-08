#COMMIT 5
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)

mycursor = mydb.cursor()
mycursor.execute("USE DatabaseVerifica")
rispId = input("Inserisci l'ID dell'automobile che vuoi modificare ")
print("""
1) MODIFICARE LA MARCA
2) MODIFICARE IL MODELLO
3) MODIFICARE L'ANNO
4) MODIFICARE IL TIPO DI CARBURANTE
5) MODIFICARE LA CILINDRATA
""")
inp = int(input()) 

if inp == 1:
    Nuova_marca = input("Inserisci la nuova marca: ")
    update_query = """
    UPDATE Automobili 
    SET Marca = %s 
    WHERE id = %s
    """
    valori = (Nuova_marca, rispId)
    mycursor.execute(update_query, valori)
    mydb.commit()
elif inp == 2:
    Nuovo_modello = input("Inserisci il nuovo modello: ")
    update_query = """
    UPDATE Automobili 
    SET Modello = %s 
    WHERE id = %s
    """
    valori = (Nuovo_modello, rispId)
    mycursor.execute(update_query, valori)
    mydb.commit()
elif inp == 3:
    Nuovo_anno = int(input("Inserisci il nuovo anno: "))
    update_query = """
    UPDATE Automobili 
    SET Anno = %s 
    WHERE id = %s
    """
    valori = (Nuovo_anno, rispId)
    mycursor.execute(update_query, valori)
    mydb.commit()
elif inp == 4:
    Nuovo_tipocarburante = input("Inserisci il nuovo tipo di carburante: ")
    update_query = """
    UPDATE Automobili 
    SET Tipo_carburante = %s 
    WHERE id = %s
    """
    valori = (Nuovo_tipocarburante, rispId)
    mycursor.execute(update_query, valori)
    mydb.commit()
elif inp == 5:
    Nuova_cilindrata = input("Inserisci la nuova cilindrata: ")
    update_query = """
    UPDATE Automobili 
    SET Cilindrata = %s 
    WHERE id = %s
    """
    valori = (Nuova_cilindrata, rispId)
    mycursor.execute(update_query, valori)
    mydb.commit()
