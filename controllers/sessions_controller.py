from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repository

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
    instructor = request.form["instructor"]
    instructor_payment = request.form["instructor_payment"]
    room = request.form["room"]
    new_session = Session(name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor, instructor_payment, room)
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
    instructor = request.form["instructor"]
    instructor_payment = request.form["instructor_payment"]
    room = request.form["room"]
    updated_session = Session(name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor, instructor_payment, room)
    session_repository.save(updated_session)
    return redirect("/sessions")


# DELETE
@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete_session(id):
    session_repository.delete(id)
    return redirect("/sessions")