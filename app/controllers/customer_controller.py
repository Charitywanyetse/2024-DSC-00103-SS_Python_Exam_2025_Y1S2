# importing needed libraries

from flask import Flask,jsonify,Blueprint,request



# question two (c)  create new customer

customer = Flask(__name__)


@customer.route("/customer", methods=["POST"])
def create_customer():
    data = request.json

    "id" = data.get("id")
    "name" = data.get("name")
    "price" = data.get("price")
    if customer : customer
    return jsonify({"message":"customer successfully created"})
    


























