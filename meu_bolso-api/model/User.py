import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

class User:
    def __init__(self, nome, sobrenome, email, senha):
        self.id_user = None  # Será definido pelo banco de dados
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"User(id={self.id_user}, nome={self.nome}, sobrenome={self.sobrenome}, email={self.email})"
    
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")