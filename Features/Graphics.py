# Obstacles + graphics
import pygame
from random import randint


TILE = 32
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT)) 

imgBrick = pygame.image.load('images/bricks.png')


class Block:
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = "tank"
        
        self.rect = pygame.Rect (px, py, size, size)
        self.hp = 1
        
    def update (self):
        pass
    
    def draw (self):
        window.blit(imgBrick, self.rect)
       # pygame.draw.rect(window, "green", self.rect)
       # pygame.draw.rect(window, "gray20", self.rect, 2)
    
    def damage (self, value):
       self.hp -= value
       if self.hp <= 0: 
           objects.remove(self)
       
objects = []


for _ in range (50):
    while True:
        x = randint(0, WIDTH // TILE -1) *TILE
        y = randint(0, HEIGHT // TILE -1) *TILE
        rect = pygame.Rect(x, y, TILE, TILE) 
        fined = False
        for obj in objects:
            if rect.colliderect(obj.rect): 
                fined =True
            
        if not fined: 
            break
    Block(x, y, TILE) 
    
