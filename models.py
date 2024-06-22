from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Product(Base):
    __tablename__ = 'inventory'
    product_id = Column(Integer, primary_key=True)
    product_name = Column('product_name', String)
    product_quantity = Column('product_quantity',Integer)
    product_price = Column('product_price', Integer)
    date_updated = Column('date_updated', Date)

    def __repr__(self):
        return f'Product: {self.product_name} | Quantity: {self.product_quantity} | Price {self.product_price} | Date updated: {self.date_updated})>'
    



    
    