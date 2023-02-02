import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.models import Customer as CustomerModel


# MUTATION

from app import db

class CustomerMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=False)
        uuid = graphene.String(required=False)
        email = graphene.String(required=True)

    customer = graphene.Field(lambda: CustomerQL)

    def mutate(self, info, uuid, name, email):
        customer = CustomerModel(name=name, uuid=uuid, email=email)

        db.session.add(customer)
        db.session.commit()

        return CustomerMutation(customer=customer)


class Mutation(graphene.ObjectType):
    mutate_create_customer = CustomerMutation.Field()


# OBJECT

class CustomerQL(SQLAlchemyObjectType):
    class Meta:
        model = CustomerModel
        interfaces = (relay.Node,)


    


# QUERY

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    customersById = graphene.List(lambda: CustomerQL, id=graphene.String(), name=graphene.String())

    def resolve_customersById(self, info, id=None, name=None):
        query = CustomerQL.get_query(info)
        print(f'>>>> ID:{id} / NAME:{name}')
        if id:
            query = query.filter(CustomerModel.id == int(id))
        return query.all()



# SCHEMA

schema = graphene.Schema(query=Query, mutation=Mutation)


# 
# CREATE CUSTOMER
# 
# mutation{
#   mutateCreateCustomer(email:"md@md.com", name:"Michael Douglas", uuid:"222-222-222"){
#     customer{
#       id
#       uuid
#       name
#       email
#       address
#       country
#     }
#   }
# }

