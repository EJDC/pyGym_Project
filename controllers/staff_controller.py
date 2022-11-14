from flask import Blueprint, Flask, redirect, render_template, request

from models.staff import Staff
import repositories.staff_repository as staff_repository

from models.staff_session_type import StaffSessionType
import repositories.staff_session_types_repository as staff_session_types_repository

staff_blueprint = Blueprint("staff", __name__)

# INDEX
@staff_blueprint.route("/staff")
def staff():
    staff = staff_repository.select_all()
    staff_session_types = staff_session_types_repository.select_all()
    return render_template("staff/index.html", staff=staff, staff_session_types = staff_session_types)

# NEW
@staff_blueprint.route("/staff/new")
def new_staff_member():
    return render_template("staff/new.html")

# CREATE
@staff_blueprint.route("/staff", methods=["POST"])
def create_staff_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    new_staff_member = Staff(first_name, last_name, email)
    staff_repository.save(new_staff_member)
    return redirect("/staff")

# EDIT
@staff_blueprint.route("/staff/<id>/edit")
def edit_staff_member(id):
    staff_member = staff_repository.select(id)
    return render_template('staff/edit.html', staff_member=staff_member)


# UPDATE
@staff_blueprint.route("/staff/<id>", methods=["POST"])
def update_staff_member(id):
    name = request.form["name"]
    updated_staff_member = Staff(name)
    staff_repository.update(updated_staff_member)
    return redirect("/staff")


# DELETE
@staff_blueprint.route("/staff/<id>/delete", methods=["POST"])
def delete_staff_member(id):
    staff_repository.delete(id)
    return redirect("/staff")