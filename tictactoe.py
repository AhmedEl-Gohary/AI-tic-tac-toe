import pygame, sys, time

pygame.init()

# Initializing constants
WIDTH = 1200
HEIGHT = 1400
O_COLOR = '#026165'
X_COLOR = '#f1f1f1'
BACKGROUND = '#649ca3'
GRID = '#deb987'

board = [['']*3, ['']*3, ['']*3]
player_x = True
move_counter = 0
restart = False
winner = ''

# Screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe AI")
screen.fill(BACKGROUND)
result_font = pygame.font.Font('font/Pixeltype.ttf', 160)
restart_font = pygame.font.Font('font/Pixeltype.ttf', 90)
ai_surface = result_font.render('AI  WON!', False, (64, 64, 64))
tie_surface = result_font.render('It\'s a Tie!', False, (64, 64, 64))
restart_surface = restart_font.render('Press Space to restart', False, (64, 64, 64))
restart_rect = restart_surface.get_rect(topleft = (530, 1300))
result_rect = ai_surface.get_rect(topleft = (50, 1280))

# Game functions
def drawBoard():
	for start in range(WIDTH // 3, WIDTH, WIDTH // 3):
		pygame.draw.line(screen, GRID, (start, 50), (start, 1150), 12)
		pygame.draw.line(screen, GRID, (50, start), (1150, start), 12)

def drawX(min_x, max_x, min_y, max_y):
	pygame.draw.line(screen, X_COLOR, (min_x, min_y), (max_x, max_y), 26)
	pygame.draw.line(screen, X_COLOR, (max_x, min_y), (min_x, max_y), 26)
	pygame.display.update()

def drawO(x, y):
	pygame.draw.circle(screen, O_COLOR, (x, y), 100, 22)
	pygame.display.update()

def center(pos):
	if pos <= 400: pos = 200
	elif pos <= 800: pos = 600
	else: pos = 1000
	return pos

def boardCoord(x, y):
	j = 0 if x == 200 else 1 if x == 600 else 2
	i = 0 if y == 200 else 1 if y == 600 else 2
	return (i, j)

def checkWinner(x, y, player):
	# only checking the corrsponding row/col/diag for a more effecient search
	# checking row
	for i in range(3):
		if board[i][y] != player: break
		if i == 2: return player
	# checking col
	for i in range(3):
		if board[x][i] != player: break
		if i == 2: return player
	# checking diagonal
	if x == y:
		for i in range(3):
			if board[i][i] != player: break
			if i == 2: return player
	# checking anti-diagonal
	if x + y == 2:
		for i in range(3):
			if board[i][2 - i] != player: break
			if i == 2: return player

while True:
	drawBoard();
	# checking for user input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mx, my = pygame.mouse.get_pos()
				mx = center(mx)
				my = center(my)
				i, j = boardCoord(mx, my)
				if board[i][j] == '':
					if player_x:
						min_x, min_y = mx - 80, my - 80
						max_x, max_y = mx + 80, my + 80
						drawX(min_x, max_x, min_y, max_y)
						board[i][j] = 'x'
						winner = checkWinner(i, j, 'x')
						if winner == 'x':
							screen.blit(ai_surface, result_rect)
							screen.blit(restart_surface, restart_rect)
						else: 
							player_x = False
					else:
						drawO(mx, my)
						board[i][j] = 'o'
						player_x = True

					for i in range(3):
						print(board[i])

					move_counter += 1
		if move_counter == 9 or winner == 'x':
			if winner == 'x':
				screen.blit(ai_surface, result_rect)
			else:
				screen.blit(tie_surface, result_rect)
			screen.blit(restart_surface, restart_rect)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					restart = True
		if restart:
			winner = ''
			move_counter = 0
			player_x = True
			screen.fill(BACKGROUND)
			drawBoard()
			for r in range(3):
				for c in range(3):
					board[r][c] = ''
			restart = False
	pygame.display.update()