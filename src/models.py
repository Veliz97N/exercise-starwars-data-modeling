import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre= Column(String)
    Estatura = Column(Integer)
    Peso = Column(Integer)
    Color_Pelo = Column(String)
    color_piel = Column(String)
    planeta_id = Column(Integer, ForeignKey('planeta.id'))

    Personaje_pelicula = relationship("Film",secondary=character_film)
    Personaje_especie = relationship("Specie",secondary=character_specie)
    

class Planeta(Base):
    __tablename__ = 'planeta'
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
    
    Caracteres = relationship('personaje')

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    Creado = Column(Date)
    Actualizado = Column(Date)
    Nombre_usuario = Column(String)
    Correo = Column(String)
    Contraseña = Column(String)
    Personajes_favoritos = relationship("Personaje",secondary=user_character_favorites)
    Planetas_favoritos = relationship("Planeta",secondary=user_character_favorites)
    

user_character_favorites = Table('user_character_favorites', Base.metadata,
    Column('id_usuario', ForeignKey('usuario.id'), nullable=False),
    Column('id_personaje', ForeignKey('personaje.id'), nullable=False)
)

user_planet_favorites = Table('user_planet_favorites', Base.metadata,
    Column('user_id', ForeignKey('user.id'), nullable=False),
    Column('planet_id', ForeignKey('planet.id'), nullable=False)
)

class Pelicula(Base):
    __tablename__ = 'peliculas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    director = Column(String)
    productor = Column(String)
    pelicula_nave = relationship("Starship",secondary=film_starship)
    pelicula_vehiculo = relationship("Vehicle",secondary=film_vehicle)
    # and some others ... :P

class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    modelo = Column(String)
    pasajeros = Column(Integer)
    largo = Column(Float)
    # and some others ... :P

class Nave(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    modelo = Column(String)
    pasajeros = Column(Numeric)
    largo = Column(Numeric)
    # and some others ... :P

class Especie(Base):
    __tablename__ = 'especies'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    lenguaje = Column(String)
    designacion = Column(String)
    color_ojos = Column(String)
    homeworld = relationship('Planeta', back_populates="species")
    # and some others ... :P



character_film = Table('character_film', Base.metadata,
    Column('character_id', ForeignKey('character.id'), nullable=False),
    Column('film_id', ForeignKey('film.id'), nullable=False)
)

film_starship = Table('film_starship', Base.metadata,
    Column('film_id', ForeignKey('film.id'), nullable=False),
    Column('starship_id', ForeignKey('starship.id'), nullable=False)
)

film_vehicle = Table('film_vehicle', Base.metadata,
    Column('film_id', ForeignKey('film.id'), nullable=False),
    Column('vehicle_id', ForeignKey('vehicle.id'), nullable=False)
)

character_specie = Table('character_specie', Base.metadata,
    Column('character_id', ForeignKey('character.id'), nullable=False),
    Column('specie_id', ForeignKey('specie.id'), nullable=False)
)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')