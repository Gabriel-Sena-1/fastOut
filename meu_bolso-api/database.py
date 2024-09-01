from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# Tabela de associação entre Gasto e Grupo
gasto_grupo = Table('gasto_grupo', Base.metadata,
    Column('id_gasto', Integer, ForeignKey('gastos.id_gasto'), primary_key=True),
    Column('id_grupo', Integer, ForeignKey('grupos.id_grupo'), primary_key=True)
)

class User(Base):
    __tablename__ = 'usuarios'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    senha = Column(String(100), nullable=False)

class Grupo(Base):
    __tablename__ = 'grupos'

    id_grupo = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    gastos = relationship('Gasto', secondary=gasto_grupo, back_populates='grupos')

class Gasto(Base):
    __tablename__ = 'gastos'

    id_gasto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.utcnow)

    grupos = relationship('Grupo', secondary=gasto_grupo, back_populates='gastos')