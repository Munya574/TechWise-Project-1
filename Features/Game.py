import pygame
from Tank import Player
pygame.init()

width , height = 800 , 600
screen = pygame.display.set_mode((width , height))
pygame.display.set_caption("Tanks")

player = Player()

run = True
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    player.draw(screen)
    pygame.display.flip()
pygame.quit()