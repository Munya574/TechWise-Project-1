import pygame
pygame.init()
prozor = pygame.display.set_mode((200, 200))
prozor.fill(pygame.Color("white"))
pygame.draw.rect(prozor, pygame.Color("black"), (20, 20, 160, 160), 5)
pygame.display.update()
pygame.time.wait(1200)
pygame.quit()