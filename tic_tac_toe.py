import pygame as pg, sys
from pygame.locals import *
import time


'''Change the images here'''

#loading the images 
opening = pg.image.load('images/tic-tac-toe.png')
x_img = pg.image.load('images/X.png')
o_img = pg.image.load('images/O.png')


'''Keep the rest unchanged'''

# take size of Tic Tac Toe (TTT) from user request (size range 9 ~ 100 square number)
TTT_size = int(input("Enter the Tic Tac Toe square size you want to play: "))
while TTT_size not in [9, 16, 25, 49, 64, 81, 100]:
	print("Sorry. The size should be a SQUARE number [9, 16, 25, 49, 64, 81, 100].")
	TTT_size = int(input("Enter the Tic Tac Toe size you want to play: "))

# the beginning status for TTT
OX_symbol: str = "O"     # start from 'O', and consists of O and X
winner = None            # not have winner yet
draw = False             # if all box filled and no winner, then draw

# set up original data and initialize global variables
_TTT_SIDE = int(TTT_size ** 0.5)               # if TTT_size is 9, TTT_side is 3
_SQUARE: int = 600                             # playground window size
_BOX_Length = _SQUARE / _TTT_SIDE              # length of each TTT box
_MARGIN = _BOX_Length / 4              # margin for each image and shapes drew
_IMAGE_SIZE: int = int(_BOX_Length - _MARGIN)  # image will be put in each box
_STATUS_HEIGHT: int = 100            # the status space is _SQUARE * _STATUS_HEIGHT

# set the name appears at the top of the display window
title = str(_TTT_SIDE) + "X" + str(_TTT_SIDE) + " Tic Tac Toe" 

# TicTacToe customized board, using list represent TTT, start consisting all None
TTT = []
for i in range (_TTT_SIDE):
    TTT += [[None] * _TTT_SIDE]

# initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((_SQUARE, _SQUARE + _STATUS_HEIGHT),0,32)
pg.display.set_caption(title)

# resizing images and background
x_img = pg.transform.scale(x_img, (_IMAGE_SIZE, _IMAGE_SIZE))
o_img = pg.transform.scale(o_img, (_IMAGE_SIZE, _IMAGE_SIZE))
opening = pg.transform.scale(opening, (_SQUARE, _SQUARE + _STATUS_HEIGHT))


def game_opening():
    # In pygame, the blit() function is used on the surface
    # to draw an image on top of another image.
    screen.blit(opening,(0,0))
    # pg.display.update() is used to update the change
    pg.display.update()
    # wait for one second
    time.sleep(1)
    screen.fill((255,255,255))
    
    # Drawing vertical lines
    i = 0
    while i < _TTT_SIDE + 1:
        pg.draw.line(screen,(0,0,0),(_BOX_Length * i, 0),(_BOX_Length * i, _SQUARE),7)
        i += 1
    
    # Drawing horizontal lines
    i = 0
    while i < _TTT_SIDE + 1:
        pg.draw.line(screen,(0,0,0),(0, _BOX_Length * i),(_SQUARE, _BOX_Length * i),7)
        i += 1
    
    draw_status()


def draw_status():
    global draw

    if winner is None:
        message = OX_symbol.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'

    font = pg.font.Font(None, 50)
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, _SQUARE, _SQUARE + _STATUS_HEIGHT, _STATUS_HEIGHT))
    text_rect = text.get_rect(center=(_SQUARE / 2, _SQUARE + _STATUS_HEIGHT / 2))
    screen.blit(text, text_rect)
    pg.display.update()