from flask import Blueprint, Flask, redirect, render_template, request

from models.session import Session
import repositories.session_repository as session_repository

sessions_blueprint = Blueprint("sessions", __name__)

# INDEX
@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("sessions/index.html", sessions=sessions)