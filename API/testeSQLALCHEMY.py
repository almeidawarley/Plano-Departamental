from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine('mysql+pymysql://root:@localhost/planodepartamental', echo=True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	name = Column(String(255))
	fullname = Column(String(255))
	password = Column(String(255))

	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

class Address(Base):
	__tablename__ = 'addresses'
	id = Column(Integer, primary_key=True)
	email_address = Column(String(255), nullable=False)
	user_id = Column(Integer, ForeignKey('users.id'))
	user = relationship("User", back_populates="addresses")
	def __repr__(self):
		return "<Address(email_address='%s')>" % self.email_address

User.addresses = relationship("Address", order_by=Address.id, back_populates="user")

Base.metadata.create_all(engine)
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
jack.addresses = [Address(email_address='jack@google.com'),Address(email_address='j25@yahoo.com')]

session.add(ed_user)
session.add(jack)
session.commit()

for row in session.query(User).filter(User.name == 'ed').all():
	print(row.name)
