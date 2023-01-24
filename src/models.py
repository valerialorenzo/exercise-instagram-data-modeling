import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    constraseña= Column (String (20), nullable=False)
    mail= Column (String (100),nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_to_id = Column (Integer, ForeignKey('usuario.id'))
    user_from_id = Column (Integer, ForeignKey('usuario.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer) 
    
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    commentText = Column(String(250), nullable=False)
    authorId = Column(Integer)
    postId = Column(Integer)
    post = relationship (Post)
    post_id = Column (Integer, ForeignKey('post.id'))
    usuario = relationship (Usuario)
    usuario_id = Column (Integer, ForeignKey('usuario.id'))
    

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String(250),nullable=False)
    postId = Column(String(250),nullable=False)
    post = relationship (Post)
    post_id = Column (Integer, ForeignKey('post.id'))


   
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
