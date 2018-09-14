class Square:
    def __init__(self, x, y, images, boardNum):
        self.boardNum = boardNum
        self.state = "none"
        self.row = y #row
        self.col = x #column
        self.images  = images #Dict with images, keys: none, X, O
        self.width = images[self.state+str(self.boardNum)].get_width()
        self.height = images[self.state+str(self.boardNum)].get_height()
    def checkOpen(self):
        #Returns if square is available
        if self.state=="none":
            return True
        else:
            return False
    def update(self, screen, row, col):
        #updates the graphic of single square to the screen
        screen.blit(self.images[self.state+str(self.boardNum)], ((row*self.width*3)+self.row*self.width, (col*self.width*3)+self.col*self.height+80))