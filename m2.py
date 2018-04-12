import random, pygame, sys
from pygame.locals import *
pygame.init()
grey= (100,100,100)
navyblue= (60,60,100)
white= (255,255,255)
red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)
yellow= (255, 255,0)
orange= (255, 128,0)
purple= (255,0, 255)
cyan= (0, 255, 255)
black=(0,0,0)
background = yellow
background2 = grey
boxcolor = black

fps = 30 
width = 600 
height = 800 
boxsize = 40 
gap = 10 


DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
OVAL = 'oval'

colors = (red, green, blue, navyblue, orange, purple, cyan)
shapes = (DONUT, SQUARE, DIAMOND, OVAL)
font = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/Stiff Staff.otf", 25)
font1 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/Stiff Staff.otf", 60)
font2 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/Stiff Staff.otf", 40)
title = pygame.image.load("body-bg_ovz9eo.png")
def start_up():
    global clock, game
    game = pygame.display.set_mode((width, height))
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Memory Game')
    intro = True
    while intro:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			pygame.quit()
    			quit()
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_1:
                                           intro = False
                                           main(4)
    			if event.key == pygame.K_2:
    				 intro = False
    				 main(6)
    			if event.key == pygame.K_q:
    				pygame.quit()
    				quit()
    	game.fill(white)
    	game.blit(title,[0,0])
    	t1=font1.render("Memory Game",True,black)
    	game.blit(t1,[75,60])
    	t2=font2.render("Press 1 for level 1.",True,black)
    	game.blit(t2,[150,160])
    	t3=font2.render("Press 2 for level 2.",True,black)
    	game.blit(t3,[150,200])
    	t4=font2.render("Press Q to quit.",True,black)
    	game.blit(t4,[150,240])
    	pygame.display.update()
    	clock.tick(20)

def main(no):
    global bwidth,bheight,sidemargin ,topmargin
    bheight=no
    bwidth=no
    
    sidemargin = int((width - (bwidth * (boxsize + gap))) / 2)
    topmargin = int((height - (bheight * (boxsize + gap))) / 2)
    mainboard = randomboard()
    openedbox = openedboxstatus(False)

    selection1 = None 

    game.fill(background)
    startgame(mainboard)
    mousex = 0
    mousey = 0

    while True:
        mouseclicked = False

        game.fill(background) 
        drawboard(mainboard, openedbox)

        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseclicked = True

        boxx, boxy = getbox(mousex, mousey)
        if boxx != None and boxy != None:
            if not openedbox[boxx][boxy] and mouseclicked:
                openbox(mainboard, [(boxx, boxy)])
                openedbox[boxx][boxy] = True 
                if selection1 == None: 
                    selection1 = (boxx, boxy)
                else: 
                    icon1shape, icon1color = shapeandcolor(mainboard, selection1[0], selection1[1])
                    icon2shape, icon2color = shapeandcolor(mainboard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        pygame.time.wait(1000) 
                        closebox(mainboard, [(selection1[0], selection1[1]), (boxx, boxy)])
                        openedbox[selection1[0]][selection1[1]] = False
                        openedbox[boxx][boxy] = False
                    elif won(openedbox): 
                        gamewon(mainboard)
                        pygame.time.wait(2000)
                        selection1 = None
                        start_up()
                        mainboard = randomboard()
                        openedbox = openedboxstatus(False)
                        drawboard(mainboard, openedbox)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        startgame(mainboard)
                    selection1 = None
        pygame.display.update()
        clock.tick(fps)


def openedboxstatus(val):
    openedbox = []
    for i in range(bwidth):
        openedbox.append([val] * bheight)
    return openedbox


def randomboard():
    icons = []
    for color in colors:
        for shape in shapes:
            icons.append( (shape, color) )

    random.shuffle(icons)
    numIconsUsed = int(bwidth * bheight / 2) 
    icons = icons[:numIconsUsed] * 2 
    random.shuffle(icons)
    board = []
    for x in range(bwidth):
        column = []
        for y in range(bheight):
            column.append(icons[0])
            del icons[0] 
        board.append(column)
    return board

def coordinates(boxx, boxy):
    left = boxx * (boxsize + gap) + sidemargin
    top = boxy * (boxsize + gap) + topmargin
    return (left, top)


def getbox(x, y):
    for boxx in range(bwidth):
        for boxy in range(bheight):
            left, top = coordinates(boxx, boxy)
            boxRect = pygame.Rect(left, top, boxsize, boxsize)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def drawIcon(shape, color, boxx, boxy):
    quarter = int(boxsize * 0.25)
    half =    int(boxsize * 0.5)

    left, top = coordinates(boxx, boxy)
    if shape == DONUT:
        pygame.draw.circle(game, color, (left + half, top + half), half - 5)
        pygame.draw.circle(game, background, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(game, color, (left + quarter, top + quarter, boxsize - half, boxsize - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(game, color, ((left + half, top), (left + boxsize - 1, top + half), (left + half, top + boxsize - 1), (left, top + half)))
    elif shape == OVAL:
        pygame.draw.ellipse(game, color, (left, top + quarter, boxsize, half))


def shapeandcolor(board, boxx, boxy):
    return board[boxx][boxy][0], board[boxx][boxy][1]


def openbox(board, boxesToReveal):
    for box in boxesToReveal :
        left, top = coordinates(box[0], box[1])
        pygame.draw.rect(game, background, (left, top, boxsize, boxsize))
        shape, color = shapeandcolor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])

    pygame.display.update()
    clock.tick(fps)


def closebox(board, boxesToCover):
    for box in boxesToCover:
        left, top = coordinates(box[0], box[1])
        pygame.draw.rect(game, background, (left, top, boxsize, boxsize))
    pygame.display.update()
    clock.tick(fps)
        


def drawboard(board, revealed):
    for boxx in range(bwidth):
        for boxy in range(bheight):
            left, top = coordinates(boxx, boxy)
            if not revealed[boxx][boxy]:
                pygame.draw.rect(game, boxcolor, (left, top, boxsize, boxsize))
            else:
                shape, color = shapeandcolor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def startgame(board):
    coveredBoxes = openedboxstatus(False)
    boxes = []
    for x in range(bwidth):
        for y in range(bheight):
            boxes.append( (x, y) )
    random.shuffle(boxes)
  
    drawboard(board, coveredBoxes)
    pygame.time.wait(1000)
    openbox(board, boxes)
    pygame.time.wait(1000)
    closebox(board, boxes)


def gamewon(board):
    coveredBoxes = openedboxstatus(True)
    color1 = background2
    color2 = background

    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        game.fill(color1)
        drawboard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)


def won(openedbox):
    for i in openedbox:
        if False in i:
            return False 
    return True

start_up()
