from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Perfil(Base):
	__tablename__ = 'perfil'
	id = Column(Integer, Sequence('perfil_id_seq'), primary_key=True)
	nome = Column(String(255))
	abreviacao = Column(String(3))
	disciplina = relationship('Disciplina', back_populates = 'perfil')
	docente = relationship('Docente', back_populates = 'perfil')

	def __repr__(self):
		return "<Perfil(nome='%s', abreviacao='%s'>" % (self.nome, self.abreviacao)
