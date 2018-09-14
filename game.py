import pygame, sys, os
from Board import *
from GameController import *
from Square import *
'''
Author: Noah Saffie
Purpose: Final- Ultimate Tic-Tac-Toe a game about advanced Tic-Tac-Toe
Date: 5-17-2017
'''
#Initialize pygame
pygame.init()
pygame.font.init()

W,H = 540,620
screen = pygame.display.set_mode((W,H))
#Images
images = {}
for image in [f for f in os.listdir("images\\") if f.endswith('.png')]:
    key = image[0:len(image)-4]
    images[key] = pygame.image.load("images\\"+image).convert()
#SET TILE SIZE - Each tile must be same size for this system.
tileSize = 60

#Create fresh board
boards = []
for i in range(9):
    if i%3==0:
        boards.append([])
    boards[len(boards)-1].append(Board([[Square(row, col, images, i) for col in range(3)] for row in range(3)], i%3, len(boards)-1, images))
#Squares are objects respresented in a 2D array in each board.
#Squares are individually selected/playable spots
#Boards are objects represented in a 2D array in gamecontroller
#Boards are combination of squares that have a win condition
#Game controller is a combination of boards with a win conditon

#Start screen have options between 2-Player, AI
gc = GameController(boards) #Initialize gameController
gc.main_menu(screen) #Beginning start menu
while gc.playing:
    gc.update(screen) #Update gamecontroller which updates the entire game including taking in input
