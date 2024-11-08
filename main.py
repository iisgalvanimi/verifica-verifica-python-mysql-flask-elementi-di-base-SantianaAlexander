import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS DatabaseVerifica")
mycursor.execute("USE DatabaseVerifica")
mycursor.execute("CREATE TABLE Automobili (id INT PRIMARY KEY AUTO_INCREMENT , Marca VARCHAR(255), Modello VARCHAR(255), Anno INT, Tipo_carburante VARCHAR(255), Cilindrata VARCHAR(255))")
sql = "INSERT INTO Automobili (Marca, Modello, Anno, Tipo_carburante, Cilindrata) VALUES (%s, %s,%s,%s,%s)"
val = [
  ('Toyota', 'Corolla', 2023, 'Ibrida', 1800),
  ('BMW', 'Serie 3', 2022, 'Benzina', 2000),
  ('Ford', 'Mustang', 2021, 'Benzina', 5000),
  ('Tesla', 'Model 3', 2020, 'Elettrica', None), 
  ('Volkswagen', 'Golf', 2019, 'Diesel', 2000),
  ('Mercedes-Benz', 'Classe C', 2018, 'Benzina', 2000),
  ('Audi', 'A4', 2017, 'Benzina', 2000),
  ('Fiat', '500', 2016, 'Benzina', 1200),
  ('Hyundai', 'Tucson', 2015, 'Benzina', 2000),
  ('Nissan', 'Qashqai', 2014, 'Benzina', 2000)
  ]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")