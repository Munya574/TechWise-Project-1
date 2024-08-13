import pygame
from Bullets import Bullet

class InputManager:
    def __init__(self, player, bullets):
        self.player = player
        self.bullets = bullets
        self.bullet_image_path = 'images/yellow_bullet.png'
        self.space_pressed = False

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.player.set_direction('left')
            self.player.move()
        elif keys[pygame.K_RIGHT]:
            self.player.set_direction('right')
            self.player.move()
        elif keys[pygame.K_UP]:
            self.player.set_direction('up')
            self.player.move()
        elif keys[pygame.K_DOWN]:
            self.player.set_direction('down')
            self.player.move()
        
        if keys[pygame.K_SPACE]:
            if not self.space_pressed:
                self.shoot()
                self.space_pressed = True
        else:
            self.space_pressed = False

    def shoot(self):
        player_x, player_y = self.player.get_position()
        direction = self.player.direction
        bullet = Bullet(player_x, player_y, 5, direction, self.bullet_image_path)
        self.bullets.append(bullet)