import pygame, sys, random, time
from pygame.time import wait
class GameController:
    def __init__(self, boards, pvp=False):
        self.boards = boards #2D List
        self.currentBoard = None
        self.imageWidth = 60
        self.imageHeight = 60
        self.PvP = pvp
        self.number = 0.00
        self.playing = True
        self.currentPlayer = 0 #0 or 1
        self.anyImg = pygame.image.load("images\\any.png").convert()
    def getLetter(self): #Returns the letter of the current player
        letters = ["X", "O"]
        return letters[self.currentPlayer]
    def rules_menu(self, screen): #Display of rules page
        W=screen.get_width()
        H=screen.get_height()
        font=pygame.font.SysFont(None, 18)
        font2=pygame.font.SysFont(None, 28)
        menuOpen = True
        #rules
        color = (0,0,0)
        lines = [font2.render("Welcome to Ultimate Tic-Tac-Toe", True, color),
                     font.render("This is Tic-Tac-Toe with a twist.", True, color),
                     font.render("All you need to do is left-click the mouse.", True, color),
                     font.render("When you click a square, the next player must use the colored grid", True, color),
                     font.render("that corresponds to the square clicked relative to whole board.", True, color),
                     font.render("Example if you click the upper-left square in a given colored board the", True, color),
                     font.render("next player must play on the colored board on the upper left on the screen", True, color),
                     font.render("Who is playing and the current board color can be seen at top of the screen.", True, color),
                     font.render("If the next board to be played is completely full or already claimed", True, color),
                     font.render("then ANY free square can be picked.", True, color),
                     font.render("A \"Board\" is represented as nine squares of the same color.", True, color),
                     font.render("You win the game by capturing three boards in a specific pattern.", True, color),
                     font.render("The pattern is three squares in a row, column, or diagonal.", True, color),
                     font.render("Each Board can be captured according to this same pattern.", True, color),
                     font.render("Good luck!", True, color)]
        height = lines[0].get_height()
        while menuOpen:
            #If hit escape go to main_menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.K_ESCAPE:
                    self.main_menu(screen)
                    menuOpen = False
                    break
            screen.fill((255,255,255))
            backButton = pygame.Rect(W/2-int(.25*W), int(.8*H), int(.5*W), int(.125*H))
            backText = font.render("Main Menu", True, (255,255,255))
            #back button code
            if backButton.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (150, 50,50), backButton)
                pygame.draw.rect(screen, (150, 255,50), backButton,3)
                if pygame.mouse.get_pressed()[0]==1:
                    self.main_menu(screen)
                    menuOpen = False
            else:
                pygame.draw.rect(screen, (225, 50,50), backButton)
                pygame.draw.rect(screen, (0, 50,255), backButton,1)
            screen.blit(backText,(backButton.x+(backButton.width-backText.get_width())//2,backButton.y+(backButton.height-backText.get_height())//2))
            
            for i in range(len(lines)): #Blit all of the rules to the screen
                screen.blit(lines[i], ((W-lines[i].get_width())//2,(height+12)*i+20))
            pygame.display.flip() #Update screen
    def main_menu(self, screen): #main menu graphic
        W=screen.get_width()
        H=screen.get_height()
        font=pygame.font.SysFont(None, 28)
        tfont=pygame.font.SysFont(None, 28)
        #Setup of text ussed in main menu
        titleText = tfont.render("Ultimate Tic Tac Toe - Main Menu",True,(50,50,250))
        Player1 = pygame.Rect(W/2-int(.25*W), int(.2*H), int(.5*W), int(.125*H))
        PlayerText1 = font.render("Start Game - 1 Player", True, (255,255,255))
        Player2 = pygame.Rect(W/2-int(.25*W), int(.35*H), int(.5*W), int(.125*H))
        PlayerText2 = font.render("Start Game - 2 Player", True, (255,255,255))
        rulesButton = pygame.Rect(W/2-int(.25*W), int(.50*H), int(.5*W), int(.125*H))
        rulesText = font.render("Rules", True, (255,255,255))
        quitButton = pygame.Rect(W/2-int(.25*W), int(.65*H), int(.5*W), int(.125*H))
        quitText = font.render("Quit Game", True, (255,255,255))
        #Loop to keep menu open for appropriate time
        menuOpen = True
        while menuOpen:
            #draw menu background 
            screen.fill((255,255,255))
            screen.blit(titleText, (W/2-titleText.get_width()/2, 20))
            #1 player mode button
            if Player1.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (150, 50,50), Player1)
                pygame.draw.rect(screen, (150, 255,50), Player1,3)
                if pygame.mouse.get_pressed()[0]==1:
                    menuOpen=False
                    self.PvP = False
            else:
                pygame.draw.rect(screen, (225, 50,50), Player1)
                pygame.draw.rect(screen, (0, 50,255), Player1,1)
            
            screen.blit(PlayerText1,(Player1.x+(Player1.width-PlayerText1.get_width())//2,Player1.y+(Player1.height-PlayerText1.get_height())//2))
            #2 player mode button
            if Player2.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (150, 50,50), Player2)
                pygame.draw.rect(screen, (150, 255,50), Player2,3)
                if pygame.mouse.get_pressed()[0]==1:
                    menuOpen=False
                    self.PvP = True
            else:
                pygame.draw.rect(screen, (225, 50,50), Player2)
                pygame.draw.rect(screen, (0, 50,255), Player2,1)
            
            screen.blit(PlayerText2,(Player2.x+(Player2.width-PlayerText2.get_width())//2,Player2.y+(Player2.height-PlayerText2.get_height())//2))
            #Rules button
            if rulesButton.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (150, 50,50), rulesButton)
                pygame.draw.rect(screen, (150, 255,50), rulesButton,3)
                if pygame.mouse.get_pressed()[0]==1:
                    self.rules_menu(screen)
            else:
                pygame.draw.rect(screen, (225, 50,50), rulesButton)
                pygame.draw.rect(screen, (0, 50,255), rulesButton,1)
            screen.blit(rulesText,(rulesButton.x+(rulesButton.width-rulesText.get_width())//2,rulesButton.y+(rulesButton.height-rulesText.get_height())//2))
            #Quit button code
            if quitButton.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (150, 50,50), quitButton)
                pygame.draw.rect(screen, (150, 255,50), quitButton,3)
                if pygame.mouse.get_pressed()[0]==1:
                    pygame.quit()
                    sys.exit()
            else:
                pygame.draw.rect(screen, (225, 50,50), quitButton)
                pygame.draw.rect(screen, (0, 50,255), quitButton,1)
            screen.blit(quitText,(quitButton.x+(quitButton.width-quitText.get_width())//2,quitButton.y+(quitButton.height-quitText.get_height())//2))
            pygame.display.flip() #Update screen
            #Able to leave screen by hitting top red x
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    def pauseMenu(self, screen): #Pause menu graphic
        W=screen.get_width()
        H=screen.get_height()
        font=pygame.font.SysFont(None, 28)
        tfont=pygame.font.SysFont(None, 28)
        titleText = tfont.render("Pause Menu",True,(50,50,250))
        #start = Resume
        startButton1 = pygame.Rect(W/2-int(.25*W), int(.2*H), int(.5*W), int(.125*H))
        startText1 = font.render("Resume Game", True, (255,255,255))
        quitButton = pygame.Rect(W/2-int(.25*W), int(.50*H), int(.5*W), int(.125*H))
        quitText = font.render("Quit Game", True, (255,255,255))
    
        menuOpen = True
        while menuOpen:
            #draw menu background 
            screen.fill((255,255,255))
            screen.blit(titleText, (W/2-titleText.get_width()/2, 20))
            #Start button code
            if startButton1.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (150, 50,50), startButton1)
                pygame.draw.rect(screen, (150, 255,50), startButton1,3)
                if pygame.mouse.get_pressed()[0]==1:
                    menuOpen=False
            else:
                pygame.draw.rect(screen, (225, 50,50), startButton1)
                pygame.draw.rect(screen, (0, 50,255), startButton1,1)
            
            screen.blit(startText1,(startButton1.x+(startButton1.width-startText1.get_width())//2,startButton1.y+(startButton1.height-startText1.get_height())//2))#Quit button code
            #Quit button code
            if quitButton.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (150, 50,50), quitButton)
                pygame.draw.rect(screen, (150, 255,50), quitButton,3)
                if pygame.mouse.get_pressed()[0]==1:
                    pygame.quit()
                    sys.exit()
            else:
                pygame.draw.rect(screen, (225, 50,50), quitButton)
                pygame.draw.rect(screen, (0, 50,255), quitButton,1)
            screen.blit(quitText,(quitButton.x+(quitButton.width-quitText.get_width())//2,quitButton.y+(quitButton.height-quitText.get_height())//2))
            pygame.display.flip() #Update to screen
            #Allow to exit by hitting quit in corner
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    def checkSquare(self, board, row, col): #Check square at given board/row/col and seen if playable
        if not board.playable:
            return False
        else:
            return board.getSquare(row, col).checkOpen()
    def check_input(self, screen):
        #Check input of player and respond properly
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: #Check for ESCAPE key to pull up pause menu
            self.pauseMenu(screen)
        HeaderSize = 80 #Offset used for parsing y coordinates of click to something easier to interpret
        if (self.PvP): #If 2 player mode was selected
                for event in pygame.event.get():
                    #Check for click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = pygame.mouse.get_pos()
                        y-=HeaderSize #Make coords easier to parse to row/column
                        boardRow = y//(self.imageHeight*3)
                        boardCol = x//(self.imageWidth*3)
                        squareRow = (y//self.imageHeight)%3
                        squareCol = (x//self.imageWidth)%3
                        #Check if square clicked is playable
                        if((self.currentBoard == self.boards[boardRow][boardCol] or self.currentBoard==None) and self.checkSquare(self.boards[boardRow][boardCol], squareRow, squareCol) and self.boards[boardRow][boardCol].playable):
                            self.boards[boardRow][boardCol].getSquare(squareRow, squareCol).state = self.getLetter()
                            self.boards[boardRow][boardCol].checkWin()
                            #Check if the next board to be played is available or if any should be available
                            if self.boards[squareRow][squareCol].playable:
                                self.currentBoard = self.boards[squareRow][squareCol]
                            else:
                                self.currentBoard = None
                            self.changePlayer()
                        else:
                            #If square is full tell player
                            self.occupied(screen)
                    else:
                        pass
        else:
            #For 1 player mode, vs AI
            if self.currentPlayer==0:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = pygame.mouse.get_pos()
                        y-=HeaderSize #Make coords easier to parse to row/column
                        boardRow = y//(self.imageHeight*3)
                        boardCol = x//(self.imageWidth*3)
                        squareRow = (y//self.imageHeight)%3
                        squareCol = (x//self.imageWidth)%3
                        #print self.checkSquare(self.boards[boardRow][boardCol], squareRow, squareCol)
                        if((self.currentBoard == self.boards[boardRow][boardCol] or self.currentBoard==None) and self.checkSquare(self.boards[boardRow][boardCol], squareRow, squareCol)):
                            self.boards[boardRow][boardCol].getSquare(squareRow, squareCol).state = self.getLetter()
                            self.boards[boardRow][boardCol].checkWin()
                            if self.boards[squareRow][squareCol].playable:
                                self.currentBoard = self.boards[squareRow][squareCol]
                            else:
                                self.currentBoard = None
                            self.changePlayer()
                        else:
                            self.occupied(screen)
                    else:
                        pass
            else:
                #AI
                time.sleep(1) #make pace feel more natural
                #If a board isnt selected, select one at random
                while self.currentBoard == None:
                    row = random.randint(0,2)
                    col = random.randint(0,2)
                    if self.boards[row][col].playable:
                        self.currentBoard = self.boards[row][col]
                '''
                if self.currentBoard ==None:
                    if (self.boards[1][1].playable):
                        self.currentBoard = self.boards[1][1]
                    elif (self.boards[0][0].playable):
                        self.currentBoard = self.boards[0][0]
                    elif (self.boards[0][2].playable):
                        self.currentBoard = self.boards[0][2]
                    elif (self.boards[2][0].playable):
                        self.currentBoard = self.boards[2][0]
                    elif (self.boards[2][2].playable):
                        self.currentBoard = self.boards[0][0]
                    else:
                        while self.currentBoard == None:
                            row = random.randint(0,2)
                            col = random.randint(0,2)
                            if self.boards[row][col].playable:
                                self.currentBoard = self.boards[row][col]
                '''
                #"smart" AI felt too obvious and predictable went for pure random
                '''
                if self.checkSquare(self.currentBoard, 1, 1):
                    self.currentBoard.getSquare(1, 1).state = self.getLetter()
                    self.changePlayer()
                    if self.boards[1][1].playable:
                        self.currentBoard = self.boards[1][1]
                    else:
                        self.currentBoard = None
                elif self.checkSquare(self.currentBoard, 0, 0):
                    self.currentBoard.getSquare(0, 0).state = self.getLetter()
                    self.changePlayer()
                    if self.boards[0][0].playable:
                        self.currentBoard = self.boards[0][0]
                    else:
                        self.currentBoard = None
                elif self.checkSquare(self.currentBoard, 0, 2):
                    self.currentBoard.getSquare(0, 2).state = self.getLetter()
                    self.changePlayer()
                    if self.boards[0][2].playable:
                        self.currentBoard = self.boards[0][2]
                    else:
                        self.currentBoard = None
                elif self.checkSquare(self.currentBoard, 2, 0):
                    self.currentBoard.getSquare(2, 0).state = self.getLetter()
                    self.changePlayer()
                    if self.boards[2][0].playable:
                        self.currentBoard = self.boards[2][0]
                    else:
                        self.currentBoard = None
                elif self.checkSquare(self.currentBoard, 2, 2):
                    self.currentBoard.getSquare(2, 2).state = self.getLetter()
                    self.changePlayer()
                    if self.boards[2][2].playable:
                        self.currentBoard = self.boards[2][2]
                    else:
                        self.currentBoard = None
                else:
                    while True:
                        row = random.randint(0, 2)
                        col = random.randint(0,2)
                        if self.checkSquare(self.currentBoard, row, col):
                            self.currentBoard.getSquare(row, col).state = self.getLetter()
                            self.changePlayer()
                            if self.boards[row][col].playable:
                                self.currentBoard = self.boards[row][col]
                            else:
                                self.currentBoard = None
                            break
                '''
                #Select a square in given board at random
                while True:
                    row = random.randint(0, 2)
                    col = random.randint(0,2)
                    if self.checkSquare(self.currentBoard, row, col):
                        self.currentBoard.getSquare(row, col).state = self.getLetter()
                        self.currentBoard.checkWin()
                        self.changePlayer()
                        if self.boards[row][col].playable:
                            self.currentBoard = self.boards[row][col]
                        else:
                            self.currentBoard = None
                        break
    def checkForWins(self, screen):
        #check every win condition and respond accordingly
        #Top row
        if (self.boards[0][0].won == self.boards[0][1].won and self.boards[0][0].won == self.boards[0][2].won and not self.boards[0][0].won == ""):
            self.won(self.boards[0][0].won, screen)
        #Middle Row
        elif (self.boards[1][0].won == self.boards[1][1].won and self.boards[1][0].won == self.boards[1][2].won and not self.boards[1][0].won == ""):
            self.won(self.boards[1][0].won, screen)
        #Bottom Row
        elif (self.boards[2][0].won == self.boards[2][1].won and self.boards[2][0].won == self.boards[2][2].won and not self.boards[2][0].won == ""):
            self.won(self.boards[2][0].won, screen)
        #Middle Column
        elif (self.boards[0][1].won == self.boards[1][1].won and self.boards[0][1].won == self.boards[2][1].won and not self.boards[0][1].won == ""):
            self.won(self.boards[0][1].won, screen)
        #Last Column
        elif (self.boards[0][2].won == self.boards[1][2].won and self.boards[0][2].won == self.boards[2][2].won and not self.boards[0][2].won == ""):
            self.won(self.boards[0][2].won, screen)
        #First Column
        elif (self.boards[0][0].won == self.boards[1][0].won and self.boards[0][0].won == self.boards[2][0].won and not self.boards[0][0].won == ""):
            self.won(self.boards[0][0].won, screen)
        #Top left to bottom right
        elif (self.boards[0][0].won == self.boards[1][1].won and self.boards[0][0].won == self.boards[2][2].won and not self.boards[0][0].won == ""):
            self.won(self.boards[0][0].won, screen)
        #Bottom left to top right
        elif (self.boards[0][2].won == self.boards[1][1].won and self.boards[0][2].won == self.boards[2][0].won and not self.boards[0][2].won == ""):
            self.won(self.boards[0][2].won, screen)
        else:
            pass
    def won(self, letter, screen): #If game is over display this graphic
        W = screen.get_width()
        screen.fill((255,255,255))
        font=pygame.font.SysFont(None, 52)
        textSurf1 = font.render(str(letter)+" has won!", True, (0,255,0))
        textSurf2 = font.render("Click to quit!", True, (0,255,0))
        screen.blit(textSurf1,((W-textSurf1.get_width())//2,260))
        screen.blit(textSurf2,((W-textSurf2.get_width())//2,360))
        pygame.display.update()
        wait(4000)
        while True:
            for event in pygame.event.get():
                #Check for click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sys.exit()
                    pygame.quit()
    def changePlayer(self):
        #Changes the current player and keeps between 0-1
        self.currentPlayer+=1
        self.currentPlayer%=2
    def occupied(self, screen):
        #Graphic displayed if selected square is already taken/not playable
        font=pygame.font.SysFont(None, 20)
        textSurf1 = font.render("That spot is already occupied select again!", True, (255,255,0))
        screen.blit(textSurf1, (0,0))
    def topGraphic(self, screen, number):
        #Fill top color with current board
        '''
        if not self.currentBoard == None:
            num = -1
            for i in range(len(self.boards)):
                for j in range(len(self.boards[i])):
                    if (self.currentBoard == self.boards[i][j]):
                        num = i*3+j
                        break
            img = self.currentBoard.images[self.getLetter()+str(num)]
            screen.blit(pygame.transform.scale(img, (540, 80)), (0,0))
        elif self.currentBoard ==  None:
            img = self.anyImg
            screen.blit(pygame.transform.scale(img, (540, 80)), (0,0))
        '''
        #Show the color of specific board playable over player letter at top of screen
        if not self.currentBoard == None:
            num = -1
            for i in range(len(self.boards)):
                for j in range(len(self.boards[i])):
                    if (self.currentBoard == self.boards[i][j]):
                        num = i*3+j
                        break
            img = self.currentBoard.images["none"+str(num)]
            screen.blit(pygame.transform.scale(img, (40,40)), (315,17))
        #If any board is currently available displays each color in a changing fashion
        elif self.currentBoard == None:
            img = self.boards[0][0].images["none"+str(int(number))]
            screen.blit(pygame.transform.scale(img, (40,40)), (315,17))
        #Write out who is currently playing
        topButton = pygame.Rect(0,0,540, 80)
        font=pygame.font.SysFont(None, 40)
        textSurf1 = font.render("Playing:  "+str(self.getLetter()), True, (0,0,0))
        screen.blit(textSurf1,(topButton.x+(topButton.width-textSurf1.get_width())//2,topButton.y+(topButton.height-textSurf1.get_height())//2))
        
    def update(self, screen):
        screen.fill((255,255,255)) #Makes the screen white
        self.check_input(screen) #Checks for input
        self.checkForWins(screen) #Checks for overall wins
        self.number+=.02 #Involved in changing of color square of current board graphic is currentBoard = None
        self.number%=8 #keeps within bounds of images available
        self.topGraphic(screen, self.number) #Display top graphic
        #Update each board
        for i in range(len(self.boards)):
            for j in range(len(self.boards[i])):
                self.boards[j][i].update(screen)
        pygame.display.flip() #Update screen
            