class Customer:
    def __init__(self, first_name, last_name, dob, email, membership_level, membership_status, payment_method, extra_physio, extra_pt, extra_service_3, extra_service_4, missed_classes = 0,  monthly_bill = 0, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.membership_level = membership_level
        self.membership_status = membership_status
        self.payment_method = payment_method
        self.extra_physio = extra_physio
        self.extra_pt = extra_pt
        self.extra_service_3 = extra_service_3
        self.extra_service_4 = extra_service_4
        self.missed_classes = missed_classes
        self.monthly_bill = monthly_bill
        self.id = id
