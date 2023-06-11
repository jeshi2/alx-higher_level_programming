#!/usr/bin/python3
"""
This is the "lazy_matrix_mul" module.
The lazy_matrix_mul matrix multiplication using numpy.dot
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
       Multiplies two Matrix
       Return: matrix
    """
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except Exception as e:
        raise TypeError("An error occurred during matrix multiplication") from e
