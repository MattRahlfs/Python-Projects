import pygame
import random

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green  = (0,155,0)
display_width = 800
display_height = 600
font = pygame.font.SysFont(None, 25)
gD = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")



clock = pygame.time.Clock()

def msg_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gD.blit(screen_text, [display_width/2, display_height/2])
    
def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gD, green, [XnY[0], XnY[1], block_size, block_size])
    
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    block_size = 15
    speed = 3
    appleCount = 0
    apple_Size = 10
    lead_x_change = 0
    lead_y_change = 0
    randApple_x = random.randrange (0, display_width-block_size, 10)
    randApple_y = random.randrange(0, display_height-block_size, 10)
    snakeList = []
    snakeLen = 1

    

    while not gameExit:
        while gameOver == True:
            gD.fill(white)
            msg_to_screen("Game over. Press c  to play again or q to quit.", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -speed
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = +speed
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -speed
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = +speed
                    lead_x_change = 0
                elif event.key == pygame.K_ESCAPE:
                    gameExit = True
                    
        if lead_x >= display_width-block_size or lead_x < 0 or lead_y >= display_height-block_size or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gD.fill(white)
        pygame.draw.rect(gD, red, [randApple_x, randApple_y, apple_Size, apple_Size])

       
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLen:
            del snakeList[0]

        for eachSe in snakeList[:-1]:
            if eachSe == snakeHead:
                gameOver = True
                
        snake(block_size, snakeList)
        
        
##        if lead_x >= randApple_x and lead_x <= randApple_x + apple_Size:
##            if lead_y >= randApple_y and lead_y <= randApple_y + apple_Size:
##                randApple_x = random.randrange (0, display_width-block_size, 10)
##                randApple_y = random.randrange(0, display_height-block_size, 10)
##                snakeLen = snakeLen + block_size
##                appleCount = appleCount + 1
##                speed = speed +.1

        if (lead_x > randApple_x and lead_x < randApple_x + apple_Size or lead_x + block_size > randApple_x and lead_x + block_size < randApple_x + apple_Size):
            if lead_y > randApple_y and lead_y < randApple_y + apple_Size or lead_y + block_size > randApple_y and lead_y + block_size < randApple_y + apple_Size:
                randApple_x = random.randrange (0, display_width-block_size, 10)
                randApple_y = random.randrange(0, display_height-block_size, 10)
                snakeLen = snakeLen + block_size
                appleCount = appleCount + 1
                speed = speed +.05
    
            
        pygame.display.update()
            
        clock.tick(60)

    msg_to_screen("you lose", red)
    pygame.display.update()
    
    pygame.quit()
    quit()

gameLoop()
