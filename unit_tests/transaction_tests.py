import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):
    
    #Transaction Class Tests

    def setUp(self):
        self.transaction = Transaction(1, 2, "Concrete", 1000, "024180/JS", "2022-02-29", "0122197", 5)

    def test_transaction_has_supplier(self):
        self.assertEqual(1, self.transaction.supplier)

    def test_transaction_has_category(self):
        self.assertEqual(2, self.transaction.category)
    
    def test_transaction_has_product(self):
        self.assertEqual("Concrete", self.transaction.product)

    def test_transaction_has_price(self):
        self.assertEqual(1000, self.transaction.price)

    def test_transaction_has_ponumber(self):
        self.assertEqual("024180/JS", self.transaction.po_number)

    def test_transaction_has_date(self):
        self.assertEqual("2022-02-29", self.transaction.date)

    def test_transaction_has_invoice(self):
        self.assertEqual("0122197", self.transaction.invoice_number)

    def test_transaction_has_id(self):
        self.assertEqual(5, self.transaction.id)