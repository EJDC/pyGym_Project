from flask import Blueprint, Flask, redirect, render_template, request

from models.staff_session_type import StaffSessionType
import repositories.staff_session_types_repository as staff_session_types_repository
import repositories.staff_repository as staff_repository
import repositories.session_type_repository as session_type_repository

staff_session_types_blueprint = Blueprint("staff_session_types", __name__)

# INDEX
@staff_session_types_blueprint.route("/staff_session_types")
def staff_session_types():
    staff_session_types = staff_session_types_repository.select_all()
    return render_template("staff_session_types/index.html", staff_session_types = staff_session_types)

# NEW
@staff_session_types_blueprint.route("/staff_session_types/new")
def new_staff_session_type():
    staff = staff_repository.select_all()
    session_types = session_type_repository.select_all()
    return render_template("staff_session_types/new.html", staff=staff, sessions_types = session_types)

# CREATE
@staff_session_types_blueprint.route("/staff_session_types", methods=["POST"])
def create_staff_session_type():
    staff_id = request.form["staff_id"]
    session_id = request.form["session_type_id"]
    staff = staff_repository.select(staff_id)
    session_type = session_type_repository.select(session_id)
    new_staff_session_type = StaffSessionType(staff, session_type)
    staff_session_types_repository.save(new_staff_session_type)
    return redirect("/staff_session_types")


# EDIT
@staff_session_types_blueprint.route("/staff_session_types/<id>/edit")
def edit_staff_session_type(id):
    staff_session_type = staff_session_types_repository.select(id)
    staff = staff_repository.select_all()
    session_types = session_type_repository.select_all()
    return render_template('staff_session_types/edit.html', staff_session_type = staff_session_type, staff = staff, session_types = session_types)


# UPDATE
@staff_session_types_blueprint.route("/staff_session_types/<id>", methods=["POST"])
def update_staff_session_type(id):
    staff_id = request.form["staff_id"]
    session_id = request.form["session_id"]
    staff = staff_repository.select(staff_id)
    session_type = session_type_repository.select(session_id)
    updated_staff_session_type = StaffSessionType(staff, session_type, id)
    staff_session_types_repository.update(updated_staff_session_type)
    return redirect("/staff_session_types")


# DELETE
@staff_session_types_blueprint.route("/staff_session_types/<id>/delete", methods=["POST"])
def delete_staff_session_type(id):
    staff_session_types_repository.delete(id)
    return redirect("/staff_session_types")
