from _sqlite3 import Row
import pygame
class Board:
    def __init__(self, squares, row, col, images):
        self.board = squares
        self.playable = True
        self.won = ""
        self.row = row
        self.col = col
        self.images  = images #Dict with images, keys: none, X, O
    def getSquare(self, row, col): #Returns the square in given row/col of this board
        return self.board[row][col]
    def checkWin(self):
            #Check for win
            #Top Row
            if (self.getSquare(0, 0).state == self.getSquare(0, 1).state and self.getSquare(0, 0).state == self.getSquare(0, 2).state and not self.getSquare(0, 0).state  == "none"):
                self.playable = False
                self.won = self.getSquare(0, 0).state
            #Middle Row
            elif (self.getSquare(1, 0).state == self.getSquare(1, 1).state and self.getSquare(1, 0).state == self.getSquare(1, 2).state and not self.getSquare(1, 0).state  == "none"):
                self.playable = False
                self.won = self.getSquare(1, 0).state
            #Last Row   
            elif (self.getSquare(2, 0).state == self.getSquare(2, 1).state and self.getSquare(2, 0).state == self.getSquare(2, 2).state and not self.getSquare(2, 0).state  == "none"):
                self.playable = False
                self.won = self.getSquare(2, 0).state
            #First Column
            elif (self.getSquare(0, 0).state == self.getSquare(1, 0).state and self.getSquare(0, 0).state == self.getSquare(2, 0).state and not self.getSquare(0, 0).state  == "none"):
                self.playable = False
                self.won = self.getSquare(0, 0).state
            #Middle Column
            elif (self.getSquare(0, 1).state == self.getSquare(1, 1).state and self.getSquare(0, 1).state == self.getSquare(2, 1).state and not self.getSquare(0, 1).state  == "none"):
                self.playable = False
                self.won = self.getSquare(0, 1).state
            #Last Column
            elif (self.getSquare(0, 2).state == self.getSquare(1, 2).state and self.getSquare(0, 2).state == self.getSquare(2, 2).state and not self.getSquare(0, 2).state  == "none"):
                self.playable = False
                self.won = self.getSquare(0, 2).state
            #TL -> BR 
            elif (self.getSquare(0, 0).state == self.getSquare(1, 1).state and self.getSquare(0, 0).state == self.getSquare(2, 2).state and not self.getSquare(0, 0).state  == "none"):
                self.playable = False
                self.won = self.getSquare(0, 0).state 
            #TR -> BL
            elif (self.getSquare(0, 2).state == self.getSquare(1, 1).state and self.getSquare(0, 2).state == self.getSquare(2, 0).state and not self.getSquare(0, 2).state  == "none"):
                self.playable = False
                self.won = self.getSquare(0, 2).state
    def update(self, screen): #Update display
        #If board has been claimed. Displays one large scaled version of winning letter/color
        if not self.won == "":
            image = self.images[self.won+str(self.col*3+self.row)]
            x,y = (image.get_width()*3*self.col+80, image.get_height()*3*self.row)
            screen.blit(pygame.transform.scale(image, (image.get_width()*3, image.get_height()*3)), (y,x))
        #If board is still playable
        elif self.playable:
            playable = False
            #Update every square to screen
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    self.board[i][j].update(screen, self.row, self.col)
            if self.playable: #Check if full and no win
                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if self.board[i][j].state == "none":
                            self.playable = True
                            playable = True
                            break
                if not playable:
                    self.playable = False
            self.checkWin() #Check if board has been won
        #If board has been filled but nobody wins. Displays a scaled version of the colored square blank.
        else:
            image = self.images["none"+str(self.col*3+self.row)]
            x,y = (image.get_width()*3*self.col+80, image.get_height()*3*self.row)
            screen.blit(pygame.transform.scale(image, (image.get_width()*3, image.get_height()*3)), (y,x))
            
                    