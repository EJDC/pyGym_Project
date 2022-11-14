from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repository
import repositories.staff_repository as staff_repository
import repositories.room_repository as room_repository
import repositories.session_type_repository as session_type_repository

sessions_blueprint = Blueprint("sessions", __name__)

# INDEX
@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)

# NEW
@sessions_blueprint.route("/sessions/new")
def new_session():
    return render_template("sessions/new.html")

# CREATE
@sessions_blueprint.route("/sessions", methods=["POST"])
def create_session():
    name = request.form["name"]
    date_and_time = request.form["date_and_time"]
    duration = request.form["duration"]
    min_age = request.form["min_age"]
    max_age = request.form["max_age"]
    p_member_price = request.form["p_member_price"]
    s_member_price = request.form["s_member_price"]
    max_capacity = request.form["max_capacity"]
    instructor_id = request.form["instructor_id"]
    instructor_payment = request.form["instructor_payment"]
    room_id = request.form["room_id"]
    session_type_id = request.form["session_type_id"]
    instructor = staff_repository.select(instructor_id)
    room = room_repository.select(room_id)
    session_type = session_type_repository.select(session_type_id)
    new_session = Session(name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor, instructor_payment, room, session_type)
    session_repository.save(new_session)
    return redirect("/sessions")
    
# EDIT
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repository.select(id)
    return render_template('sessions/edit.html', session=session)

# UPDATE
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    date_and_time = request.form["date_and_time"]
    duration = request.form["duration"]
    min_age = request.form["min_age"]
    max_age = request.form["max_age"]
    p_member_price = request.form["p_member_price"]
    s_member_price = request.form["s_member_price"]
    max_capacity = request.form["max_capacity"]
    instructor_id = request.form["instructor_id"]
    instructor_payment = request.form["instructor_payment"]
    room_id = request.form["room_id"]
    session_type_id = request.form["session_type_id"]
    instructor = staff_repository.select(instructor_id)
    room = room_repository.select(room_id)
    session_type = session_type_repository.select(session_type_id)
    updated_session = Session(name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor, instructor_payment, room, session_type, id)
    session_repository.update(updated_session)
    return redirect(request.referrer)

@sessions_blueprint.route("/sessions/<id>")
def show_(id):
    session = session_repository.select(id)
    staff = staff_repository.select_all()
    rooms = room_repository.select_all()
    session_types = session_type_repository.select_all()
    # bookings = customer_repository.select_sessions_customers(id)
    return render_template('sessions/session_information.html', session = session, staff = staff, rooms=rooms, session_types = session_types)
    # , bookings = bookings)

# DELETE
@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")