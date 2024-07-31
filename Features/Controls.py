import pygame
from pygame.locals import *
from Tank import Player

class InputManager:
    def __init__(self, player: Player) -> None:
        self.running = True
        self.player = player
        self.x = 400
        self.y = 300
        self.direction = None

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.move_up()
                    if event.key == K_DOWN:
                        self.move_down()
                    if event.key == K_LEFT:
                        self.move_left()
                    if event.key == K_RIGHT:
                        self.move_right()
                if event.type == QUIT:
                    self.running = False
                    

    def move_up(self):
        self.direction = "up"
        self.y -= 5  
        self.update_player_position()
        
    def move_down(self):
        self.direction = "down"
        self.y += 5
        self.update_player_position()

    def move_left(self):
        self.direction = "left"
        self.x -= 5
        self.update_player_position()

    def move_right(self):
        self.direction = "right"
        self.x += 5
        self.update_player_position()