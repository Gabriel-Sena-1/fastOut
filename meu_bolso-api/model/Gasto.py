# gasto.py
from datetime import datetime
from database_manager import DatabaseManager

db = DatabaseManager("localhost:8080", "db", "b7Lq!Xy29D#Wj4N", "meubolso")

class Gasto:
    def __init__(self, nome, valor, data=None):
        self.id_gasto = None
        self.nome = nome
        self.valor = valor
        self.data = data if data else datetime.now()
        self.grupos = []

    def salvar(self):
        db.connect()
        if self.id_gasto is None:
            sql = "INSERT INTO gastos (nome, valor, data) VALUES (%s, %s, %s)"
            val = (self.nome, self.valor, self.data)
            db.execute(sql, val)
            db.commit()
            self.id_gasto = db.lastrowid
        else:
            sql = "UPDATE gastos SET nome = %s, valor = %s, data = %s WHERE id_gasto = %s"
            val = (self.nome, self.valor, self.data, self.id_gasto)
            db.execute(sql, val)
            db.commit()
        db.disconnect()

    @staticmethod
    def buscar_por_id(id_gasto):
        db.connect()
        sql = "SELECT * FROM gastos WHERE id_gasto = %s"
        val = (id_gasto,)
        db.execute(sql, val)
        result = db.fetchone()
        db.disconnect()
        if result:
            gasto = Gasto(result[1], result[2], result[3])
            gasto.id_gasto = result[0]
            return gasto
        return None

    @staticmethod
    def buscar_todos():
        db.connect()
        sql = "SELECT * FROM gastos"
        db.execute(sql)
        results = db.fetchall()
        db.disconnect()
        gastos = []
        for result in results:
            gasto = Gasto(result[1], result[2], result[3])
            gasto.id_gasto = result[0]
            gastos.append(gasto)
        return gastos

    def atualizar(self):
        if self.id_gasto is not None:
            db.connect()
            sql = "UPDATE gastos SET nome = %s, valor = %s, data = %s WHERE id_gasto = %s"
            val = (self.nome, self.valor, self.data, self.id_gasto)
            db.execute(sql, val)
            db.commit()
            db.disconnect()

    def deletar(self):
        if self.id_gasto is not None:
            db.connect()
            sql = "DELETE FROM gastos WHERE id_gasto = %s"
            val = (self.id_gasto,)
            db.execute(sql, val)
            db.commit()
            db.disconnect()
            self.id_gasto = None

# Exemplo de uso:
# gasto = Gasto("Compras", 100.50)
# gasto.salvar()
# gasto_recuperado = Gasto.buscar_por_id(gasto.id_gasto)
# gasto.valor = 120.00
# gasto.atualizar()
# gasto.deletar()