import pygame
import random

# CONSTANTS
WIN_DIMENSIONS = (600, 600) # width, height
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_SIZE = 20
INITIAL_CELL_COUNT = 30
CELL_WIDTH = int(WIN_DIMENSIONS[0] / GRID_SIZE)
CELL_HEIGHT = int(WIN_DIMENSIONS[1] / GRID_SIZE)
UP, DOWN, LEFT, RIGHT = "up", "down", "left", "right"
DIRECTIONS = (UP, DOWN, LEFT, RIGHT, f"{UP}-{LEFT}", 
	f"{UP}-{RIGHT}", f"{DOWN}-{LEFT}", f"{DOWN}-{RIGHT}")
# ^CONSTANTS


def main():

	input("Left click to turn a cell on, right click to turn it off.\n\
	 When you are ready to run the simulation press space.\nNow press Enter to start :)")

	board_array = init_board_array()

	window = init_gui()

	time = pygame.time.Clock()

	key_pressed = False

	game_running = True
	while game_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				key_pressed = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				board_array = change_cell_status(board_array, mouse_pos)

		if 	key_pressed:
			board_array = update_board(board_array)

		window = update_gui(window, board_array)
		pygame.display.update()
		time.tick(1)




def init_gui():
	window = pygame.display.set_mode(WIN_DIMENSIONS)
	pygame.display.set_caption("Game of Life :)")
	window.fill(BLACK)
	return window


def change_cell_status(board_array, mouse_pos):
	# When the user clicks on a cell this function either kills or brings it to life.
	mouse_row = mouse_pos[1] // CELL_WIDTH
	mouse_column = mouse_pos[0] // CELL_HEIGHT
	if board_array[mouse_row][mouse_column] == 1:
		board_array[mouse_row][mouse_column] = 0
	else:
		board_array[mouse_row][mouse_column] = 1

	return board_array



def update_board(board_array):
	
	for row_num, row in enumerate(board_array):
		for column_num, column in enumerate(row):
			neighbours = get_cell_neighbours([row_num, column_num])
			num_live_neighbours = number_of_neighbours_alive(board_array, neighbours)

			if num_live_neighbours > 3 or num_live_neighbours < 2:
				board_array[row_num][column_num] = 0

			elif num_live_neighbours == 3:
				board_array[row_num][column_num] = 1

	print()
	for row in board_array:

		print(row)
	print()
	return board_array


def number_of_neighbours_alive(board_array, cell_neighbours):
	return sum(1 for cell in cell_neighbours if board_array[cell[0]][cell[1]] == 1)


def get_cell_neighbours(cell_index_array, direction = 0): #IMPLEMENT TESTS FOR THIS
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
	elif neighbour is not None and direction == 7:
		return [neighbour]
	elif neighbour is not None:
		return get_cell_neighbours(cell_index_array, direction + 1)
	else:
		return []


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
			if board_array[row_index][column_index] == 1:
				cell_colour = WHITE
			elif board_array[row_index][column_index] == 0:
				cell_colour = BLACK
			pygame.draw.rect(window, cell_colour, [column_index * CELL_WIDTH, row_index * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT])
	return window

			






if __name__ == "__main__":
	main()
