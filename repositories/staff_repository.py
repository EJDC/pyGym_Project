from db.run_sql import run_sql
from models.staff import Staff

def save(staff):
    sql = "INSERT INTO staff (first_name, last_name, email, monthly_invoice) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [staff.first_name, staff.last_name, staff.email, staff.monthly_invoice]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id


def select_all():
    staff = []
    sql = "SELECT * FROM staff"
    results = run_sql(sql)
    for result in results:
        staff_member = Staff(result["first_name"], result["last_name"], result["email"], result["monthly_invoice"], result["id"])
        staff.append(staff_member)
    return staff


def select(id):
    staff_member = None 
    sql = "SELECT * FROM staff WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        staff_member = Staff(result["first_name"], result["last_name"], result["email"], result["monthly_invoice"], result["id"])
    return staff_member


def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(staff):
    sql = "UPDATE staff SET (first_name, last_name, email, monthly_invoice) = (%s, %s, %s, %s) WHERE id = %s"
    values = [staff.first_name, staff.last_name, staff.email, staff.monthly_invoice, staff.id]
    run_sql(sql, values)