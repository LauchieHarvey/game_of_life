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


	def test_number_of_neighbours_alive(self):
		board_array = [
		[0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]
		cell_neighbours1 = [[0, 4], [2, 3], [1, 4], [1, 2], [0, 3], [0, 2], [2, 4], [2, 2]]
		cell_neighbours2 = [[0, 1], [1, 1], [1, 0]]
		cell_neighbours3 = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]

		# cell is board_array[1, 3]
		self.assertEqual(number_of_neighbours_alive(board_array, cell_neighbours1), 4)
		self.assertEqual(number_of_neighbours_alive(board_array, cell_neighbours2), 1)
		self.assertEqual(number_of_neighbours_alive(board_array, cell_neighbours3), 3)



if __name__ == "__main__":
	unittest.main()