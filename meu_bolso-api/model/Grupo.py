import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

class Grupo:
    def __init__(self, nome):
        self.id_grupo = None  # Será definido pelo banco de dados
        self.nome = nome

    def __str__(self):
        return f"Grupo(id={self.id_grupo}, nome={self.nome})"
    



mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")