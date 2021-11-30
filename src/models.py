import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table, Numeric, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

personaje_pelicula = Table('personaje_pelicula', Base.metadata,
    Column('personaje_id', ForeignKey('personajes.id'), nullable=False),
    Column('pelicula_id', ForeignKey('peliculas.id'), nullable=False)
)
personaje_especie = Table('personaje_especie', Base.metadata,
    Column('personaje_id', ForeignKey('personajes.id'), nullable=False),
    Column('especie_id', ForeignKey('especies.id'), nullable=False)
)

pelicula_nave = Table('pelicula_nave', Base.metadata,
    Column('pelicula_id', ForeignKey('peliculas.id'), nullable=False),
    Column('nave_id', ForeignKey('naves.id'), nullable=False)
)

pelicula_vehiculo = Table('pelicula_vehiculo', Base.metadata,
    Column('pelicula_id', ForeignKey('peliculas.id'), nullable=False),
    Column('vehiculo_id', ForeignKey('vehiculos.id'), nullable=False)
)


usuario_personajes_favoritos = Table('usuario_personajes_favoritos', Base.metadata,
    Column('usuario_id', ForeignKey('usuarios.id'), nullable=False),
    Column('personaje_id', ForeignKey('personajes.id'), nullable=False)
)

usuario_planetas_favoritos = Table('usuario_planetas_favoritos', Base.metadata,
    Column('usuario_id', ForeignKey('usuarios.id'), nullable=False),
    Column('planeta_id', ForeignKey('planetas.id'), nullable=False)
)


class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre= Column(String)
    Estatura = Column(Integer)
    Peso = Column(Integer)
    Color_Pelo = Column(String)
    color_piel = Column(String)
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    planeta = relationship("Planeta")
    Personaje_pelicula = relationship("Pelicula",secondary=personaje_pelicula)
    Personaje_especie = relationship("Especie",secondary=personaje_especie)
    

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    Creado = Column(Date)
    Nombre = Column(String)
    Clima = Column(String)
    Diametro = Column(Numeric)
    Gravedad = Column(Numeric)
    Periodo_orbita = Column(Numeric)
    Poblacion = Column(Integer)
    Periodo_rotacion = Column(Numeric)
    Superficie_agua = Column(Numeric)
    Terreno = Column(String)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    Creado = Column(Date)
    Actualizado = Column(Date)
    Nombre_usuario = Column(String)
    Correo = Column(String)
    Contraseña = Column(String)
    Personajes_favoritos = relationship("Personaje",secondary=usuario_personajes_favoritos)
    Planetas_favoritos = relationship("Planeta",secondary=usuario_planetas_favoritos)
    

class Pelicula(Base):
    __tablename__ = 'peliculas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    director = Column(String)
    productor = Column(String)
    pelicula_nave = relationship("Nave",secondary=pelicula_nave)
    pelicula_vehiculo = relationship("Vehiculo",secondary=pelicula_vehiculo)
    

class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    modelo = Column(String)
    pasajeros = Column(Integer)
    largo = Column(Float)

class Nave(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    modelo = Column(String)
    pasajeros = Column(Numeric)
    largo = Column(Numeric)

class Especie(Base):
    __tablename__ = 'especies'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    lenguaje = Column(String)
    designacion = Column(String)
    color_ojos = Column(String)
    homeworld = relationship('Planeta', back_populates="especies")






## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')