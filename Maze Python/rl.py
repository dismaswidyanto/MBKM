import pygame
import random 
from Q_Learning import Q_Learning
from print_Qtable import print_Qtable
from travel import travel

#initialize pygame
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)

#make class block
class Block:
	def __init__(self, row, col, block_size, SIZE):
		self.row = row
		self.col = col
		self.x = row * block_size
		self.y = col * block_size
		self.block_size = block_size
		self.SIZE = SIZE
		self.color = WHITE
			
	def draw(self, window):
		pygame.draw.rect(window, self.color, (self.x, self.y, self.block_size, self.block_size))
		
	def make_start(self):
		self.color = GREEN
		
	def make_goal(self):
		self.color = RED
		
	def make_obstacle(self):
		self.color = BLACK
		
	def reset(self):
		self.color = WHITE


#make maze: make varible to store object Block
def make_maze(SIZE, window_size):
	block_size = window_size // SIZE
	maze = []
	for i in range(SIZE):
		maze.append([])
		for j in range(SIZE):
			block = Block(i, j, block_size, SIZE)
			maze[i].append(block)
			
	return maze

#draw maze: draw maze in pygame
def draw_maze(window, maze, SIZE, window_size):
	temp_size = SIZE
	block_size = window_size // SIZE
	window.fill(WHITE)
	
	#draw block rectangle
	for temp_size in maze:
		for block in temp_size:
			block.draw(window)
	
	#draw block line (hor, ver)
	for i in range(SIZE+1):
		pygame.draw.line(window, BLACK, (0, i * block_size), (window_size, i * block_size))
		pygame.draw.line(window, BLACK, (i * block_size, 0), (i * block_size, window_size))
	
	pygame.display.update()

#get_mouse_pos: get mouse position
def get_mouse_pos(block_size):
	mouse_x,mouse_y = pygame.mouse.get_pos()
	
	x = mouse_x // block_size
	y = mouse_y // block_size
	
	return x,y

#main program
def main():
	#parameter
	SIZE = 5
	window_size = 600
	block_size = window_size // SIZE
	alpha = 0.5
	gamma = 0.9
		
	#create maze for visual
	maze_vis = make_maze(SIZE, window_size)
	
	#create q-table
	Q_table = [[0 for i in range(4)] for j in range (SIZE*SIZE)]
	
	#create maze for RL
	maze_RL = [[0 for i in range(SIZE)] for j in range (SIZE)]
	
	#initalize pygame
	pygame.init()
	window = pygame.display.set_mode((window_size, window_size))
	
	#flag
	run = True
	start = None
	goal = None
	
	while run:
		draw_maze(window, maze_vis, SIZE, window_size)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print_Qtable(Q_table, SIZE)
				for i in range(SIZE):
					print(maze_RL[i])
				run = False
			
			#mouse input
			if pygame.mouse.get_pressed()[0]:
				col,row = get_mouse_pos(block_size)
				block = maze_vis[col][row]
				
				if not start and block != goal:
					start = block
					start.make_start()
					start_state = (row*SIZE) + col + 1
					maze_RL[row][col] = 2
				
				elif not goal and block != start:
					goal = block
					goal.make_goal()
					goal_state = (row*SIZE) + col + 1
					maze_RL[row][col] = 3
				
				elif block != start and block != goal:
					block.make_obstacle()
					maze_RL[row][col] = 1
				
			elif pygame.mouse.get_pressed()[2]:
				col,row = get_mouse_pos(block_size)
				block = maze_vis[col][row]
				block.reset()
				maze_RL[row][col] = 0
				if block == start:
					start = None
				elif block == goal:
					goal = None
					
			#keyboard input
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					Q_Learning(Q_table, alpha, gamma, maze_RL, start_state, goal_state, SIZE)
					print_Qtable(Q_table, SIZE)


#run main program
main()
