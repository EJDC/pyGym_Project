class Session:
    def __init__(self, name, date_and_time, duration, min_age, max_age, p_member_price, s_member_price, max_capacity, instructor_payment, session_type, instructor=None, room=None, id=None):
        self.name = name
        self.date_and_time = date_and_time
        self.duration = duration
        self.min_age = min_age
        self.max_age = max_age
        self.p_member_price = p_member_price
        self.s_member_price = s_member_price
        self.max_capacity = max_capacity
        self.instructor = instructor
        self.instructor_payment = instructor_payment
        self.room = room
        self.session_type = session_type
        self.id = id