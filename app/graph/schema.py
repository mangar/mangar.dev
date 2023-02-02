import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Customer as CustomerModel

DATABASE_URL = "mysql://root:pwd@192.168.1.113/py_mysql"
def get_db():
    engine = create_engine(DATABASE_URL, echo=True, future=True)
    db = Session(engine)
    return db


class CustomerMutation(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=False)
        name = graphene.String(required=False)
        uuid = graphene.String(required=False)

    customer = graphene.Field(lambda: CustomerQL)

    def mutate(self, info, uuid, name):
        customer = CustomerModel(name=name, uuid=uuid)

        db = get_db()

        db.begin()
        db.add(customer)
        db.commit()

        


        return CustomerMutation(customer=customer)


class Mutation(graphene.ObjectType):
    mutate_customer = CustomerMutation.Field()




class CustomerQL(SQLAlchemyObjectType):
    class Meta:
        model = CustomerModel
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    customers = graphene.List(lambda: CustomerQL, name=graphene.String())

    def resolve_customer(self, info, id=None):
        query = CustomerQL.get_query(info)
        if id:
            query = query.filter(CustomerModel.id == id)
        return query.all()

    # all_customers = SQLAlchemyConnectionField(
    #     CustomerQL.connection, sort=CustomerQL.sort_argument()
    # )

    # names = graphene.List(["Marcio", "Mangar"])

    # def resolve_users(self, info):
    #     query = CustomerModel.get_query(info)  # SQLAlchemy query
    #     return query.all()

schema = graphene.Schema(query=Query, mutation=Mutation)



# mutation{
#   mutateCustomer(name:"Marcio Mangar", uuid:"123-123-123"){
#     customer{
#       id
#       uuid
#       name
#     }
#   }
# }

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

