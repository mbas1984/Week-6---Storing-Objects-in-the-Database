## SqlAlchemy ASGT

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    year = Column(Integer)
    
    def __init__(self, name = None,year = None):
        self.name = name
        self.year = year
        
    def __repr__(self):
        return "Car(%r, %r)" % (self.name,self.year)


engine = create_engine('sqlite:///foo.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

c1 = Car("Lexus", 2016)
session.add(c1)

alldata = session.query(Car).all()
for somedata in alldata:
    print (somedata)








