from db.run_sql import run_sql
from models.session_type import SessionType

def save(session_type):
    sql = "INSERT INTO session_types (name) VALUES (%s) RETURNING id"
    values = [session_type.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    session_type.id = id


def select_all():
    session_types = []
    sql = "SELECT * FROM session_types"
    results = run_sql(sql)
    for result in results:
        session_type = SessionType(result["name"], result["id"])
        session_types.append(session_type)
    return session_types


def select(id):
    session_type = None 
    sql = "SELECT * FROM session_types WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    session_type = SessionType(result["name"], result["id"])
    return session_type


def delete_all():
    sql = "DELETE FROM session_types"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM session_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(session_type):
    sql = "UPDATE session_types SET name = %s WHERE id = %s"
    values = [session_type.name, session_type.id]
    run_sql(sql, values)
