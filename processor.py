import numpy as np


def print_menu():
    """Prints the matrix calculator menu."""
    print()
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')


def create_matrix():
    """Reads dimensions and content from input.
    Returns a numpy array matrix."""
    n, m = input('Enter size of matrix: ').strip().split()
    n, m = int(n), int(m)
    matrix = np.empty((n, m), dtype=float)
    print('Enter matrix rows:')
    for i in range(n):
        matrix[i] = input().strip().split()
    return matrix


def print_matrix(matrix):
    """Accepts a numpy array object and prints it the way JetBrains wants us to."""
    for row in matrix:
        row_string = ''
        for i in range(len(row)):
            row_string += str(row[i]) + ' '
        print(row_string)


def add_matrices(matrix1, matrix2):
    """Attempts to add two numpy arrays as matrices.
    If they can't be added, returns None."""
    if matrix1.shape == matrix2.shape:
        return matrix1 + matrix2


def multiply_matrices(matrix1, matrix2):
    """Attempts to perform matrix multiplication on two NumPy arrays.
    If the dimensions don't work out, returns None."""
    if len(matrix1[0]) == len(matrix2):
        return matrix1.dot(matrix2)


def transpose():
    """Provides a variety of matrix transpositions."""
    def print_transpose_menu():
        print()
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')

    def main_transpose(matrix):
        """Normal matrix transposition."""
        return matrix.transpose()

    def side_transpose(matrix):
        """Transposes a NumPy array matrix along its side diagonal."""
        n, m = matrix.shape
        new_matrix = np.empty((m, n), dtype=float)
        for i in range(m):
            for j in range(n):
                new_matrix[i][j] = matrix[m-j-1][n-i-1]
        return new_matrix

    def vertical_transpose(matrix):
        """Transposes a NumPy array matrix along a vertical median line."""
        return np.fliplr(matrix)

    def horizontal_transpose(matrix):
        """Transposes a NumPy array matrix along a horizontal median line."""
        return np.flipud(matrix)

    # transpose program
    print_transpose_menu()
    flip_type = int(input('Your choice: '))
    mat = create_matrix()
    print('The result is: ')
    if flip_type == 1:
        print_matrix(main_transpose(mat))
    elif flip_type == 2:
        print_matrix(side_transpose(mat))
    elif flip_type == 3:
        print_matrix(vertical_transpose(mat))
    elif flip_type == 4:
        print_matrix(horizontal_transpose(mat))


def invert_matrix(matrix):
    """Attempts to perform matrix inversion on a NumPy array.
    Returns none if inversion is not possible."""
    try:
        inverted = np.linalg.inv(matrix)
        return inverted
    except np.linalg.LinAlgError:
        return None


if __name__ == '__main__':
    # main loop
    while True:
        print_menu()
        action = int(input('Your choice: '))

        if action == 0:  # exit
            break
        elif action == 1:  # add matrices
            a = create_matrix()
            b = create_matrix()
            result = add_matrices(a, b)
            if result is None:
                print('These matrices cannot be added.')
            else:
                print('The result is:')
                print_matrix(result)
        elif action == 2:  # scalar multiplication
            a = create_matrix()
            c = float(input('Enter constant: ').strip())
            print('The result is:')
            print_matrix(c * a)
        elif action == 3:  # matrix multiplication
            a = create_matrix()
            b = create_matrix()
            result = multiply_matrices(a, b)
            if result is None:
                print('These matrices cannot be multiplied.')
            else:
                print('The result is:')
                print_matrix(result)
        elif action == 4:  # transpose
            transpose()
        elif action == 5:  # determinant
            a = create_matrix()
            result = np.linalg.det(a)
            print('The result is:')
            print(round(result, 2))
        elif action == 6:  # invert
            a = create_matrix()
            result = invert_matrix(a)
            if result is None:
                print("This matrix doesn't have an inverse.")
            else:
                print('The result is:')
                print_matrix(result)
        else:
            print('Invalid input')
