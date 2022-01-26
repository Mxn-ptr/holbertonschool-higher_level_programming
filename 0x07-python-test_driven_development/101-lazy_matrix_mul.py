#!/usr/bin/python3

""" Define a function for multiplicate matrix """
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ lazy_matrix_mul
        Args:
            m_a (matrix): first matrix
            m_b (matrix): seconde matrix
    Return: mul matrix """
    return numpy.matmul(m_a, m_b)
