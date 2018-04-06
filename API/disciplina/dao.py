from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Disciplina(Base):
	__tablename__ = 'disciplina'
	id = Column(Integer, Sequence('disciplina_id_seq'), primary_key=True)
	codigo = Column(String(6))
	nome = Column(String(255))
	chTeorica = Column(Integer)
	chPratica = Column(Integer)
	perfil = relationship('Perfil', back_populates = 'disciplina')

	def __repr__(self):
		return "<Disciplina(codigo='%s', nome='%s', chTeorica='%d', chPratica='%d')>" % (self.codigo, self.nome, self.chTeorica, self.chPratica)
