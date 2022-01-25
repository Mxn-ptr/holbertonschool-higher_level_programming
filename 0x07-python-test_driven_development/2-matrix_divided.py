#!/usr/bin/python3

""" Defines a divided matrix function """


def matrix_divided(matrix, div):
    """Function : matrix_divided
        Args:
                matrix: the matrix to be divided
                div: number to divide
        Raises:
                TypeError: If matrix is null or contains not int or float
                TypeError: If the matrix have differents sizes of row
                TypeError: If div is not an int or float
                ZeroDivisionErro: if div is 0
        Returns:
                New matrix with divided numbers """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        for elements in row:
            if ((not isinstance(elements, int)) and
                    (not isinstance(elements, float))):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    for row in matrix:
        if (not len(row) == len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
