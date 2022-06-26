import unittest
from models.category import Category

class TestCategory(unittest.TestCase):
    
    #Category Class Tests

    def setUp(self):
        self.category = Category("Plant", "Excavator", 1)

    def test_category_has_main(self):
        self.assertEqual("Plant", self.category.main_cat)

    def test_category_has_sub(self):
        self.assertEqual("Excavator", self.category.sub_cat)

    def test_category_has_id(self):
        self.assertEqual(1, self.category.id)