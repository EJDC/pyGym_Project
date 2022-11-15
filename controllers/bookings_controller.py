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
    customers = customer_repository.select_all()
    sessions = session_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings, sessions = sessions, customers = customers)

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
    bookings = bookings_repository.select_all()
    # Check if customer is active or deactivated.
    if customer.membership_status == "Deactivated":
        return redirect("https://http.cat/401")
    else:
        current_occupancy = bookings_repository.capacity_check(session)
        # Check if space in class.
        if current_occupancy + 1 > session.max_capacity:
            return redirect("https://http.cat/401")
        else:
            for booking in bookings:
                booking_customer_id = str(booking.customer.id)
                session_customer_id = str(booking.session.id)
                if booking_customer_id == customer_id and session_customer_id == session_id:
                    return  redirect("https://http.cat/401")
            new_booking = Booking(customer, session)
            bookings_repository.save(new_booking)
            return redirect(request.referrer)


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
    return redirect(request.referrer)
