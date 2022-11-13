from flask import Blueprint, Flask, redirect, render_template, request

from models.room_session_type import RoomSessionType
import repositories.room_session_types_repository as room_session_types_repository
import repositories.room_repository as room_repository
import repositories.session_type_repository as session_type_repository

room_session_types_blueprint = Blueprint("room_session_types", __name__)

# INDEX
@room_session_types_blueprint.route("/room_session_types")
def room_session_types():
    room_session_types = room_session_types_repository.select_all()
    return render_template("room_session_types/index.html", room_session_types = room_session_types)

# NEW
@room_session_types_blueprint.route("/room_session_types/new")
def new_room_session_type():
    rooms = room_repository.select_all()
    session_types = session_type_repository.select_all()
    return render_template("room_session_types/new.html", rooms=rooms, sessions_types = session_types)

# CREATE
@room_session_types_blueprint.route("/room_session_types", methods=["POST"])
def create_room_session_type():
    room_id = request.form["room_id"]
    session_id = request.form["session_type_id"]
    room = room_repository.select(room_id)
    session_type = session_type_repository.select(session_id)
    new_room_session_type = RoomSessionType(room, session_type)
    room_session_types_repository.save(new_room_session_type)
    return redirect("/room_session_types")


# EDIT
@room_session_types_blueprint.route("/room_session_types/<id>/edit")
def edit_room_session_type(id):
    room_session_type = room_session_types_repository.select(id)
    rooms = room_repository.select_all()
    session_types = session_type_repository.select_all()
    return render_template('room_session_types/edit.html', room_session_type = room_session_type, rooms = rooms, session_types = session_types)


# UPDATE
@room_session_types_blueprint.route("/room_session_types/<id>", methods=["POST"])
def update_room_session_type(id):
    room_id = request.form["room_id"]
    session_id = request.form["session_id"]
    room = room_repository.select(room_id)
    session_type = session_type_repository.select(session_id)
    updated_room_session_type = RoomSessionType(room, session_type, id)
    room_session_types_repository.update(updated_room_session_type)
    return redirect("/room_session_types")


# DELETE
@room_session_types_blueprint.route("/room_session_types/<id>/delete", methods=["POST"])
def delete_room_session_type(id):
    room_session_types_repository.delete(id)
    return redirect("/room_session_types")
