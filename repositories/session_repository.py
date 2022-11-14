from db.run_sql import run_sql
from models.session import Session
from models.customer import Customer
import repositories.session_type_repository as session_type_repository
import repositories.staff_repository as staff_repository
import repositories.room_repository as room_repository

def save(session):
    sql = "INSERT INTO sessions (name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor_id, instructor_payment, room, session_type) VALUES (%s, %s, %s, %s, %s, %s,%s, %s,%s,%s, %s, %s) RETURNING id"
    values = [session.name, session.date_and_time, session.duration, session.min_age, session.max_age, session.p_member_price, session.s_member_price, session.max_capacity, session.instructor.id, session.instructor_payment, session.room.id, session.session_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    session.id = id


def select_all():
    sessions = []
    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for result in results:
        room = room_repository.select(result["room"])
        instructor = staff_repository.select(result["instructor_id"])
        session_type = session_type_repository.select(result["session_type"])
        session = Session(result["name"], result["date_and_time"], result["duration"], result["min_age"], result["max_age"], result["p_member_price"], result["s_member_price"], result["max_capacity"], instructor, result["instructor_payment"], room, session_type, result["id"])
        sessions.append(session)
    return sessions


def select(id):
    session = None 
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        room = room_repository.select(result["room"])
        instructor = staff_repository.select(result["instructor_id"])
        session_type = session_type_repository.select(result["session_type"])
        session = Session(result["name"], result["date_and_time"], result["duration"], result["min_age"], result["max_age"], result["p_member_price"], result["s_member_price"], result["max_capacity"], instructor, result["instructor_payment"], room, session_type, result["id"])
    return session


def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(session):
    sql = "UPDATE sessions SET (name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor_id, instructor_payment, room, session_type) = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [session.name, session.date_and_time, session.duration, session.min_age, session.max_age, session.p_member_price, session.s_member_price, session.max_capacity, session.instructor.id, session.instructor_payment, session.room.id, session.session_type.id, session.id]
    run_sql(sql, values)

def select_customers_attending_session(id):
    customers_attending_session = []
    sql = "SELECT customers.* FROM customers INNER JOIN bookings ON bookings.customer_id = customers.id WHERE bookings.session_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        # room = room_repository.select(result["room"])
        # instructor = staff_repository.select(result["instructor_id"])
        # session_type = session_type_repository.select(result["session_type"])
        customer = Customer(result["first_name"], result["last_name"], result["dob"], result["email"], result["membership_level"], result["membership_status"], result["payment_method"], result["extra_physio"], result["extra_pt"], result["extra_service_3"], result["extra_service_4"], result["missed_classes"], result["monthly_bill"], result["id"])
        customers_attending_session.append(customer)
    return customers_attending_session