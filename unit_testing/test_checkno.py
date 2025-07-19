import unittest
from number_value import check_no

class checking_number(unittest.TestCase):

    def setUp(self):
        self.number_value=check_no()

    def test_no(self):
       self.assertNotEqual(self.number_value.even_no(10),0,"this is not a even no")

    def test_add(self):
        self.assertEqual(self.number_value.add(10, 3), 13, "The actual sum does not match expected sum")

    def tearDown(self):
        del self.number_value

if __name__ == "__main__":
    unittest.main()