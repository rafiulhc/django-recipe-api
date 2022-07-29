from django.test import SimpleTestCase

from app.calc import add, subtract


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """
        test that two numbers are added together
        """
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract_numbers(self):
        """
        test numbers truely subtract
        """
        result = subtract(3,5)
        self.assertEqual(result, 2)
        