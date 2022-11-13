from flask import Flask, render_template

from controllers.customers_controller import customers_blueprint
from controllers.sessions_controller import sessions_blueprint
from controllers.staff_controller import staff_blueprint
from controllers.room_controller import rooms_blueprint
from controllers.bookings_controller import bookings_blueprint
from controllers.session_type_controller import session_types_blueprint
from controllers.room_session_types_controller import room_session_types_blueprint
from controllers.staff_session_types_controller import staff_session_types_blueprint

app = Flask(__name__)

app.register_blueprint(customers_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(staff_blueprint)
app.register_blueprint(rooms_blueprint)
app.register_blueprint(bookings_blueprint)
app.register_blueprint(session_types_blueprint)
app.register_blueprint(room_session_types_blueprint)
app.register_blueprint(staff_session_types_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
