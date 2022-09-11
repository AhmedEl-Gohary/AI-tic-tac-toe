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
scores = {'x': 1, 'o': -1, 'tie': 0}

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

def checkWinner():
	winner = ''
	# checking row
	for i in range(3):
		if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
			winner = board[i][0]
	# checking col
	for i in range(3):
		if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
			winner = board[0][i]
	# checking diagonal
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		winner = board[0][0]
	# checking anti-diagonal
	if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		winner = board[1][1]
	if winner == '' and move_counter == 9:
		return 'tie'
	return winner


def minimax(board, alpha, beta, is_maximizing):
	result = checkWinner()
	if result != '':
		return scores[result]

	if is_maximizing:
		max_score = -math.inf
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					board[i][j] = 'x'
					score = minimax(board, alpha, beta, False)
					board[i][j] = ''
					max_score = max(score, max_score)
					alpha = max(alpha, score)
					if beta <= alpha:
						break
			else:
				continue
			break
		return max_score
	else:
		min_score = math.inf
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					board[i][j] = 'o'
					score = minimax(board, alpha, beta, True)
					board[i][j] = ''
					min_score = min(score, min_score)
					beta = min(beta, score)
					if beta <= alpha:
						break
			else:
				continue
			break
		return min_score


while True:
	drawBoard();
	pygame.display.update()
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
				pygame.display.update()

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
		best_score = -math.inf
		best_move = (0, 0)
		for i in range(3):
			for j in range(3):
				if board[i][j] == '':
					board[i][j] = 'x'
					score = minimax(board, -math.inf, math.inf, False)
					board[i][j] = ''
					if score > best_score:
						best_score = score
						best_move = (i, j)
					
		drawX(best_move[0], best_move[1])
		move_counter += 1
		board[best_move[0]][best_move[1]] = 'x'
		player_x = False
		winner = checkWinner()
		for i in range(3):
			print(board[i])

	if winner == 'x' or move_counter == 9:
		if winner == 'x':
			screen.blit(ai_surface, result_rect)
		else:
			screen.blit(tie_surface, result_rect)
		screen.blit(restart_surface, restart_rect)
		need_restart = True

	pygame.display.update()