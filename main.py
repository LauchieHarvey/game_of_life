import pygame
import random
from matplotlib import pyplot as plt
import numpy

# CONSTANTS

# You can change these to modify user experience:
GRID_SIZE = 50
INITIAL_CELL_COUNT = 0
WIN_DIMENSIONS = (800, 800) # width, height
WHITE = (140, 140, 140)
BLACK = (0, 0, 0)

# Leave these constants alone unless you know what you're doing:
CELL_WIDTH = int(WIN_DIMENSIONS[0] / GRID_SIZE)
CELL_HEIGHT = int(WIN_DIMENSIONS[1] / GRID_SIZE)
UP, DOWN, LEFT, RIGHT = "up", "down", "left", "right"
DIRECTIONS = (UP, DOWN, LEFT, RIGHT, f"{UP}-{LEFT}", 
	f"{UP}-{RIGHT}", f"{DOWN}-{LEFT}", f"{DOWN}-{RIGHT}")

# ^CONSTANTS^


def main():
	""" controls flow of the pygame gui, game algorithm and console output."""

	input("Left click in a square to turn the cell on or off.\n\
When you are ready to run the simulation press space.\nYou can press space at any time to pause\
\nIf you are paused, you can press the 'n' key to skip one step forward.\n\
Now press Enter to start :)")

	board_array = init_board_array()
	generation_cell_count_list = [0]
	window = init_gui()
	time = pygame.time.Clock()

	paused = True
	game_running = True
	while game_running:
		generation_cell_count = generation_cell_count_list[-1]
		key_pressed = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_running = False
				pygame.quit()
				break

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and not paused:
					paused = True
				elif event.key == pygame.K_SPACE and paused:
					paused = False

				elif paused and event.key == pygame.K_n:
					board_array, generation_cell_count = update_board(board_array, generation_cell_count)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				board_array, generation_cell_count = change_cell_status(board_array, 
					mouse_pos, generation_cell_count)
				generation_cell_count_list[-1] = generation_cell_count

		if not paused:
			board_array, generation_cell_count = update_board(board_array, generation_cell_count)
			generation_cell_count_list.append(generation_cell_count)

		if game_running:
			window = update_gui(window, board_array)
			pygame.display.update()
			time.tick(5)

	# Now the user has quit the main game we show them the graph.
	show_graph(generation_cell_count_list)




def init_gui():
	""" Initialises the Pygame graphical user interface and returns it."""
	window = pygame.display.set_mode(WIN_DIMENSIONS)
	pygame.display.set_caption("Game of Life :)")
	window.fill(BLACK)

	return window


def change_cell_status(board_array, mouse_pos, generation_cell_count):
	""" When the user clicks on a cell this function either kills or brings it to life.
			
			Parameters:
				board_array (list(list(int...))): The 2D list that holds the 
				dead or alive status of each cell
				mouse_pos (tuple(int, int)): The coordinate of the mouse on the pygame window (x, y)
				generation_cell_count (int): The number of cells alive in the generation.

			Returns:
				board_array (list(list(int...))): The updated 2D list that holds the status of each cell
				(int): The updated number of cells alive in the generation.
	"""

	mouse_row = mouse_pos[1] // CELL_WIDTH
	mouse_column = mouse_pos[0] // CELL_HEIGHT
	if board_array[mouse_row][mouse_column] == 1:
		board_array[mouse_row][mouse_column] = 0
		generation_cell_count -= 1
	else:
		board_array[mouse_row][mouse_column] = 1
		generation_cell_count += 1

	return (board_array, generation_cell_count)




