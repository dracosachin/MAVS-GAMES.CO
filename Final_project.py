import pygame,time,random,sys
from pygame.locals import *
def gamestart():
        pygame.init()
        pygame.font.init()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        green = (105,105,105)
        border = (255,153,18)
        d_green = (0,102,0)
        d_yellow = (204,153,0)
        yellow= (255, 255,0)
        height = 800
        width = 600
        block = 10
        obs_x = []
        obs_y = []
        high2 = [0,0,0]
        high1 = [0,0,0]
        game=pygame.display.set_mode((height,width))
        pygame.display.set_caption("Slither")
        direction = "right"
        background = pygame.image.load("green.jpg")
        title = pygame.image.load("mavs.jpg")
        font = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/snake/1.ttf", 25)
        font1 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/snake/1.ttf", 60)
        font2 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/snake/1.ttf", 40)
        font3 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/snake/KBZipaDeeDooDah.ttf", 20)
        def start_up():
                intro = True
                while intro:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_1:
                                                 snake()
                                        if event.key == pygame.K_2:
                                                 memory()
                                        if event.key == pygame.K_q:
                                                pygame.quit()
                                                quit()
                        game.fill(white)
                        game.blit(title,[0,0])
                        t1=font1.render("M",True,white)
                        game.blit(t1,[150,60])
                        t5=font1.render("A",True,white)
                        game.blit(t5,[150,160])
                        t6=font1.render("V",True,white)
                        game.blit(t6,[150,260])
                        t7=font1.render("S",True,white)
                        game.blit(t7,[150,360])
                        t8=font1.render("G A M E S",True,yellow)
                        game.blit(t8,[25,460])
                        t2=font2.render("Press 1 for Snake game.",True,black)
                        game.blit(t2,[325,75])
                        t3=font2.render("Press 2 for Memory game.",True,black)
                        game.blit(t3,[325,120])
                        t4=font2.render("Press Q to quit.",True,black)
                        game.blit(t4,[325,160])
                        pygame.display.update()
                
        start_up()
def memory():
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
        width = 640 
        height = 480 
        boxsize = 40 
        gap = 10 


        DONUT = 'donut'
        SQUARE = 'square'
        DIAMOND = 'diamond'
        OVAL = 'oval'

        colors = (red, green, blue, navyblue, orange, purple, cyan)
        shapes = (DONUT, SQUARE, DIAMOND, OVAL)
        font = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/2.ttf", 25)
        font1 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/2.ttf", 40)
        font2 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/2.ttf", 25)
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
                                if event.key == pygame.K_m:
                                         gamestart()
                                if event.key == pygame.K_q:
                                        pygame.quit()
                                        quit()
                game.fill(white)
                game.blit(title,[0,0])
                t1=font1.render("Memory Game",True,black)
                game.blit(t1,[145,60])
                t2=font2.render("Press 1 for level 1.",True,black)
                game.blit(t2,[150,160])
                t3=font2.render("Press M for Main Menu.",True,black)
                game.blit(t3,[150,240])
                t3=font2.render("Press 2 for level 2.",True,black)
                game.blit(t3,[150,200])
                t4=font2.render("Press Q to quit.",True,black)
                game.blit(t4,[150,280])
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

