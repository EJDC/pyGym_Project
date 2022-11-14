from flask import Blueprint, Flask, redirect, render_template, request

from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint("customers", __name__)

# INDEX
@customers_blueprint.route("/customers")
def customers():
    customers = customer_repository.select_all()
    return render_template("customers/index.html", customers=customers)

# NEW
@customers_blueprint.route("/customers/new")
def new_customer():
    return render_template("customers/new.html")

# CREATE
@customers_blueprint.route("/customers", methods=["POST"])
def create_customer():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    dob = request.form["dob"]
    email = request.form["email"]
    membership_level = request.form["membership_level"]
    membership_status = request.form["membership_status"]
    payment_method = request.form["payment_method"]
    extra_physio = request.form["extra_physio"]
    extra_pt = request.form["extra_pt"]
    extra_service_3 = request.form["extra_service_3"]
    extra_service_4 = request.form["extra_service_4"]
    # missed_classes = missed_classes
    # monthly_bill = monthly_bill
    # id = id
    new_customer = Customer(first_name, last_name, dob, email, membership_level, membership_status, payment_method, extra_physio, extra_pt, extra_service_3, extra_service_4)
    customer_repository.save(new_customer)
    return redirect("/customers")

# EDIT
@customers_blueprint.route("/customers/<id>/edit")
def edit_customer(id):
    customer = customer_repository.select(id)
    return render_template('customers/edit.html', customer=customer)


# UPDATE
@customers_blueprint.route("/customers/<id>", methods=["POST"])
def update_customer(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    dob = request.form["dob"]
    email = request.form["email"]
    membership_level = request.form["membership_level"]
    membership_status = request.form["membership_status"]
    payment_method = request.form["payment_method"]
    extra_physio = request.form["extra_physio"]
    extra_pt = request.form["extra_pt"]
    extra_service_3 = request.form["extra_service_3"]
    extra_service_4 = request.form["extra_service_4"]
    # missed_classes = missed_classes
    # monthly_bill = monthly_bill
    # id = id
    updated_customer = Customer(first_name, last_name, dob, email, membership_level, membership_status, payment_method, extra_physio, extra_pt, extra_service_3, extra_service_4)
    customer_repository.update(updated_customer)
    return redirect("/customers")

@customers_blueprint.route("/customers/<id>")
def show_customer(id):
    customer = customer_repository.select(id)
    return render_template('customers/customer_profile.html', customer = customer)

# DELETE
@customers_blueprint.route("/customers/<id>/delete", methods=["POST"])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")