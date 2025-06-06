import pygame
import math

objects = []
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
        oldX, oldY = self.rect.center #save it's old position, if tank collides with obstacles it will return to old space
        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed
            
        for obj in objects: #collision check of player with obstacles
            if obj != self and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        self.check_boundaries()

    def check_boundaries(self):
        if self.rect.left < 0:
            self.rect.left = 0
            
        elif self.rect.right > 800:
            self.rect.right = 800
            self.move_count = 0
        if self.rect.top < 0:
            self.rect.top = 0
            
        elif self.rect.bottom > 600:
            self.rect.bottom = 600
            