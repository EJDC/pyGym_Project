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

customer1 = Customer("Ned", "Flanders", '1976-6-22', "ned@okilydokiley.com", "Standard", "Active", "Direct Debit", True, True, False, False)
customer_repository.save(customer1)

customer2 = Customer("Clancy", "Wiggum", '1964-7-22', "clancy@springfieldcops.gov", "Premium", "Active", "Card Payment", False, True, False, True)
customer_repository.save(customer2)

room1 = Room("Studio1")
room_repository.save(room1)

staff1 = Staff("Arnold", "Schwarzenegger", "iwill@beback.com")
staff_repository.save(staff1)

session_type1 = SessionType("Yoga")
session_type_repository.save(session_type1)

session1 = Session("Fun Yoga", '2022-11-22 10:30:00', 45, 16, 99, 5.50, 9.99, 30, staff1, 50.40, room1, session_type1)
session_repository.save(session1)

room_session_type1 = RoomSessionType(room1, session_type1)
room_session_types_repository.save(room_session_type1)

staff_session_type1 = StaffSessionType(staff1, session_type1)
staff_session_types_repository.save(staff_session_type1)

booking1 = Booking(customer1, session1)
bookings_repository.save(booking1)


# pdb.set_trace()


