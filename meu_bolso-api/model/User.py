class User:
    def __init__(self, nome, sobrenome, email, senha):
        self.id_user = None  # Será definido pelo banco de dados
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"User(id={self.id_user}, nome={self.nome}, sobrenome={self.sobrenome}, email={self.email})"