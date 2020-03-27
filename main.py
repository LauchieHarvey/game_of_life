import pygame

# CONSTANTS
WIN_DIMENSIONS = (600, 600) # width, height
BACKGROUND_COLOUR = (255, 255, 255)
GRID_SIZE = 20
CELL_WIDTH = int(WIN_DIMENSIONS[0] / GRID_SIZE)
CELL_HEIGHT = int(WIN_DIMENSIONS[1] / GRID_SIZE)
# ^CONSTANTS


def main():

	board_array = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
	board_array[4][4] = 1

	window = init_gui()

	game_running = True
	while game_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				quit()

			update_gui(window, board_array)
			pygame.display.update()



def init_gui():
	window = pygame.display.set_mode(WIN_DIMENSIONS)
	pygame.display.set_caption("Game of Life :)")
	window.fill(BACKGROUND_COLOUR)
	return window


def update_board(board_array):
	pass


def update_gui(window, board_array):
	for row_index, row_value in enumerate(board_array):
		for column_index, column_value in enumerate(row_value):
			if column_value == 1:
				cell_colour = (0, 0, 0)
			else:
				cell_colour = BACKGROUND_COLOUR

			pygame.draw.rect(window, cell_colour, [column_index * CELL_WIDTH, row_index * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT])






if __name__ == "__main__":
	main()
