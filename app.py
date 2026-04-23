from flask import Flask
from db import table 
app = Flask(__name__)

@app.route('/')
def index():
    print(table)

# cursor is a interface which is passing on the queries to sql.

    waiter=table.cursor()
    # Waiter - give him the query (sql)- what do u want    
    waiter.execute("SELECT * from users")

    # food - data what wa have got from sql as per order 
    food=waiter.fetchall()
    print(food)
    return 'Hello World from EBG'

