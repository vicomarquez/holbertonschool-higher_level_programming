#!/usr/bin/python3i
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        len_2 = len(matrix[i])
        for y in range(len_2):
            if y != len_2 - 1:
                end = ' '
            else:
                end = ''
            print("{:d}".format(matrix[i][y]), end=end)
        print("")
