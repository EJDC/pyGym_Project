from flask import Blueprint, Flask, redirect, render_template, request

from models.staff import Staff
import repositories.staff_repository as staff_repository

staff_blueprint = Blueprint("staff", __name__)

# INDEX
@staff_blueprint.route("/staff")
def staff():
    staff = staff_repository.select_all()
    return render_template("staff/index.html", staff=staff)