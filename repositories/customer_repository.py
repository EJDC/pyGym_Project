from db.run_sql import run_sql
from models.customer import Customer
from models.session import Session
import repositories.session_type_repository as session_type_repository
import repositories.staff_repository as staff_repository
import repositories.room_repository as room_repository

def save(customer):
    sql = "INSERT INTO customers (first_name, last_name, dob, email, membership_level, membership_status, payment_method, extra_physio, extra_pt, extra_service_3, extra_service_4, missed_classes, monthly_bill) VALUES (%s, %s, %s, %s, %s, %s,%s, %s,%s,%s, %s, %s, %s) RETURNING id"
    values = [customer.first_name, customer.last_name, customer.dob, customer.email, customer.membership_level, customer.membership_status, customer.payment_method, customer.extra_physio, customer.extra_pt, customer.extra_service_3, customer.extra_service_4, customer.missed_classes, customer.monthly_bill]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id


def select_all():
    customers = []
    sql = "SELECT * FROM customers"
    results = run_sql(sql)
    for result in results:
        customer = Customer(result["first_name"], result["last_name"], result["dob"], result["email"], result["membership_level"], result["membership_status"], result["payment_method"], result["extra_physio"], result["extra_pt"], result["extra_service_3"], result["extra_service_4"], result["missed_classes"], result["monthly_bill"], result["id"])
        customers.append(customer)
    return customers


def select(id):
    customer = None 
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        customer = Customer(result["first_name"], result["last_name"], result["dob"], result["email"], result["membership_level"], result["membership_status"], result["payment_method"], result["extra_physio"], result["extra_pt"], result["extra_service_3"], result["extra_service_4"], result["missed_classes"], result["monthly_bill"],result["id"])
    return customer


def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(customer):
    sql = "UPDATE customers SET (first_name, last_name, dob, email, membership_level, membership_status, payment_method, extra_physio, extra_pt, extra_service_3, extra_service_4, missed_classes, monthly_bill) = (%s, %s, %s, %s, %s, %s,%s, %s,%s,%s, %s, %s, %s) WHERE id = %s"
    values = [customer.first_name, customer.last_name, customer.dob, customer.email, customer.membership_level, customer.membership_status, customer.payment_method, customer.extra_physio, customer.extra_pt, customer.extra_service_3, customer.extra_service_4, customer.missed_classes, customer.monthly_bill, customer.id]
    run_sql(sql, values)
    
def select_customers_bookings(id):
    customer_bookings = []
    sql = "SELECT sessions.* FROM sessions INNER JOIN bookings ON bookings.session_id = sessions.id WHERE bookings.customer_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        room = room_repository.select(result["room"])
        instructor = staff_repository.select(result["instructor_id"])
        session_type = session_type_repository.select(result["session_type"])
        booking = Session(result["name"], result["date_and_time"], result["duration"], result["min_age"], result["max_age"], result["p_member_price"], result["s_member_price"], result["max_capacity"], result["instructor_payment"],  session_type, instructor, room, result["id"])
        customer_bookings.append(booking)
    return customer_bookings