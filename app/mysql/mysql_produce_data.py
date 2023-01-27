import sys, random

from faker import Faker
from mysql.connector import connect, Error


MY_HOST = "localhost"
MY_USER = "root"
MY_PWD = "pwd"
MY_DATABASE = "py_mysql"

def get_connect(database=MY_DATABASE):
    return connect(host=MY_HOST, user=MY_USER, password=MY_PWD, database=database)

def create_db(db_name="py_mysql"):
    connect = get_connect("db")
    mycursor = connect.cursor()
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")


def create_tables():
    connect = get_connect()
    mycursor = connect.cursor()

    mycursor.execute("""CREATE TABLE IF NOT EXISTS customers ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        uuid VARCHAR(255),
        account_no VARCHAR(255),
        name VARCHAR(255), 
        address VARCHAR(255), 
        country VARCHAR(255),
        email VARCHAR(255), 
        date_birth DATE
        )"""
        )

    mycursor.execute(
        """CREATE TABLE IF NOT EXISTS orders ( 
            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            uuid VARCHAR(255),
            customer_id int, FOREIGN KEY(customer_id) REFERENCES customers(id),
            date_order DATE,
            payment_type VARCHAR(255),
            total_amount DECIMAL(10,2),
            status VARCHAR(255)            
        )"""
        )




def generate_data(count=10):
    create_db()
    create_tables()

    connect = get_connect()
    cursor = connect.cursor()

    fake = Faker()

    # clients table
    for _ in range(count):
        iban = fake.iban()
        cursor.execute(f'''INSERT INTO customers( uuid,
            account_no, 
            name, 
            address, 
            country,
            email, 
            date_birth) 
        values( UUID(),
            "{iban}", 
            "{fake.name()}", 
            "{fake.address()}", 
            "{fake.country_code()}", 
            "{fake.free_email()}", 
            "{fake.date()}"
            )        
        ''')

        connect.commit()

        for _ in range(random.randint(1,90)):
            cursor.execute(f'''INSERT INTO orders( 
                uuid,
                customer_id,
                date_order,
                payment_type, total_amount, status) 
            values( UUID(),
                (select id from customers where account_no = '{iban}'), 
                "{fake.date()}", 
                "{random.choice(['CC', 'DEBIT', 'CASH', 'PIX'])}", 
                {fake.pyint()},
                "{random.choice(['PAID','WAITING_PAYMENT','CANCELED',])}"
                )        
            ''')

        connect.commit()




if __name__ == '__main__':
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print (f">> PRODUCE SQL DATA ({count})")

    generate_data(count)



    connect = get_connect()
    cursor = connect.cursor()

    cursor.execute("SELECT id, uuid, account_no, name, address, country, email, date_birth FROM customers limit 10")
    result = cursor.fetchall()

    for r in result:
        print(r)



