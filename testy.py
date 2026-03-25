import unittest
from unittest import TestCase

from PythonTasks_wyjatki_algorytmy_1 import bubble_sort_lambda

class Tests_BubbleSort(TestCase):
    def setUp(self):
        # create a instance of what we want test before every test
        self.input = [9, 8, 26, 11, 22]

    def tearDown(self):
        # clear the object after every test
        del self.input

    def test_ascending_bubble_sort(self):
        bubble_sort_lambda(self.input)
        self.assertEqual(self.input, [8, 9, 11, 22, 26])

    def test_descending_bubble_sort(self):
        bubble_sort_lambda(self.input, key=lambda x: -x)
        self.assertEqual(self.input, [26, 22, 11, 9, 8])

    def test_by_even_numbers_bubble_sort(self):
        bubble_sort_lambda(self.input, key=lambda x: (x % 2 == 0, x))
        self.assertEqual(self.input, [9, 11, 8, 22, 26])

    def test_by_odd_numbers_descending_bubble_sort(self):
        bubble_sort_lambda(self.input, key=lambda x: (x % 2 != 0, -x))
        self.assertEqual(self.input, [26, 22, 8, 11, 9])

# execute tests
if __name__ == "__main__":
    Tests_BubbleSort()