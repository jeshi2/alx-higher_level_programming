#!/usr/bin/python3
"""function that inherit from my list
"""

class MyList(list):
    """
    Custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
