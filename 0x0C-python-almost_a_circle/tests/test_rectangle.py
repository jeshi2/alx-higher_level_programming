#!/usr/bin/python3
"""test for rectangle with unittest"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import turtle
from unittest.mock import patch
from io import StringIO
import io
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """class for testing"""
    def test_constructor_1(self):
        r = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_to_dictionary(self):
        r = Rectangle(10, 5, 2, 3, 1)
        expected_dict = {
            "id": 1,
            "width": 10,
            "height": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_width_getter_setter(self):
        r = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r.width, 10)
        r.width = 20
        self.assertEqual(r.width, 20)
        with self.assertRaises(TypeError):
            r.width = "invalid"

    def test_height_getter_setter(self):
        r = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r.height, 5)
        r.height = 8
        self.assertEqual(r.height, 8)
        with self.assertRaises(TypeError):
            r.height = "invalid"

    def test_x_getter_setter(self):
        r = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r.x, 2)
        r.x = 4
        self.assertEqual(r.x, 4)
        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(ValueError):
            r.x = -3

    def test_y_getter_setter(self):
        r = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r.y, 3)
        r.y = 6
        self.assertEqual(r.y, 6)
        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.y = -2

    def test_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(2, 2)
        input_string = io.StringIO()
        res_str = "##\n##\n"
        with redirect_stdout(input_string):
            r.display()
        self.assertEqual(res_str, input_string.getvalue())

        r.x = 1
        res_str = " ##\n ##\n"
        input_string = io.StringIO()
        with redirect_stdout(input_string):
            r.display()
        self.assertEqual(res_str, input_string.getvalue())


    def test_str(self):
        r = Rectangle(10, 5, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 10/5"
        self.assertEqual(str(r), expected_str)

    def test_update_args(self):
        r = Rectangle(10, 5, 2, 3, 1)
        r.update(2, 8, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)

    def test_update_kwargs(self):
        r = Rectangle(10, 5, 2, 3, 1)
        r.update(width=8, height=6, x=4)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 4)

    def test_constructor_2(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_constructor_3(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_constructor_4(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_constructor_5(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_type(self):
        self.assertRaises(TypeError, Rectangle, "1", 1)
        self.assertRaises(TypeError, Rectangle, width='2')
        self.assertRaises(TypeError, Rectangle, width=float('NaN'))
        self.assertRaises(TypeError, Rectangle, width=float('inf'))
        self.assertRaises(TypeError, Rectangle, 1, height='abc')
        self.assertRaises(TypeError, Rectangle, 1, 1, x={})
        self.assertRaises(TypeError, Rectangle, 1, 1, y=2.5)

    def test_value(self):
        self.assertRaises(ValueError, Rectangle, -5, 1)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -565)
        self.assertRaises(ValueError, Rectangle, 1, 1, -755)
        self.assertRaises(ValueError, Rectangle, 1, 1, -2)
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_rectangle_representation(self):
        rect_repr = str(Rectangle(1, 2, 3, 4, 5))
        result = '[Rectangle] (5) 3/4 - 1/2'
        self.assertEqual(rect_repr, result)

    def test_rectangle_update_exists_1(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89)
        self.assertEqual(rect.id, 89)

    def test_rectangle_update_exists_2(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_rectangle_update_exists_3(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_update_exists_4(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2, 3)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_update_exists_5(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2, 3, 4)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_exists_6(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89})
        self.assertEqual(rect.id, 89)

    def test_rectangle_update_exists_7(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_rectangle_update_exists_8(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_update_exists_9(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_update_exists_10(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_create_exists_3(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_create_exists_4(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_create_exists_5(self):
        rect = Rectangle.create(**{
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
        })
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_basic_display(self):
        r = Rectangle(2, 2)
        input_string = io.StringIO()
        res_str = "##\n##\n"
        with redirect_stdout(input_string):
            r.display()
        self.assertEqual(res_str, input_string.getvalue())

        r.x = 1
        res_str = " ##\n ##\n"
        input_string = io.StringIO()
        with redirect_stdout(input_string):
            r.display()
        self.assertEqual(res_str, input_string.getvalue())

if __name__ == '__main__':
    unittest.main()
