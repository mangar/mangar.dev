from app import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True, index=True)
    uuid = db.Column(db.String)
    account_no = db.Column(db.String)
    name = db.Column(db.String)
    address = db.Column(db.String)
    country = db.Column(db.String)
    email = db.Column(db.String)
    date_birth = db.Column(db.DateTime)
    # orders = relationship("Order")

    def __repr__(self):
        return f"<User {self.uuid} - {self.name}>"




# from sqlalchemy import Column
# from sqlalchemy import ForeignKey
# from sqlalchemy import Integer
# from sqlalchemy import String
# from sqlalchemy import DateTime

# from sqlalchemy.orm import relationship

# from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()

# class Customer(Base):
#     __tablename__ = "customers"

#     id = Column(Integer, primary_key=True, index=True)
#     uuid = Column(String)
#     account_no = Column(String)
#     name = Column(String)
#     address = Column(String)
#     country = Column(String)
#     email = Column(String)
#     date_birth = Column(DateTime)
#     orders = relationship("Order")


# class Order(Base):
#     __tablename__ = "orders"

#     id = Column(Integer, primary_key=True, index=True)
#     uuid = Column(String)
#     # customer_id = Column(Integer)
#     customer_id = Column(Integer, ForeignKey("customers.id"))
#     date_order = Column(DateTime)
#     payment_type = Column(String)
#     total_amount = Column(String)
#     status = Column(String)

