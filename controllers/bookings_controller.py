from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.bookings_repository as bookings_repository
import repositories.customer_repository as customer_repository
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("bookings", __name__)

# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = bookings_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

# NEW
@bookings_blueprint.route("/bookings/new")
def new_booking():
    customers = customer_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("bookings/new.html", customers=customers, sessions=sessions)


# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    customer_id = request.form["customer_id"]
    session_id = request.form["session_id"]
    customer = customer_repository.select(customer_id)
    session = session_repository.select(session_id)
    new_booking = Booking(customer, session)
    bookings_repository.save(new_booking)
    return redirect("/bookings")


# EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = bookings_repository.select(id)
    customers = customer_repository.select_all()
    sessions = session_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, customers=customers, sessions=sessions)


# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    customer_id = request.form["customer_id"]
    session_id = request.form["session_id"]
    customer = customer_repository.select(customer_id)
    session = session_repository.select(session_id)
    booking = booking(customer, session, id)
    bookings_repository.update(booking)
    return redirect("/bookings")


# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    bookings_repository.delete(id)
    return redirect("/bookings")
