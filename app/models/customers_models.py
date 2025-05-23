
from flask import db
from datetime import datetime

class Customer():
    __tablename__ = "customer"
    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string(50), nullable= False )
    email = db.column(db.integer, nullable=False )
    contact = db.column(db.relati(30), nullable=False)
    product_id = db.column(db.relati(30), nullable=False)
    produced_at = db.column(db.datetime ,default=datetime.now())
    updated_at = db.column(db.datetime ,default=datetime.now())
    

def __init__(self,name,email,contact, product_id,produced_at ,updated_at):
    self.name = name
    self.email = email
    self.contact = contact
    self.product_id = product_id
    self.produced_at = produced_at
    self.updated_at = updated_at













