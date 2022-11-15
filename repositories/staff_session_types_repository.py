from db.run_sql import run_sql
from models.staff_session_type import StaffSessionType

from models.staff import Staff
import repositories.staff_repository as staff_repository

from models.session_type import SessionType
import repositories.session_type_repository as session_type_repository

def save(staff_session_type):
    sql = "INSERT INTO staff_session_types (staff_id, session_type_id) VALUES (%s, %s) RETURNING id"
    values = [staff_session_type.staff_member.id, staff_session_type.session_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff_session_type.id = id


def select_all():
    staff_session_types = []
    sql = "SELECT * FROM staff_session_types"
    results = run_sql(sql)
    for result in results:
        staff = staff_repository.select(result["staff_id"])
        session_type = session_type_repository.select(result["session_type_id"])
        staff_session_type = StaffSessionType(staff, session_type, result["id"])
        staff_session_types.append(staff_session_type)
    return staff_session_types


def select(id):
    staff_session_type = None 
    sql = "SELECT * FROM staff_session_types WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        staff = staff_repository.select(result["staff_id"])
        session_type = session_type_repository.select(result["session_type_id"])
        staff_session_type = StaffSessionType(staff, session_type, result["id"])
    return staff_session_type


def delete_all():
    sql = "DELETE FROM staff_session_types"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM staff_session_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(staff_session_type):
    sql = "UPDATE staff_session_types SET (staff_id, session_type_id) = (%s, %s) WHERE id = %s"
    values = [staff_session_type.staff_member.id, staff_session_type.session_type.id, staff_session_type.id]
    run_sql(sql, values)

def select_session_instructor(session_type_id):
    instructors = []
    sql = "SELECT staff.* FROM staff INNER JOIN staff_session_types ON staff_session_types.staff_id = staff.id WHERE staff_session_types.session_type_id =  %s"
    values = [session_type_id]
    results = run_sql(sql, values)
    for result in results:
        instructor = Staff(result["first_name"], result["last_name"], result["email"], result["monthly_invoice"], result["id"])
        instructors.append(instructor)
    return instructors
