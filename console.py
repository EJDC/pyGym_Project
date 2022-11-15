import pdb

from models.booking import Booking
import repositories.bookings_repository as bookings_repository

from models.customer import Customer
import repositories.customer_repository as customer_repository

from models.room_session_type import RoomSessionType
import repositories.room_session_types_repository as room_session_types_repository

from models.room import Room
import repositories.room_repository as room_repository

from models.session import Session
import repositories.session_repository as session_repository

from models.session_type import SessionType
import repositories.session_type_repository as session_type_repository

from models.staff_session_type import StaffSessionType
import repositories.staff_session_types_repository as staff_session_types_repository

from models.staff import Staff
import repositories.staff_repository as staff_repository

bookings_repository.delete_all()
customer_repository.delete_all()
room_session_types_repository.delete_all()
session_repository.delete_all()
room_repository.delete_all()
staff_session_types_repository.delete_all()
staff_repository.delete_all()
session_type_repository.delete_all()

# CUSTOMERS

customer1 = Customer("Ned", "Flanders", '1976-6-22', "ned@okilydokiley.com", "Standard", "Active", "Direct Debit", True, True, False, False)
customer_repository.save(customer1)

customer2 = Customer("Clancy", "Wiggum", '1964-7-22', "clancy@springfieldcops.gov", "Premium", "Active", "Card Payment", False, True, False, True)
customer_repository.save(customer2)

customer3 = Customer("Patty", "Bouvier", '1953-12-2', "patty@stopsmoking.com", "Standard", "Active", "Cash", True, False, True, False)
customer_repository.save(customer3)

customer4 = Customer("Edna", "Krabappel", '1959-9-14', "edna@springfieldelementary.ac", "Premium", "Active", "Direct Debit", False, True, False, True)
customer_repository.save(customer4)

# ROOMS

room1 = Room("Studio 1")
room_repository.save(room1)

room2 = Room("Studio 2")
room_repository.save(room2)

room3 = Room("Cycle Studio")
room_repository.save(room3)

room4 = Room("Pool")
room_repository.save(room4)

# STAFF

staff1 = Staff("Rainer", "Wolfcastle", "iwill@beback.com")
staff_repository.save(staff1)

staff2 = Staff("Luann", "Van Houten", "millhouse_mum@stay_fit.com")
staff_repository.save(staff2)

staff3 = Staff("Moe", "Szyslak", "mybarismygym@pygym.com")
staff_repository.save(staff3)

# SESSION

session_type1 = SessionType("Yoga")
session_type_repository.save(session_type1)

session_type2 = SessionType("Cycle")
session_type_repository.save(session_type2)

session_type3 = SessionType("Strength")
session_type_repository.save(session_type3)

session_type4 = SessionType("Aqua")
session_type_repository.save(session_type4)


# SESSIONS

session1 = Session("Vinyasa Yoga", '2022-11-22 08:00:00', 45, 16, 99, 5.50, 9.99, 30, 49.99, session_type1, staff1, room1)
session_repository.save(session1)

session2 = Session("Group Cycle", '2022-11-22 08:30:00', 60, 16, 99, 0.00, 5.99, 35, 54.99,  session_type2,  staff2, room3)
session_repository.save(session2)

session3 = Session("Core Conditioning", '2022-11-22 09:30:00', 30, 16, 99, 0.00, 4.99, 25, 39.99, session_type2, staff2,  room3)
session_repository.save(session3)

# ROOM SESSION TYPES

room_session_type1 = RoomSessionType(room1, session_type1)
room_session_types_repository.save(room_session_type1)

room_session_type2 = RoomSessionType(room1, session_type3)
room_session_types_repository.save(room_session_type2)

room_session_type3 = RoomSessionType(room2, session_type1)
room_session_types_repository.save(room_session_type3)

room_session_type4 = RoomSessionType(room2, session_type3)
room_session_types_repository.save(room_session_type4)

room_session_type5 = RoomSessionType(room3, session_type2)
room_session_types_repository.save(room_session_type5)

room_session_type6 = RoomSessionType(room4, session_type4)
room_session_types_repository.save(room_session_type6)

# STAFF SESSION TYPES

staff_session_type1 = StaffSessionType(staff1, session_type1)
staff_session_types_repository.save(staff_session_type1)

staff_session_type2 = StaffSessionType(staff1, session_type3)
staff_session_types_repository.save(staff_session_type2)

staff_session_type3 = StaffSessionType(staff2, session_type2)
staff_session_types_repository.save(staff_session_type3)

staff_session_type3 = StaffSessionType(staff2, session_type3)
staff_session_types_repository.save(staff_session_type3)

staff_session_type5 = StaffSessionType(staff3, session_type4)
staff_session_types_repository.save(staff_session_type5)

staff_session_type6 = StaffSessionType(staff3, session_type1)
staff_session_types_repository.save(staff_session_type6)

# BOOKINGS

booking1 = Booking(customer1, session1)
bookings_repository.save(booking1)

booking2 = Booking(customer1, session3)
bookings_repository.save(booking2)

booking3 = Booking(customer2, session2)
bookings_repository.save(booking3)

booking4 = Booking(customer2, session3)
bookings_repository.save(booking4)

booking5 = Booking(customer3, session1)
bookings_repository.save(booking5)

booking6 = Booking(customer3, session2)
bookings_repository.save(booking6)


# pdb.set_trace()


