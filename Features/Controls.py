import pygame
import math
from pygame.locals import *
from Tank import Player

class InputManager:
    def __init__(self, player: Player) -> None:
        self.running = True
        self.player = player
        self.bullets = bullets
        self.x = 400
        self.y = 300
        self.direction = None


def rotation(self):
    pos = pygame.mouse.get_pos()

    x_dist = pos[0] - self.rect.centerx
    y_dist = -(pos[1]-self.rect.centery)
    angle = math.degrees(math.atan2(y_dist, x_dist))

    turret = pygame.transform.rotate(self.player, angle - 90)
    turret_rect = turret.get_rect(center = (self.rect.centerx, self.rect.centerx))

    self.screen.blit(turret, turret_rect)

def input(self, keys):
    if keys[pygame.K_UP]:
        self.player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        self.player.rect.y += 5
    if keys[pygame.K_LEFT]:
        self.player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        self.player.rect.x += 5
    if keys[pygame.K_SPACE]:
        if not self.space_pressed:
            self.shoot()
            self.space_pressed = True
    else:
        self.space_pressed = False
    if keys[QUIT]:
        self.running = False
                    


    # def move_up(self):
    #     self.direction = "up"
    #     self.y -= 5  
    #     self.update_player_position()
        
    # def move_down(self):
    #     self.direction = "down"
    #     self.y += 5
    #     self.update_player_position()

    # def move_left(self):
    #     self.direction = "left"
    #     self.x -= 5
    #     self.update_player_position()

    # def move_right(self):
    #     self.direction = "right"
    #     self.x += 5
    #     self.update_player_position()