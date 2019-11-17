import pygame, random

pygame.init()

mainLoop = False
gameDisplay = pygame.display.set_mode((800,600))
white = (255,255,255)
skyColor =(112, 203, 255)
black = (0,0,0)
tan = (212,189,134)
cloud1_X = random.randrange(800,900)
cloud2_X = random.randrange(800,900)
cloud3_X = random.randrange(800,900)
cloud1Speed = random.randrange(1,4)
cloud2Speed = random.randrange(1,4)
cloud3Speed = random.randrange(1,4)




def background():
    global cloud1_X, cloud2_X, cloud3_X, cloud1Speed, cloud2Speed, cloud3Speed
    gameDisplay.fill(skyColor, (0,0, 800, 360))
    cloud1_X = cloud1_X -cloud1Speed
    cloud2_X = cloud2_X -cloud2Speed
    cloud3_X = cloud3_X -cloud3Speed
    BG = pygame.image.load('Images/sky.png')
    cloud1 = pygame.image.load('Images/cloud1.png')
    cloud2 = pygame.image.load('Images/cloud2.png')
    cloud3 = pygame.image.load('Images/cloud3.png')
    gameDisplay.blit(cloud1, (cloud1_X,10))
    gameDisplay.blit(cloud2, (cloud2_X,100))
    gameDisplay.blit(cloud3, (cloud3_X,200))

    if cloud1_X < -355:
        cloud1_X = 800
        cloud1Speed = random.randrange(1,4)
    elif cloud2_X < -355:
        cloud2_X = 800
        cloud2Speed = random.randrange(1,4)
    elif cloud3_X < -355:
        cloud3Speed = random.randrange(1,4)
        cloud3_X = 800

    pygame.draw.rect(gameDisplay, tan,(0,360,800,450))
    
    Menu = pygame.image.load('Images/Tan_Options.png')
    gameDisplay.blit(Menu, (-1,360))
##    Edge = pygame.transform.rotate(Edge,90)
##    gameDisplay.blit(Edge, (-1,360))
##    Edge = pygame.transform.rotate(Edge,90)
##    gameDisplay.blit(Edge, (-1,550))
##    Edge = pygame.transform.rotate(Edge,90)
##    gameDisplay.blit(Edge, (750,360))


def openButtons():
   playGame = pygame.image.load('Images/Button_PLAY1.png')
   gameDisplay.blit(playGame, (40, 400))

def startGame():
    mainLoop = True
    char_X = 100
    char_Y = 100
    

    while mainLoop:
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_w]:
            char_Y = char_Y -0.5
        elif keyPressed[pygame.K_s]:
            char_Y = char_Y +0.5
        elif keyPressed[pygame.K_a]:
            char_X = char_X -0.5
        elif keyPressed[pygame.K_d]:
            char_X = char_X +0.5
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("QUIT")
                mainLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print ("ESCAPE")
                    mainLoop = False
            
            

                
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, (char_X,char_Y, 10,10))
        pygame.display.update()
    

        


playGame = pygame.image.load('Images/Button_PLAY1.png')
while not mainLoop:
    gameDisplay.fill(skyColor, (0,0, 800, 321))
    mousePos = pygame.mouse.get_pos()
    background()
    playGame = pygame.image.load('Images/Button_PLAY1.png')
    gameDisplay.blit(playGame, (40, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ("QUIT")
            mainLoop = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print ("ESCAPE")
                mainLoop = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mousePos[0] >= 55 and mousePos[1] >=400 and mousePos[0] <= 215 and mousePos[1]<= 475:
                playGame = pygame.image.load('Images/Button_PLAY2.png')
                gameDisplay.blit(playGame, (40, 400))
                startGame()
                mainLoop = True
            
                




    
    pygame.display.update()



pygame.quit()
quit()
    
