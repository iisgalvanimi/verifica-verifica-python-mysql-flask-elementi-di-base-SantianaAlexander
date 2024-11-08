import mysql.connector
from flask import Flask, jsonify

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DatabaseVerifica"
)
mycursor = mydb.cursor()
app = Flask(__name__)


@app.route("/")
def hello():
    return "SITO AUTOMOBILI"

@app.route('/dati', methods=['GET'])
def get_automobili():
    mycursor.execute("SELECT * FROM Automobili")
    rows = mycursor.fetchall()

    columns = [desc[0] for desc in mycursor.description]

    mammiferi_list = [dict(zip(columns, row)) for row in rows]

    return jsonify(mammiferi_list)