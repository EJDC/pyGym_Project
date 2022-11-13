from db.run_sql import run_sql
from models.room_session_type import RoomSessionType

from models.room import Room
import repositories.room_repository as room_repository

from models.session_type import SessionType
import repositories.session_repository as session_type_repository

def save(room_session_type):
    sql = "INSERT INTO room_session_types (room_id, session_type_id) VALUES (%s, %s) RETURNING id"
    values = [room_session_type.room.id, room_session_type.session_type.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    room_session_type.id = id


def select_all():
    room_session_types = []
    sql = "SELECT * FROM room_session_types"
    results = run_sql(sql)
    for result in results:
        room = room_repository.select(result["room_id"])
        session_type = session_type_repository.select(result["session_type_id"])
        room_session_type = room_session_type(session_type, room, result["id"])
        room_session_types.append(room_session_type)
    return room_session_types


def select(id):
    room_session_type = None 
    sql = "SELECT * FROM room_session_types WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        room = room_repository.select(result["room_id"])
        session_type = session_type_repository.select(result["session_type_id"])
        room_session_type = RoomSessionType(room, session_type, result["id"])
    return room_session_type


def delete_all():
    sql = "DELETE FROM room_session_types"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM room_session_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(room_session_type):
    sql = "UPDATE room_session_types SET (room_id, session_type_id) = (%s, %s) WHERE id = %s"
    values = [room_session_type.room.id, room_session_type.session_type.id, room_session_type.id]
    run_sql(sql, values)
