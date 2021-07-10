from django.test import TestCase

from app.calc import add,subtract

#testcase 1S
class CalcTests(TestCase):
    def test_add_nummbers(self):
         """ test that two number added together"""
         self.assertEqual(add(3,8),11)
    def test_subtract_numbers(self):
        """test that values are subtracted and returned"""
        self.assertEqual(subtract(5,11),-6)