from flask import Blueprint, Flask, redirect, render_template, request

from models.room import Room
import repositories.room_repository as room_repository

from models.room_session_type import RoomSessionType
import repositories.room_session_types_repository as room_session_types_repository

from models.session_type import SessionType
import repositories.session_type_repository as session_type_repository

rooms_blueprint = Blueprint("rooms", __name__)

# INDEX
@rooms_blueprint.route("/rooms")
def rooms():
    rooms = room_repository.select_all()
    room_session_types = room_session_types_repository.select_all()
    session_types = session_type_repository.select_all()
    return render_template("rooms/index.html", rooms=rooms, room_session_types = room_session_types, session_types = session_types)

# NEW
@rooms_blueprint.route("/rooms/new")
def new_room():
    return render_template("rooms/new.html")

# CREATE
@rooms_blueprint.route("/rooms", methods=["POST"])
def create_room():
    name = request.form["name"]
    new_room = Room(name)
    room_repository.save(new_room)
    return redirect("/rooms")

# EDIT
@rooms_blueprint.route("/rooms/<id>/edit")
def edit_room(id):
    room = room_repository.select(id)
    return render_template('rooms/edit.html', room=room)


# UPDATE
@rooms_blueprint.route("/rooms/<id>", methods=["POST"])
def update_room(id):
    name = request.form["name"]
    updated_room = Room(name)
    room_repository.update(updated_room)
    return redirect("/rooms")


# DELETE
@rooms_blueprint.route("/rooms/<id>/delete", methods=["POST"])
def delete_room(id):
    room_repository.delete(id)
    return redirect("/rooms")