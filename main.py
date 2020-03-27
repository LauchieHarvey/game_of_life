import pygame
#import random as rand

# CONSTANTS
WIN_DIMENSIONS = (600, 600) # width, height
BACKGROUND_COLOUR = (255, 255, 255)
GRID_SIZE = 20
CELL_WIDTH = WIN_DIMENSIONS[0] / GRID_SIZE
CELL_HEIGHT = WIN_DIMENSIONS[1] / GRID_SIZE


# ^CONSTANTS

def main():
	window = init_gui()

	game_running = True
	while game_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
			pygame.display.update()



def init_gui():
	window = pygame.display.set_mode(WIN_DIMENSIONS)
	pygame.display.set_caption("Game of Life :)")
	window.fill(BACKGROUND_COLOUR)

	for row_num in range(GRID_SIZE):
		for column_num in range(GRID_SIZE):
			pygame.draw.rect(window, (0, 0, 0), [column_num * CELL_WIDTH, row_num * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT])

	return window


def initialise_board():
	pass



def update_board(board_array):
	pass


def update_gui(board_array):
	pass










if __name__ == "__main__":
	main()
