from flask import Flask, jsonify
from db import table 
import psycopg2.extras
app = Flask(__name__)

@app.route('/')
def index():
    print(table)

# cursor is a interface which is passing on the queries to sql.

    waiter=table.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    waiter.execute('SELECT * from "EBG"')

    # food - data what wa have got from sql as per order 
    food=waiter.fetchall()
    print(food)
    return jsonify(food)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

