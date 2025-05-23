
from flask import db
from datetime import datetime

class Products():
    __tablename__ = "products"
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(30), nullable= False )
    price = db.column(db.integer, nullable=False )
    category_id = db.column(db.relati(30), nullable=False)
    produced_at = db.column(db.datetime ,default=datetime.now())
    updated_at = db.column(db.datetime ,default=datetime.now())
    

def __init__(self,name,price,category_id, produced_at ,updated_at):
    self.name = name
    self.price = price
    self.category_id = category_id
    self.produced_at = produced_at
    self.updated_at = updated_at
    












