from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Docente(Base):
    __tablename__ = 'docente'
    id = Column(Integer, Sequence('docente_id_seq'), primary_key=True)
    nome = Column(String(255))
    sobrenome = Column(String(255))
    creditos = Column(Integer)
    perfil = relationship('Perfil', back_populates='docente')

    def __repr__(self):
        return "<Docente(nome='%s', sobrenome='%s', creditos='%d'>" % (self.nome, self.sobrenome, self.creditos)
