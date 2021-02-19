from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select

engine = create_engine('sqlite:///melembra.db', echo=True)
db_session =scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()



class Usuarios(Base):
    __tablename__ = 'usuarios'    
    login = Column(String(50), primary_key=True, index=True)    
    senha = Column(String(10))

    def __repr__(self):
        return '<Usuário {}>'.format(self.login)
    def save(self):
        db_session.add(self)
        db_session.commit()
    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Lembretes(Base):
    __tablename__ = 'lembretes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(20))
    texto = Column(String(1800))
    usuario_id = Column(Integer, ForeignKey('usuarios.login'))
    usuario = relationship("Usuarios")
    
    def __repr__(self):
        return '<Lembretes {}>'.format(self.titulo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()
        
def init_db():
    Base.metadata.create_all(bind=engine)

# if __name__ == '__main__':
#     init_db()