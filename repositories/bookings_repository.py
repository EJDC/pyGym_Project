from db.run_sql import run_sql
from models.booking import Booking

from models.customer import Customer
import repositories.customer_repository as customer_repository

import repositories.session_repository as session_repository

def save(booking):
    sql = "INSERT INTO bookings (customer_id, session_id) VALUES (%s, %s) RETURNING id"
    values = [booking.customer.id, booking.session.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        customer = customer_repository.select(result["customer_id"])
        session = session_repository.select(result["session_id"])
        booking = Booking(customer, session, result["id"])
        bookings.append(booking)
    return bookings


def select(id):
    booking = None 
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        customer = customer_repository.select(result["customer_id"])
        session = session_repository.select(result["session_id"])
        booking = Booking(customer, session, result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking):
    sql = "UPDATE bookings SET (customer_id, session_id) = (%s, %s) WHERE id = %s"
    values = [booking.customer.id, booking.session.id, booking.id]
    run_sql(sql, values)

def capacity_check(session):
    bookings = []
    sql = "SELECT * FROM bookings WHERE session_id = %s"
    sessionid = str(session.id)
    values = [sessionid]
    results = run_sql(sql, values)
    for result in results:
        customer = customer_repository.select(result["customer_id"])
        session = session_repository.select(result["session_id"])
        booking = Booking(customer, session, result["id"])
        bookings.append(booking)
    return len(bookings)
