import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse


from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Customer




app = FastAPI(title="GraphQL")



DATABASE_URL = "mysql://root:pwd@192.168.1.113/py_mysql"

def get_db():
    engine = create_engine(DATABASE_URL, echo=True, future=True)
    db = Session(engine)
    return db
    


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")





@app.post("/query/json")
async def query_json(customer_id:int):
    """ """
    responses = []
    
    try:
        db = get_db()
        users = db.query(Customer).filter(Customer.id == customer_id)
        for user in users:
            _user = {
                'id':user.id,
                'name':user.name,
                'address':user.address,
                'country':user.country,
                'email':user.email,
                'date_birth':user.date_birth,
                'orders_count':0,
                'orders':[]
            }

            print(f'- {user.name}')

            for order in user.orders:
                _user['orders'].append({
                    'id':order.id,
                    'uuid':order.uuid,
                    'payment_type':order.payment_type,
                    'total_amount':order.total_amount,
                    'status':order.status
                })
                print(f'  - {order.uuid}')

            _user['orders_count'] = len(_user['orders'])

            responses.append(_user)



    finally:
        db.close()

    return JSONResponse(content=json.loads(json.dumps(responses, default=str)))


