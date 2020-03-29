# test file for main.py
import unittest
from main import *


class Test_non_void_functions(unittest.TestCase):

	def test_index_at_direction(self):
		# Tests index_at_direction with valid directions
		self.assertEqual(index_at_direction([5,5], LEFT), [5, 4])
		self.assertEqual(index_at_direction([5,5], RIGHT), [5, 6])
		self.assertEqual(index_at_direction([5,5], f"{UP}-{RIGHT}"), [4, 6])
		self.assertEqual(index_at_direction([5,5], f"{DOWN}-{LEFT}"), [6, 4])

	def test_invalid_index_at_direction_is_none(self):
		# Tests index_at_direction with invalid directions
		self.assertIsNone(index_at_direction([0, 0], LEFT))
		self.assertIsNone(index_at_direction([0, 0], UP))
		self.assertIsNone(index_at_direction([GRID_SIZE - 1, 4], DOWN))
		self.assertIsNone(index_at_direction([3, GRID_SIZE - 1], RIGHT))


	def test_get_cell_neighbours(self):
		self.assertEqual(get_cell_neighbours([3,3]), [[2,3], [4,3], [3,2], [3,4], [2,2], [2,4], [4,2], [4,4]])


if __name__ == "__main__":
	unittest.main()