import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("abubakrs game")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('spaceship.png')
playerX = 370 
playerY = 480
playerX_change = 0



def player(x,y):
    screen.blit(playerImg,(x,y))



running = True
while running:

    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #key stroke
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_LEFT:
            playerX_change = -0.1
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.1    
    if event.type == pygame.KEYUP:
        if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0.1
                  

    playerX += playerX_change
    player(playerX,playerY)
    pygame.display.update()        
    


