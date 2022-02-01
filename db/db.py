'''
References:
https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
https://docs.python.org/3/library/sqlite3.html
'''
import sqlite3
from os.path import exists
class Db:
    def __init__(self):
       self.con = sqlite3.connect('estore.db') 

    def getCursor(self):
        return self.con.cursor()
    
    def close(self):
        self.con.commit()
        self.con.close()
        
        
def genDb():
    db = Db()
    cur = db.getCursor()

    #Note: Added category name for ease of use. Otherwise we need to have category table linked to products to derive the name

    cur.execute("CREATE TABLE categories (id INTEGER, name TEXT)")
    cur.execute("CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, category_name TEXT, category_id INTEGER, price real, available_quantity INTEGER, warning_quantity INTEGER)")


    # Insert Category data
    cur.execute("INSERT INTO categories (id,name) VALUES (1,'Cloths')")
    # cur.execute("INSERT INTO categories (id,name) VALUES (2,'Vegetables')")
    # cur.execute("INSERT INTO categories (id,name) VALUES (3,'Fruits')")
    cur.execute("INSERT INTO categories (id,name) VALUES (4,'Electronics')")

    # Insert Category data
    cur.execute("INSERT INTO products (name, category_id, category_name,price, available_quantity, warning_quantity) VALUES ('Shirts',1,'Cloths',1000,10,5)")
    cur.execute("INSERT INTO products (name, category_id, category_name,price, available_quantity, warning_quantity) VALUES ('Hat',1,'Cloths',500,5,2)")
    cur.execute("INSERT INTO products (name, category_id, category_name,price, available_quantity, warning_quantity) VALUES ('Towel',1,'Cloths',500,20,5)")

    cur.execute("INSERT INTO products (name, category_id, category_name,price, available_quantity, warning_quantity) VALUES ('RAM',4,'Electronics',2000,10,5)")
    cur.execute("INSERT INTO products (name, category_id, category_name,price, available_quantity, warning_quantity) VALUES ('Headphone',4,'Electronics',500,5,2)")
    cur.execute("INSERT INTO products (name, category_id, category_name,price, available_quantity, warning_quantity) VALUES ('Laptop',4,'Electronics',50000,10,5)")

    db.close()
    
    
'''
Generate initial records if db does not exist
'''    
file_exists = exists('estore.db')
if (not file_exists):
    genDb()
        
    
