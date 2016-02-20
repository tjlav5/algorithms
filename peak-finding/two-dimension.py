import unittest

def findPeak(matrix):

    print(matrix)

    j = len(matrix[0]) / 2

    col_max_row = float("-inf")
    col_max_val = float("-inf")
    for i in range(len(matrix)):
        if matrix[i][j] > col_max_val:
            col_max_val = matrix[i][j]
            col_max_row = i

    if len(matrix[0]) == 1:
        return col_max_val

    if matrix[i][j] < matrix[i][j - 1]:
        return findPeak([[column for column in row[:j]] for row in matrix])
    elif matrix[i][j] < matrix[i][j + 1]:
        return findPeak([[column for column in row[j+1:]] for row in matrix])
    else:
        return matrix[i][j]


class TestFindPeak(unittest.TestCase):

    def test_peak_left(self):

        arr = [
            [  1 ,  2 , 3],
            [  5 , 10 , 9],
            [ 17 ,  4 , 1]
        ]

        self.assertEqual(findPeak(arr), 17)
        # self.assertEqual(findPeak([9, 8, 7, 6, 5, 4]), 9)

    def test_no_peak(self):

        arr = [
            [  1 ,  1 , 1],
            [  1 ,  1 , 1],
            [  1 ,  1 , 1]
        ]

        self.assertEqual(findPeak(arr), 1)


if __name__ == '__main__':
    unittest.main()