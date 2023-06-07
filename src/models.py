import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False,  unique=True)
    email = Column(String(50), nullable=False)
    password = Column(String(30), nullable=False)
    

class Perfil(Base):
    __tablename__ = 'perfil'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable= False)
    last_name= Column(String(50), nullable= False)
    phone=Column(String(30), nullable= True)
    edad=Column(Integer, nullable= False)
    state=Column(String(20), nullable= False)
    country=Column(String(20), nullable= False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)

class Talent(Base):
    __tablename__='talent'
    id=Column(Integer, primary_key=True)
    name= Column(String(100), nullable= True)
    since=Column(Integer, nullable= True)
    about_you=Column(Integer, nullable= True)
    perfil_id = Column(Integer, ForeignKey('perfil.id'))
    perfil = relationship(Perfil)

class Categories(Base):
    __tablename__='categories'
    id=Column(Integer, primary_key= True)
    name=Column(String(100), nullable= False)
    talent_id = Column(Integer, ForeignKey('talent.id'))
    talent = relationship(Talent)

class Talent_Request(Base):
    __tablename__='talent_request'
    id=Column(Integer, primary_key= True)
    request=Column(Boolean, default= False)
    usuario_id=Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    perfil_id = Column(Integer, ForeignKey('perfil.id'))
    perfil = relationship(Perfil)

def request_response(invitacion):
    if invitacion:
        return "sí"
    else:
        return "no"

class Talent_Search(Base):
    __tablename__='talent_search'
    id=Column(Integer, primary_key= True)
    card=Column(String(100), nullable=False)
    usuario_id=Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)
    perfil_id = Column(Integer, ForeignKey('perfil.id'))
    perfil = relationship(Perfil)
    talent_id = Column(Integer, ForeignKey('talent.id'))
    talent = relationship(Talent)
    categories_id=Column(Integer, ForeignKey('categories.id'))
    categoies = relationship(Categories)

# class Personaje(Base):
#     __tablename__ = 'personaje'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable= False)
#     descripcion = Column(String(150), nullable=False)

# class Favorito(Base):
#     __tablename__ = 'Favorito'
#     id = Column(Integer, primary_key=True)
#     personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
#     personaje = relationship(Personaje)
#     planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
#     planeta = relationship(Perfil)
#     usuario_id = Column(Integer, ForeignKey('usuario.id'))
#     usuario = relationship(Usuario)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     usuario_id = Column(Integer, ForeignKey('usuario.id'))
#     usuario = relationship(Usuario)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
