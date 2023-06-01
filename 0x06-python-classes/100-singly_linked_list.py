#!/usr/bin/python3
"""singly linked implementation in python"""


class Node:
    """a node instance of a single linked list"""

    def __init__(self, data, next_node=None):
        """
        Args:
            data (int): The data to be stored in the node.
                Raises a TypeError if data is not an integer.
            next_node (Node): The next node in the linked list. Defaults to None.
                Raises a TypeError if next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.
        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.
        Args:
            value (int): The data to be stored in the node.
                Raises a TypeError if value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.
        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.
        Args:
            value (Node): The next node in the linked list.
                Raises a TypeError if value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    Attributes:
        __head (Node): The head node of the linked list.
    """

    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node into the correct sorted position in the linked list.
        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
