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

    def date_in_words(self):
        day = self.date_and_time.strftime("%d")
        month = self.date_and_time.strftime("%b")
        year = self.date_and_time.strftime("%Y")
        return (day +" "+ month + " " + year)

    def time_in_words(self):
        hour = self.date_and_time.strftime("%I")
        minute = self.date_and_time.strftime("%M")
        ampm = self.date_and_time.strftime("%p")
        return (hour +":"+ minute + " " + ampm)