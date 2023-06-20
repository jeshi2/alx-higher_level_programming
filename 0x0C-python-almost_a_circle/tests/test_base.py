#!/usr/bin/python3
import unittest
from models.base import Base

"""module test
"""


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_assignment(self):
        """
        Test id assignment when creating instances.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()
