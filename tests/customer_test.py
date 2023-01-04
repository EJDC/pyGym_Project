import unittest
from models.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ned", "Flanders", 2-12-1967, "ned@flanders.com", "Standard", "Active", "Direct Debit", True, True, False, False)

    def test_customer_has_first_name(self):
        self.assertEqual("Ned", self.customer.first_name)

    def test_customer_has_second_name(self):
        self.assertEqual("Flanders", self.customer.last_name)

    def test_customer_has_dob(self):
        self.assertEqual(2-12-1967, self.customer.dob)
    
    def test_customer_has_email(self):
        self.assertEqual("ned@flanders.com", self.customer.email)

    def test_customer_has_membership_level(self):
        self.assertEqual("Standard", self.customer.membership_level)

    def test_customer_has_membership_status(self):
        self.assertEqual("Active", self.customer.membership_status)

    def test_customer_has_payment_method(self):
        self.assertEqual("Direct Debit", self.customer.payment_method)

 