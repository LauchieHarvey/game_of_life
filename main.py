import pygame
import random

# CONSTANTS
WIN_DIMENSIONS = (600, 600) # width, height
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_SIZE = 40
CELL_WIDTH = int(WIN_DIMENSIONS[0] / GRID_SIZE)
CELL_HEIGHT = int(WIN_DIMENSIONS[1] / GRID_SIZE)
INITIAL_CELL_COUNT = 10
UP, DOWN, LEFT, RIGHT = "up", "down", "left", "right"
DIRECTIONS = (UP, DOWN, LEFT, RIGHT, f"{UP}-{LEFT}", 
	f"{UP}-{RIGHT}", f"{DOWN}-{LEFT}", f"{DOWN}-{RIGHT}")
# ^CONSTANTS


def main():

	board_array = init_board_array()

	window = init_gui()

	game_running = True
	while game_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				quit()

			update_board(board_array)

			update_gui(window, board_array)
			pygame.display.update()



def init_gui():
	window = pygame.display.set_mode(WIN_DIMENSIONS)
	pygame.display.set_caption("Game of Life :)")
	window.fill(BLACK)
	return window


def update_board(board_array):
	get_cell_neighbours([5, 5])



def get_cell_neighbours(cell_index_array, direction = 0):
	""" Returns a 2D tuple of the neighbours indexes.

			Parameters: 
				cell_index_array ([int, int]): A tuple in format (row, column) corresponding 
				to the cell position in the board_array function.

			Returns:
				([[int, int]...]): tuple containing the indexes of neighbouring cells
	"""
	neighbour = index_at_direction(cell_index_array, DIRECTIONS[direction])

	if neighbour is not None and direction != 7:
		return [neighbour,] + get_cell_neighbours(cell_index_array, direction + 1)
	elif direction == 7:
		return [neighbour]
	else:
		return get_cell_neighbours(cell_index_array, direction + 1)


def index_at_direction(cell_index_array, direction):
	""" Returns the index of the neighbouring cell in the given direction"""

	index_array = cell_index_array.copy()
	if (
		(index_array[1] == GRID_SIZE - 1 and RIGHT in direction) or
		(index_array[1] == 0 and LEFT in direction) or
		(index_array[0] == 0 and UP in direction) or
		(index_array[0] == GRID_SIZE - 1 and DOWN in direction)
		):
		return None

	if RIGHT in direction: 
		index_array[1] += 1
	elif LEFT in direction:
		index_array[1] -= 1
	if UP in direction:
		index_array[0] -= 1
	elif DOWN in direction:
		index_array[0] += 1


	return index_array



def init_board_array():
	board_array = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
	for cell in range(INITIAL_CELL_COUNT):
		board_array[random.randint(0, GRID_SIZE - 1)][random.randint(0, GRID_SIZE - 1)] = 1

	return board_array


def update_gui(window, board_array):
	for row_index, row_value in enumerate(board_array):
		for column_index, column_value in enumerate(row_value):
			if column_value == 1:
				pygame.draw.rect(window, WHITE, [column_index * CELL_WIDTH, row_index * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT])

			






if __name__ == "__main__":
	main()
