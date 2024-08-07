import pygame
import random

class Enemy:
    def __init__(self):
       self.image = pygame.image.load('enemy.png') 
       self.rect = self.image.get_rect()
       self.rect.bottomright = (400,300)
       self.move_count = 0
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        choice = random.randint(0,2)
        if self.move_count > 0:
            self.move_count = self.move_count - 1
            if self.angle == 0:
                self.x += 3
            if self.angle == 90:
                self.y -= 3
            if self.angle == 180:
                self.x -= 3
            if self.angle == 270:
                self.y += 3
        if choice == 0:
            self.move_count = 20
        if choice == 1:
            self.angle = random.randint(0,3) * 90
        else:
            #need to add shooting
            pass 

    