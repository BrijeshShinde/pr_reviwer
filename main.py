import mysql.connector

def insert_product(title:str, price:float, description:str):
    conncetion = mysql.connector.connect(
        host = "localhost",
        user="root",
        password = "root",
        database ="mydb",
        port=3306 
    )

    cusor = conncetion.cursor()

    cusor.execute("""
        Insert into products (title, description, price) values ('{title}','{description}',{price})
        """)

    conncetion.commit()
    cusor.close()
    conncetion.close()

insert_product('product1',10.50,'this is a nice product')
print()
print("-"*80)

def agent():
    pass