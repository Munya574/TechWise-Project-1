import pygame
import random
from Bullets import Bullet
from Tank import Player
import math
import aStar

class Enemy:
    def __init__(self):
        self.original_image = pygame.image.load('images/enemy.png') 
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

        self.bullets = []
        self.shoot_delay = 800
        self.last_shot_time = pygame.time.get_ticks()
        self.shoot_range = 200 # Distance to player

        self.grid = [[0 for _ in range(20)] for _ in range(15)]  # Example grid, 0 = walkable, 1 = obstacle
        self.path = []

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)

    def update(self, player):
        self.clock.tick(80)

        if self.move_count > 0:
            self.move_count -= 1
            self.move_in_current_direction()
        else:
            self.choose_new_direction()

        self.shoot(player)

        # Update bullets
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.off_screen(800, 600):
                self.bullets.remove(bullet)

        # Boundary checks
        self.check_boundaries()

        if not self.path:
            start_node = aStar.Node(self.rect.x // 50, self.rect.y // 50)  # Assuming each grid cell is 50x50 pixels
            end_node = aStar.Node(player.rect.x // 50, player.rect.y // 50)
            self.path = aStar.a_star(start_node, end_node, self.grid)

        if self.path:
            next_move = self.path.pop(0)
            self.rect.x = next_move[0] * 50
            self.rect.y = next_move[1] * 50

    def move_in_current_direction(self):
        if self.angle == 0:
            self.rect.y += 1
        elif self.angle == 90:
            self.rect.x -= 1
        elif self.angle == 180:
            self.rect.y -= 1
        elif self.angle == 270:
            self.rect.x += 1

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

    def check_boundaries(self):
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

    def collidelist(self):
        return -1  

    def shoot(self, player):
        # Check the distance between the player and the enemy
        player_distance = self.get_distance_to_player(player)
        
        if player_distance <= self.shoot_range:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_shot_time > self.shoot_delay:
                bullet_direction = self.get_bullet_direction()
                bullet = Bullet(self.rect.centerx, self.rect.centery, 3, bullet_direction, 'images/yellow_bullet.png')
                self.bullets.append(bullet)
                self.last_shot_time = current_time

    def get_bullet_direction(self):
        if self.angle == 0:
            return 'down'
        elif self.angle == 90:
            return 'left'
        elif self.angle == 180:
            return 'up'
        elif self.angle == 270:
            return 'right'
        
    def get_distance_to_player(self, player):
        # Calculate the distance to the player
        enemy_center = self.rect.center
        player_center = player.rect.center
        distance = math.sqrt((enemy_center[0] - player_center[0]) ** 2 + 
                             (enemy_center[1] - player_center[1]) ** 2)
        return distance