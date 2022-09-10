import pygame

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