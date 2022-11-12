from flask import Blueprint, Flask, redirect, render_template, request

from models.room import Room
import repositories.room_repository as room_repository

rooms_blueprint = Blueprint("rooms", __name__)

# INDEX
@rooms_blueprint.route("/rooms")
def rooms():
    rooms = room_repository.select_all()
    return render_template("rooms/index.html", rooms=rooms)