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
        """Test invalid attribute values."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle("width", 10)
        self.assertEqual(str(e.exception), "width must be an integer")

        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, "height")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 10, "x")
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 10, 10, "y")
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 10)
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 10, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 10, 10, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

if __name__ == '__main__':
    unittest.main()
