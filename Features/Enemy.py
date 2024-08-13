import pygame
import random

class Enemy:
    def __init__(self):
        self.original_image = pygame.image.load('enemy.png') 
        self.size = (70, 50) 
        self.original_image = pygame.transform.scale(self.original_image, self.size)
        
        self.image = self.original_image  
        self.rect = self.image.get_rect()

        # Start the enemy at a random position along the top of the screen
        self.rect.x = random.randint(0, 800 - self.rect.width) 
        self.rect.y = 0 

        self.move_count = 0
        self.angle = 0
        self.clock = pygame.time.Clock()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.clock.tick(80)

        if self.move_count > 0:
            self.move_count -= 1
            if self.angle == 0:
                self.rect.y += 2
            elif self.angle == 90:
                self.rect.x -= 2
            elif self.angle == 180:
                self.rect.y -= 2
            elif self.angle == 270:
                self.rect.x += 2
        else:
            self.choose_new_direction()

        # Boundary checks
        if self.rect.left < 0:
            self.rect.left = 0
            self.move_count = 0
        elif self.rect.right > 800:
            self.rect.right = 800
            self.move_count = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.move_count = 0
        elif self.rect.bottom > 600:
            self.rect.bottom = 600
            self.move_count = 0

        if self.collidelist() != -1:
            self.move_count = 0

    def choose_new_direction(self):
        self.move_count = random.randint(20, 60) 
        new_angle = random.choice([0, 90, 180, 270]) 
        self.rotate_image(new_angle)
        self.angle = new_angle

    def rotate_image(self, new_angle):
        if new_angle == 0:
            self.image = self.original_image
        elif new_angle == 270:
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif new_angle == 180:
            self.image = pygame.transform.rotate(self.original_image, 180)
        elif new_angle == 90:
            self.image = pygame.transform.rotate(self.original_image, -90)

        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)

    def collidelist(self):
        return -1  