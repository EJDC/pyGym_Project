from flask import Flask, render_template

from controllers.customers_controller import customers_blueprint
from controllers.sessions_controller import sessions_blueprint
from controllers.staff_controller import staff_blueprint
from controllers.room_controller import rooms_blueprint


app = Flask(__name__)

app.register_blueprint(customers_blueprint)
app.register_blueprint(sessions_blueprint)
app.register_blueprint(staff_blueprint)
app.register_blueprint(rooms_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
