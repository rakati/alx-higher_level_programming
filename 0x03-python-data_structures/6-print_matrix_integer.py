#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        print(' '.join('{:d}'.format(e) for e in line))
