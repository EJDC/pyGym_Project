class Staff:
    def __init__(self, first_name, last_name, email, monthly_invoice = 0.00, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.monthly_invoice = monthly_invoice
        self.id = id