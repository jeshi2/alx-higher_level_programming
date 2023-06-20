#!/usr/bin/python3
"""
Unittests for the Square class.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Defines the test cases for the Square class."""

    def test_attributes(self):
        """Test attribute assignment when creating instances."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

        s2 = Square(10, 2, 3, 99)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 99)

    def test_size_validation(self):
        """Test size validation."""
        with self.assertRaises(ValueError):
            s = Square(-5)
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(TypeError):
            s = Square("size")

    def test_update(self):
        """Test update method."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(20, 8)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 0)
        s.update(30, 12, 6)
        self.assertEqual(s.id, 30)
        self.assertEqual(s.size, 12)
        self.assertEqual(s.x, 12)
        s.update(40, 14, 7, 4)
        self.assertEqual(s.id, 40)
        self.assertEqual(s.size, 14)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 7)

    def test_str(self):
        """Test __str__ method."""
        s = Square(5, 2, 3, 99)
        expected = "[Square] (99) 2/3 - 5"
        self.assertEqual(str(s), expected)


if __name__ == "__main__":
    unittest.main()
