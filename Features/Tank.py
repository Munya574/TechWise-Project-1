import pygame
import math

class Player:
    def __init__(self):
        self.image = pygame.image.load('images/pic.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 300)
        self.direction = 'up' 
        self.speed = 5

    def draw(self, screen):
        image = pygame.transform.rotate(self.image, self.get_rotation_angle())
        screen.blit(image, self.rect)

    def get_position(self):
        return self.rect.center

    def get_rotation_angle(self):
        angles = {
            'up': 0,
            'down': 180,
            'left': 90,
            'right': 270
        }
        return angles.get(self.direction, 0)

    def set_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed