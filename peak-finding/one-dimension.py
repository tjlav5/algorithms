import unittest

def findPeak(arr):

    length = len(arr)

    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr[0], arr[1])

    if arr[length / 2] < arr[length / 2 - 1]:
        return findPeak(arr[:(length / 2)])
    elif arr[length / 2] < arr[length / 2 + 1]:
        return findPeak(arr[length / 2 + 1:])
    else:
        return arr[length / 2]


class TestFindPeak(unittest.TestCase):
    def test_peak_left(self):
        self.assertEqual(findPeak([9, 8, 7, 6, 5]), 9)
        self.assertEqual(findPeak([9, 8, 7, 6, 5, 4]), 9)

    def test_peak_right(self):
        self.assertEqual(findPeak([5, 6, 7, 8, 9]), 9)
        self.assertEqual(findPeak([4, 5, 6, 7, 8, 9]), 9)

    def test_peak_middle(self):
        self.assertEqual(findPeak([1, 2, 3, 2, 1]), 3)

    def test_peak_middle_left(self):
        self.assertEqual(findPeak([8, 9, 10, 5, 4, 3, 2, 1]), 10)

    def test_peak_middle_right(self):
        self.assertEqual(findPeak([1, 2, 3, 4, 5, 6, 5, 4]), 6)


if __name__ == '__main__':
    unittest.main()