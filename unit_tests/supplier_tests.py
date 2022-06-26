import unittest
from models.supplier import Supplier

class TestSupplier(unittest.TestCase):
    
    #Supplier Class Tests

    def setUp(self):
        self.supplier = Supplier("Timber'R'Us", "42141512TRU", "John Doe", "100 West Street", "0141 241 2451", 2)

    def test_supplier_has_name(self):
        self.assertEqual("Timber'R'Us", self.supplier.supplier_name)

    def test_supplier_has_number(self):
        self.assertEqual("42141512TRU", self.supplier.supplier_number)
    
    def test_supplier_has_manager(self):
        self.assertEqual("John Doe", self.supplier.supplier_manager)

    def test_supplier_has_address(self):
        self.assertEqual("100 West Street", self.supplier.supplier_address)

    def test_supplier_has_phone(self):
        self.assertEqual("0141 241 2451", self.supplier.supplier_phone)

    def test_supplier_has_id(self):
        self.assertEqual(2, self.supplier.id)