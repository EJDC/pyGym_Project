from flask import Blueprint, Flask, redirect, render_template, request

from models.session_type import SessionType
import repositories.session_type_repository as session_type_repository

session_types_blueprint = Blueprint("session_types", __name__)

# INDEX
@session_types_blueprint.route("/sessiontypes")
def session_types():
    session_types = session_type_repository.select_all()
    return render_template("session_types/index.html", session_types=session_types)


# NEW
@session_types_blueprint.route("/sessiontypes/new")
def new_session_type():
    return render_template("session_types/new.html")


# CREATE
@session_types_blueprint.route("/sessiontypes", methods=["POST"])
def create_session_type():
    name = request.form["name"]
    new_session_type = SessionType(name)
    session_type_repository.save(new_session_type)
    return redirect("/sessiontypes")


# EDIT
@session_types_blueprint.route("/sessiontypes/<id>/edit")
def edit_session_type(id):
    session_type = session_type_repository.select(id)
    return render_template('session_types/edit.html', session_type=session_type)


# UPDATE
@session_types_blueprint.route("/sessiontypes/<id>", methods=["POST"])
def update_zombie(id):
    name = request.form["name"]
    session_type = SessionType(name, id)
    session_type_repository.update(session_type)


# DELETE
@session_types_blueprint.route("/sessiontypes/<id>/delete", methods=["POST"])
def delete_zombie(id):
    session_type_repository.delete(id)
    return redirect("/sessiontypes")
