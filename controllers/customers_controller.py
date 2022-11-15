from flask import Blueprint, Flask, redirect, render_template, request

from models.customer import Customer
import repositories.customer_repository as customer_repository

from models.booking import Booking
import repositories.bookings_repository as bookings_respository

from models.session import Session
import repositories.session_repository as session_respository

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
    extra_physio = request.form.get("extra_physio")
    extra_pt = request.form.get("extra_pt")
    extra_service_3 = request.form.get("extra_service_3")
    extra_service_4 = request.form.get("extra_service_4")
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
    extra_physio = request.form.get("extra_physio")
    extra_pt = request.form.get("extra_pt")
    extra_service_3 = request.form.get("extra_service_3")
    extra_service_4 = request.form.get("extra_service_4")
    missed_classes = request.form["missed_classes"]
    monthly_bill = request.form["monthly_bill"]
    updated_customer = Customer(first_name, last_name, dob, email, membership_level, membership_status, payment_method, extra_physio, extra_pt, extra_service_3, extra_service_4, missed_classes, monthly_bill, id)
    customer_repository.update(updated_customer)
    return redirect(request.referrer)

# SHOW
@customers_blueprint.route("/customers/<id>")
def show_customer(id):
    customer = customer_repository.select(id)
    sessions_booked = customer_repository.select_customers_bookings(id)
    sessions = session_respository.select_all()
    bookings = bookings_respository.select_all()
    return render_template('customers/customer_profile.html', customer = customer, sessions_booked = sessions_booked, sessions = sessions,bookings = bookings)

# DELETE
@customers_blueprint.route("/customers/<id>/delete", methods=["POST"])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")