import pygame
import random

class Enemy:
    def __init__(self):
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.bottomright = (400, 300)
        self.move_count = 0
        self.angle = 0
        self.clock = pygame.time.Clock()  

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.clock.tick(60)  
        print(self.angle)
        if self.move_count > 0:
            self.move_count -= 1
            if self.angle == 0:
                self.rect.x += 3
            elif self.angle == 90:
                self.rect.y -= 3
            elif self.angle == 180:
                self.rect.x -= 3
            elif self.angle == 270:
                self.rect.y += 3
        else:
            self.choose_new_direction()

    def choose_new_direction(self):
        self.move_count = 20  
        self.angle = random.randint(0, 3) * 90