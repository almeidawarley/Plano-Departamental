from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@localhost/planodepartamental', echo=True)
Base = declarative_base()