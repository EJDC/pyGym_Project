from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repository
import repositories.staff_repository as staff_repository
import repositories.room_repository as room_repository
import repositories.session_type_repository as session_type_repository
import repositories.bookings_repository as bookings_repository
import repositories.customer_repository as customers_repository
import repositories.staff_session_types_repository as staff_sessions_repository
import repositories.room_session_types_repository as room_session_types_repository

sessions_blueprint = Blueprint("sessions", __name__)

# INDEX
@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)

# NEW
@sessions_blueprint.route("/sessions/new")
def new_session():
    session_types = session_type_repository.select_all()
    return render_template("sessions/new.html", session_types = session_types)

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
    instructor_payment = request.form["instructor_payment"]
    # room_id = null
    session_type_id = request.form["session_type_id"]
    # instructor = null
    # room = room_repository.select(room_id)
    session_type = session_type_repository.select(session_type_id)
    new_session = Session(name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor_payment, session_type)
    session_repository.save(new_session)
    #will redirect to next part of form
    id = str(new_session.id)
    return redirect("/sessions/"+ id + "/instructor_room")

@sessions_blueprint.route("/sessions/<id>/instructor_room")
def instructor_room(id):
    session = session_repository.select(id)
    session_type_id = session.session_type.id
    instructors = staff_sessions_repository.select_session_instructor(session_type_id)
    rooms = room_session_types_repository.select_session_room(session_type_id)
    return render_template("sessions/instructor_room.html", session=session, instructors = instructors, rooms = rooms) 

# EDIT
@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repository.select(id)
    return render_template('sessions/edit.html', session=session)

# UPDATE
@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    session = session_repository.select(id)
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
    session_type_actual = session.session_type
    instructor = staff_repository.select(instructor_id)
    room = room_repository.select(room_id)
    updated_session = Session(name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor_payment, session_type_actual, instructor, room, id)
    session_repository.update(updated_session)
    return redirect("/sessions/" + id)


@sessions_blueprint.route("/sessions/<id>/instructor_room", methods=["POST"])
def add_instructor_and_room(id):
    session = session_repository.select(id)
    name = session.name
    date_and_time = session.date_and_time
    duration = session.duration
    min_age = session.min_age
    max_age = session.max_age
    p_member_price = session.p_member_price
    s_member_price = session.s_member_price
    max_capacity = session.max_capacity
    instructor_payment = session.instructor_payment
    session_type_id = session.session_type
    instructor_id = request.form["instructor_id"]
    room_id = request.form["room_id"]
    instructor = staff_repository.select(instructor_id)
    room = room_repository.select(room_id)
    updated_session = Session(name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor_payment, session_type_id, instructor, room, id)
    session_repository.update(updated_session)
    return redirect("/sessions/" + id)
# show
@sessions_blueprint.route("/sessions/<id>")
def show_(id):
    session = session_repository.select(id)
    session_type_id = session.session_type.id
    staff = staff_sessions_repository.select_session_instructor(session_type_id)
    rooms = room_session_types_repository.select_session_room(session_type_id)
    # staff = staff_repository.select_all()
    # rooms = room_repository.select_all()
    session_types = session_type_repository.select_all()
    attendees = session_repository.select_customers_attending_session(id)
    bookings = bookings_repository.select_all()
    customers = customers_repository.select_all()
    instructor = staff_repository.select(session.instructor.id)
    return render_template('sessions/session_information.html', instructor = instructor, customers = customers, session = session, staff = staff, rooms=rooms, session_types = session_types, attendees = attendees, bookings = bookings)

    session = session_repository.select(id)



# DELETE
@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")