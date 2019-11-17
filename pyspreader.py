import re, pygame

pygame.init()
black = (0,0,0)
gray = (205, 201, 201)
WPM = 0
font = pygame.font.SysFont("arial", 30)

mainLoop = True


def paused():
    pD = pygame.display.set_mode((600, 400))
    pD.fill(black, (0,0, 600,400))
    label = font.render("Paused, Press P again ro resume or C to change WPM", 1, (gray))
    pD.blit(label, ((600/2 - label.get_rect().width/2), 400/2 - label.get_rect().height/2))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pass
        elif event.key == pygame.K_c:
            userInput = input ("Enter the WPM\n\n")
            WPM = int(userInput) / 60
    
    
def drawtoScreen(each, WPM):
    pD = pygame.display.set_mode((600, 400))
    pD.fill(black, (0,0, 600,400))
    pygame.display.update()

    
    pD.fill(black, (0,0, 600,400))
    label = font.render(each, 1, (gray))
    pD.blit(label, ((600/2 - label.get_rect().width/2), 400/2 - label.get_rect().height/2))
    pygame.display.update()
    pygame.time.Clock().tick(WPM)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ("QUIT")
            mainLoop = False
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print ("ESCAPE")
                mainLoop = False
                pygame.quit()
                quit()
            elif event.key == pygame.K_p:
                print ("PAUSING")
                paused()
                    
    
    
while mainLoop:
    
    
    userInput = input ("Enter the WPM\n\n")
    WPM = int(userInput) / 60
    #WPM = 1 / WPM
    userInput = input ("Enter the String you wish to read\n\n")

    sepInput = re.sub("[^\w]", " ",  userInput).split()

                    
    for each in sepInput:
        drawtoScreen(each, WPM)

    mainLoop = False

    
pygame.quit()
quit()






