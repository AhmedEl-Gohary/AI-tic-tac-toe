import pygame, sys, time, math

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
need_restart = False
winner = ''

# Screen settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe AI")
screen.fill(BACKGROUND)
result_font = pygame.font.Font('Pixeltype.ttf', 160)
restart_font = pygame.font.Font('Pixeltype.ttf', 90)
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

def drawX(i, j):
	min_x = max_x = 400 * j + 200
	min_y = max_y = 400 * i + 200
	min_x -= 80
	max_x += 80
	min_y -= 80
	max_y += 80
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

	return ''

def minimax(board):
	return 1


while True:
	drawBoard();
	# checking for user input
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if need_restart and event.type == pygame.KEYDOWN:
			if event.key ==  pygame.K_SPACE:
				winner = ''
				move_counter = 0
				player_x = True
				screen.fill(BACKGROUND)
				drawBoard()
				for r in range(3):
					for c in range(3):
						board[r][c] = ''
				need_restart = False

		if event.type == pygame.MOUSEBUTTONDOWN and not player_x and not need_restart:
			if event.button == 1:
				mx, my = pygame.mouse.get_pos()
				mx = center(mx)
				my = center(my)
				x, y = boardCoord(mx, my)
				if  board[x][y] == '':
					drawO(mx, my)
					board[x][y] = 'o'
					player_x = True
					move_counter += 1

	if player_x and move_counter < 9 and not need_restart:
		best_move = (0, 0)
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					best_move = (i, j)
					break
			else:
				continue
			break

		drawX(best_move[0], best_move[1])
		move_counter += 1
		board[best_move[0]][best_move[1]] = 'x'
		winner = checkWinner(best_move[0], best_move[1], 'x')
		if winner != 'x':
			player_x = False

	if winner == 'x' or move_counter == 9:
		if winner == 'x':
			screen.blit(ai_surface, result_rect)
		else:
			screen.blit(tie_surface, result_rect)
		screen.blit(restart_surface, restart_rect)
		need_restart = True

	pygame.display.update()