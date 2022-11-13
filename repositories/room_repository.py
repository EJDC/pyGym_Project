from db.run_sql import run_sql
from models.room import Room

def save(room):
    sql = "INSERT INTO rooms (name) VALUES (%s) RETURNING id"
    values = [room.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    room.id = id


def select_all():
    rooms = []
    sql = "SELECT * FROM rooms"
    results = run_sql(sql)
    for result in results:
        room = Room(result["name"], result["id"])
        rooms.append(room)
    return rooms


def select(id):
    room = None 
    sql = "SELECT * FROM rooms WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        room = Room(result["name"], result["id"])
    return room


def delete_all():
    sql = "DELETE FROM rooms"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM rooms WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(room):
    sql = "UPDATE rooms SET name = %s WHERE id = %s"
    values = [room.name, room.id]
    run_sql(sql, values)