def snake():
        pygame.init()
        pygame.font.init()
        white = (255,255,255)
        black = (0,0,0)
        red = (255,0,0)
        green = (105,105,105)
        border = (255,153,18)
        d_green = (0,102,0)
        d_yellow = (204,153,0)
        height = 800
        width = 600
        block = 10
        obs_x = []
        obs_y = []
        high2 = [0,0,0]
        high1 = [0,0,0]
        game=pygame.display.set_mode((height,width))
        pygame.display.set_caption("Slither")
        direction = "right"
        background = pygame.image.load("green.jpg")
        title = pygame.image.load("sasa.jpg")
        font = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/snake/2.ttf", 25)
        font1 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/snake/2.ttf", 40)
        font2 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/snake/2.ttf", 25)
        font3 = pygame.font.Font("C:/Users/Sachin/Desktop/openlab/snake/2.ttf", 15)
        def start_up():
                obs_x = []
                obs_y = []
                intro = True
                while intro:
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_1:
                                                 ran = 10
                                                 intro = False
                                                 obstacles(ran)
                                                 game_loop(ran)
                                        if event.key == pygame.K_2:
                                                 ran2 = 20
                                                 intro = False
                                                 obstacles(ran2)
                                                 game_loop(ran2)
                                        if event.key == pygame.K_m:
                                                 gamestart()
                                        if event.key == pygame.K_q:
                                                pygame.quit()
                                                quit()
                        game.fill(white)
                        game.blit(title,[0,0])
                        t1=font1.render("Welcome To Snake World",True,black)
                        game.blit(t1,[30,60])
                        t2=font2.render("Press 1 for level 1.",True,black)
                        game.blit(t2,[160,250])
                        t3=font2.render("Press 2 for level 2.",True,black)
                        game.blit(t3,[160,290])
                        t3=font2.render("Press M for Main Menu.",True,black)
                        game.blit(t3,[150,200])
                        t4=font2.render("Press Q to quit.",True,black)
                        game.blit(t4,[160,330])
                        t5=font3.render("Note:",True,black)
                        game.blit(t5,[50,450])
                        t6=font3.render("1) When the snake is moving upwards/downward,",True,black)
                        game.blit(t6,[50,470])
                        t8=font3.render("   do not press downward/upward key.",True,black)
                        game.blit(t8,[50,490])
                        t7=font3.render("2) When the snake is moving left/right,",True,black)
                        game.blit(t7,[50,510])
                        t9=font3.render("   do not press right/left key.",True,black)
                        game.blit(t9,[50,530])
                        pygame.display.update()
        def score(score):
                text = font.render("Score : "+str(score),True,black)
                game.blit(text,[10,10])
        def obstacles(ran1):
                for i in range(ran1):
                        ob_x = round(random.randint(10,height-10)/10)*10
                        ob_y = round(random.randint(10,width-10)/10)*10
                        obs_x.append(ob_x)
                        obs_y.append(ob_y)
        def show(ran):
                if ran == 10 :
                        message_to_screen1("1:"+" "+str(high1[0]),black,350,300)
                        message_to_screen1("2:"+" "+str(high1[1]),black,350,325)
                        message_to_screen1("3:"+" "+str(high1[2]),black,350,350)
                elif ran == 20:
                        message_to_screen1("1:"+" "+str(high2[0]),black,350,300)
                        message_to_screen1("2:"+" "+str(high2[1]),black,350,325)
                        message_to_screen1("3:"+" "+str(high2[2]),black,350,350)
        def message_to_screen1(msg,color,a,b):
                s_text1 = font.render(msg,True,color)
                game.blit(s_text1, [a,b])
        def snake(block,lis):
                for i in lis:
                        pygame.draw.rect(game,white, [i[0],i[1],block,block])
        def message_to_screen(msg,color):
                s_text = font.render(msg,True,color)
                game.blit(s_text, [100,150])
        clock = pygame.time.Clock()
        def game_loop(ran):
                gameExit = False
                gameOver = False
                x=height/2
                y=width/2
                x_change=0
                y_change=0
                lis = []
                leng = 1
                app_x = round(random.randint(0,width-10)/10.0)*10.0
                app_y = round(random.randint(0,width-10)/10.0)*10.0
                while not gameExit:
                        while gameOver == True:
                                game.fill(white)
                                high1.sort(reverse = True)
                                high2.sort(reverse = True)
                                game.blit(background,[0,0])
                                message_to_screen("C to play again, Q to quit, M for Main Menu",black)
                                message_to_screen1("High Scores:",black,300,250)
                                show(ran)
                                pygame.display.update()
                                for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                                if event.key == pygame.K_m:
                                                        gameExit = False
                                                        gameOver = False
                                                        x=height/2
                                                        y=width/2
                                                        x_change=0
                                                        y_change=0
                                                        lis = []
                                                        leng = 1
                                                        start_up()
                                                if event.key == pygame.K_q:	
                                                        gameExit = True
                                                        gameOver = False
                                                if event.key == pygame.K_c:
                                                        game_loop(ran)
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        gameExit = True
                                if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_LEFT:
                                                x_change = -10
                                                y_change = 0
                                        elif event.key == pygame.K_RIGHT:
                                                x_change = 10
                                                y_change = 0
                                        elif event.key == pygame.K_UP:
                                                y_change = -10
                                                x_change = 0
                                        elif event.key == pygame.K_DOWN:
                                                y_change = 10
                                                x_change = 0
                        if x >= 790 or x<=10 or y>=590 or y<=10:
                                if x>790 :
                                        x=10
                                elif x<10 :
                                        x=790
                                elif y>590:
                                        y=10
                                elif y<10 :
                                        y=590		
                        x+=x_change
                        y+=y_change
                        game.fill(white)
                        game.blit(background,[0,0])
                        pygame.draw.rect(game, red, [app_x,app_y,10,10])
                        head = []
                        head.append(x)
                        head.append(y)
                        lis.append(head)
                        if len(lis) > leng:
                                del lis[0]
                        for i in lis[:-1]:
                                if i == head:
                                        gameOver = True
                                        if ran == 10:
                                                high1.append(leng-1)
                                        elif ran == 20:
                                                high2.append(leng-1)
                        snake(block, lis)
                        for i in range(ran):
                                pygame.draw.rect(game,d_green, [obs_x[i],obs_y[i],10,10])
                        score(leng-1)
                        for i in range(ran):
                                if x == obs_x[i] and y == obs_y[i]:
                                        gameOver = True
                                        if ran == 10:
                                                high1.append(leng-1)
                                        elif ran == 20:
                                                high2.append(leng-1)
                        pygame.display.update()	
                        if x == app_x and y == app_y:
                                app_x = round(random.randrange(10,height-10)/10.0)*10.0
                                app_y = round(random.randrange(10,width-10)/10.0)*10.0
                                leng += 1
                        clock.tick(25)
                pygame.quit()
                quit()
        start_up()

gamestart()
