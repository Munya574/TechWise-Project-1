import pygame

class Player:
    def __init__(self):
       self.image = pygame.image.load('pic.png') 
       self.rect = self.image.get_rect()
       self.rect.topleft = (400,300)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)