import pygame as pg,sys
from pygame.locals import *
import time

# set up golbal variables and background
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)

#TicTacToe 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]

#initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
# set the name appears at the top of the display window
pg.display.set_caption("Tic Tac Toe")
