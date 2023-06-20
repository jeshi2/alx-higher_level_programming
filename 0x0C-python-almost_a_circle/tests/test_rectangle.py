#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""defined test module
"""


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_attributes(self):
        """
        Test attribute assignment when creating instances.
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_invalid_attributes(self):
        """
        Test invalid attribute values.
        """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            Rectangle(10, -2)

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -5

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.height = -5

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.x = "abc"

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.y = 3.14

if __name__ == '__main__':
    unittest.main()
