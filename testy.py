import unittest
from unittest import TestCase

from PythonTasks_wyjatki_algorytmy_1 import bubble_sort_lambda
from PythonTasks_Zadania_akademickie_2 import give_value

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

class Tests_give_value(TestCase):
    def setUp(self):
        self.input = 0

    def tearDown(self):
        del self.input

    def test_give_number_int_less_than(self):
        self.input = -1
        self.assertEqual(give_value(self.input), 0)

    def test_give_number_int_more_than(self):
        self.input = 101
        self.assertEqual(give_value(self.input), 100)

    def test_give_number_int_eq_max(self):
        self.input = 100
        self.assertEqual(give_value(self.input), 100)

    def test_give_number_int_eq_min(self):
        self.input = 0
        self.assertEqual(give_value(self.input), 0)

    def test_give_number_int_valid_value(self):
        self.input = 50
        self.assertEqual(give_value(self.input), 50)

    def test_give_number_str(self):
        self.input = "-1"
        self.assertEqual(give_value(self.input), 0)

    def test_give_number_float(self):
        self.input = 100.5
        self.assertEqual(give_value(self.input), 100)

    def test_give_number_bool_True(self):
        self.input = True
        self.assertEqual(give_value(self.input), 1)

    def test_give_number_bool_False(self):
        self.input = False
        self.assertEqual(give_value(self.input), 0)

    def test_give_number_list(self):
        self.input = [1,2,3]
        with self.assertRaises(TypeError):
            give_value(self.input)

    def test_give_number_tuple(self):
        self.input = (1,2)
        with self.assertRaises(TypeError):
            give_value(self.input)

    def test_give_number_set(self):
        self.input = {1}
        with self.assertRaises(TypeError):
            give_value(self.input)

    def test_give_number_dict(self):
        self.input = {1: 0}
        with self.assertRaises(TypeError):
            give_value(self.input)


# execute tests
if __name__ == "__main__":
    Tests_BubbleSort()
    Tests_give_value()