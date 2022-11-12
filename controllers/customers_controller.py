from flask import Blueprint, Flask, redirect, render_template, request

from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint("customers", __name__)

# INDEX
@customers_blueprint.route("/customers")
def customers():
    customers = customer_repository.select_all()
    return render_template("customers/index.html", customers=customers)