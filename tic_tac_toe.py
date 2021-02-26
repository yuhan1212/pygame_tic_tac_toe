import pygame as pg,sys
from pygame.locals import *
import time

# set up golbal variables and background size
XO = 'x'
winner = None
draw_result = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (100,10,10)

#TicTacToe 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]

#initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)

# set the name appears at the top of the display window
pg.display.set_caption("Tic Tac Toe")

#loading the images
opening = pg.image.load('images/opening.png')
x_img = pg.image.load('images/x.png')
o_img = pg.image.load('images/o.png')

#resizing images
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
opening = pg.transform.scale(opening, (width, height+100))

# function to start and restart the game
def game_opening():
    # In pygame, the blit() function is used on the surface
    # to draw an image on top of another image.
    # pg.display.update() is used to update the change
    screen.blit(opening,(0, 0))
    pg.display.update()
    # wait for one second
    time.sleep(1)
    screen.fill(white)
    # Drawing vertical lines
    pg.draw.line(screen,line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen,line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    # Drawing horizontal lines
    pg.draw.line(screen,line_color, (0,height / 3), (width, height / 3), 7)
    pg.draw.line(screen,line_color, (0,height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()

