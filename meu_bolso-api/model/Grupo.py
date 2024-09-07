from pydantic import BaseModel
from db.database_manager import DatabaseManager
import os

host = str(os.getenv("DB_HOST"))
db = DatabaseManager("db_container", os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_NAME"))

class GrupoBase(BaseModel):
    nome: str

class GrupoResponse(GrupoBase):
    id_grupo: int

class Grupo:
    def __init__(self, nome: str):
        self.id_grupo = None
        self.nome = nome

    def salvar(self):
        db.connect()
        if self.id_grupo is None:
            sql = "INSERT INTO grupos (nome) VALUES (%s)"
            val = (self.nome,)
            db.execute(sql, val)
            db.commit()
            self.id_grupo = db.lastrowid
        else:
            sql = "UPDATE grupos SET nome = %s WHERE id_grupo = %s"
            val = (self.nome, self.id_grupo)
            db.execute(sql, val)
            db.commit()
        db.disconnect()

    @staticmethod
    def buscar_por_id(id_grupo: int) -> GrupoResponse:
        db.connect()
        sql = "SELECT * FROM grupos WHERE id_grupo = %s"
        val = (id_grupo,)
        db.execute(sql, val)
        result = db.fetchone()
        db.disconnect()

        if result:
            grupo = GrupoResponse(
                id_grupo=result[0],
                nome=result[1]
            )
            return grupo

        return None

    @staticmethod
    def buscar_todos():
        db.connect()
        sql = "SELECT * FROM grupos"
        db.execute(sql)
        results = db.fetchall()
        db.disconnect()
        grupos = []
        for result in results:
            grupo = GrupoResponse(
                id_grupo=result[0],
                nome=result[1]
            )
            grupos.append(grupo)
        return grupos

    def atualizar(self):
        if self.id_grupo is not None:
            db.connect()
            sql = "UPDATE grupos SET nome = %s WHERE id_grupo = %s"
            val = (self.nome, self.id_grupo)
            db.execute(sql, val)
            db.commit()
            db.disconnect()

    def deletar(self):
        if self.id_grupo is not None:
            db.connect()
            sql = "DELETE FROM grupos WHERE id_grupo = %s"
            val = (self.id_grupo,)
            db.execute(sql, val)
            db.commit()
            db.disconnect()
            self.id_grupo = None

    @staticmethod
    def associar_usuario(id_grupo: int, id_user: int):
        db.connect()
        sql = "INSERT INTO usuario_grupo (id_user, id_grupo) VALUES (%s, %s)"
        val = (id_user, id_grupo)
        db.execute(sql, val)
        db.commit()
        db.disconnect()

    @staticmethod
    def remover_associacao_usuario(id_grupo: int, id_user: int):
        db.connect()
        sql = "DELETE FROM usuario_grupo WHERE id_user = %s AND id_grupo = %s"
        val = (id_user, id_grupo)
        db.execute(sql, val)
        db.commit()
        db.disconnect()

    @staticmethod
    def buscar_usuarios_associados(id_grupo: int):
        db.connect()
        sql = """
        SELECT u.id_user, u.nome, u.sobrenome, u.email
        FROM usuarios u
        INNER JOIN usuario_grupo ug ON u.id_user = ug.id_user
        WHERE ug.id_grupo = %s
        """
        val = (id_grupo,)
        db.execute(sql, val)
        results = db.fetchall()
        db.disconnect()
        usuarios = [{"id_user": row[0], "nome": row[1], "sobrenome": row[2], "email": row[3]} for row in results]
        return usuarios

    