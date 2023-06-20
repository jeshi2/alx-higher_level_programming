#!/usr/bin/python3
"""test files testing base class with unitest"""
import unittest
from models.square import Square
import os

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_str(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update(self):
        s = Square(5)
        s.update(1, 10, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 10")
        s.update(id=2, x=5)
        self.assertEqual(str(s), "[Square] (2) 5/3 - 10")

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)
    def test_Square_update_exists_1(self):
        square = Square(4, 3, 2, 1)
        square.update(89)
        self.assertEqual(square.id, 89)

    def test_Square_update_exists_2(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_update_exists_3(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1, 2)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_update_exists_4(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1, 2, 3)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_update_exists_6(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89})
        self.assertEqual(square.id, 89)

    def test_Square_update_exists_7(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_update_exists_8(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_update_exists_9(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_create_exists_2(self):
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_create_exists_3(self):
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_create_exists_4(self):
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)


    def test_Square_creation_1(self):
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_Square_creation_2(self):
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_creation_3(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_size_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_Square_x_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_Square_y_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_Square_creation_4(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_Square_size_raise_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_Square_x_raise_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_Square_y_raise_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_Square_size_raise_value_error_2(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_Square_representation(self):
        square_repr = str(Square(1, 2, 3, 4))
        result = '[Square] (4) 2/3 - 1'
        self.assertEqual(square_repr, result)

    def test_Square_to_dictionary_exists(self):
        square_dict = Square(1, 2, 3, 4).to_dictionary()
        result = {
            'size': 1,
            'x': 2,
            'y': 3,
            'id': 4
        }
        self.assertEqual(square_dict, result)

    def test_Square_update_exists_1(self):
        square = Square(4, 3, 2, 1)
        square.update(89)
        self.assertEqual(square.id, 89)

    def test_Square_update_exists_2(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_update_exists_3(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1, 2)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_update_exists_4(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1, 2, 3)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_update_exists_6(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89})
        self.assertEqual(square.id, 89)

    def test_Square_update_exists_7(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_update_exists_8(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_update_exists_9(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_create_exists_2(self):
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_create_exists_3(self):
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_create_exists_4(self):
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

if __name__ == '__main__':
    unittest.main()