def update_board(board_array, generation_cell_count):
	""" The main algorithm determining which cells stay alive and which die.

			Parameters:
				board_array (list(list(int...))): The 2D list that holds the 
				dead or alive status of each cell
				generation_cell_count (int): The number of cells alive in the generation.

			Returns:
				list(list(int, int...)): The updated board_array.
				(int): The updated number of cells alive in the generation.
	"""
	# Below is required to create a new variable all together instead of just a pointer to the same variable
	new_board_array = [row[:] for row in board_array]
	
	for row_num, row in enumerate(board_array):
		for column_num, column in enumerate(row):
			neighbours = get_cell_neighbours([row_num, column_num])
			num_live_neighbours = number_of_neighbours_alive(board_array, neighbours)

			if num_live_neighbours not in [3, 2]:
				# If the cell was previously alive decrement the generation cell count.
				if new_board_array[row_num][column_num] == 1:
					generation_cell_count -= 1
				new_board_array[row_num][column_num] = 0

			elif num_live_neighbours == 3:
				# If the cell was previously dead, add one to the generation cell count.
				if new_board_array[row_num][column_num] == 0:
					generation_cell_count += 1 
				new_board_array[row_num][column_num] = 1

	return (new_board_array, generation_cell_count)


def number_of_neighbours_alive(board_array, cell_neighbours):
	""" Returns the number of live cell neighbours of the given cell.

			Parameters:
				board_array (list(list(int, int...))): The 2D list representing the grid of cells
				cell_neighbours (list(int, int...)): A list of integers representing the indexes of
				cells surrounding a given cell.

			Returns:
				int: The total number of neighbours that are alive.
	"""
	return sum(1 for cell in cell_neighbours if board_array[cell[0]][cell[1]] == 1)


def get_cell_neighbours(cell_index_array):
	""" Returns a 2D array of the neighbours indexes.

			Parameters: 
				cell_index_array ([int, int]): A tuple in format (row, column) corresponding 
				to the cell position in the board_array function.

			Returns:
				([[int, int]...]): tuple containing the indexes of neighbouring cells
	"""
	neighbour_list = []
	for direction in DIRECTIONS:
		neighbour = index_at_direction(cell_index_array, direction)
		if neighbour != None:
			neighbour_list.append(neighbour)
	return neighbour_list




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
	""" Not currently being used. A function which generates a randomized starting grid.
	based off the number of the initial cell count constant.
	"""
	board_array = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
	for cell in range(INITIAL_CELL_COUNT):
		board_array[random.randint(0, GRID_SIZE - 1)][random.randint(0, GRID_SIZE - 1)] = 1

	return board_array


def update_gui(window, board_array):
	""" Changes the gui to reflect the current state of the board_array list."""
	for row_index, row_value in enumerate(board_array):
		for column_index, column_value in enumerate(row_value):
			if board_array[row_index][column_index] == 1:
				cell_colour = WHITE
			elif board_array[row_index][column_index] == 0:
				cell_colour = BLACK
			pygame.draw.rect(window, cell_colour, [column_index * CELL_WIDTH, row_index * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT])

	for row_number in range(GRID_SIZE):
		pygame.draw.line(window, WHITE, (CELL_WIDTH * row_number, 0), (CELL_WIDTH * row_number, WIN_DIMENSIONS[1]), 1)
		pygame.draw.line(window, WHITE, (0, row_number * CELL_HEIGHT), (WIN_DIMENSIONS[0], row_number * CELL_HEIGHT), 1)

	pygame.draw.line(window, WHITE, (WIN_DIMENSIONS[0] - 1, 0), (WIN_DIMENSIONS[0] - 1, WIN_DIMENSIONS[1]), 2)
	pygame.draw.line(window, WHITE, (0, WIN_DIMENSIONS[1] - 1), (WIN_DIMENSIONS[0], WIN_DIMENSIONS[1] - 1), 2)
	return window


def show_graph(generation_cell_count_list):
	""" Generates values for x axis and plots it on a graph

			Parameters:
				generation_cell_count_list (list(int)): The list of cell counts, one for each generation.

			Returns:
				Void.
	"""
	y_values = numpy.array(generation_cell_count_list)
	x_values = numpy.array([i for i in range(len(generation_cell_count_list))])
	plt.xticks(x_values)

	graph = plt.plot(x_values, y_values)
	plt.xlabel("Generations")
	plt.ylabel("Number of Cells Alive")

	plt.title("Number of Cells Alive by Generation")
	plt.show()

if __name__ == "__main__":
	main()