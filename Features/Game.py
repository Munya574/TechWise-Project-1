import pygame
from Tank import Player
from Bullets import Bullet
from Controls import InputManager
from Enemy import Enemy
from Graphics import Block, objects  # Import Block and objects list

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tanks")
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.player_bullets = []
        self.enemy = Enemy()
        self.enemy_bullets = self.enemy.bullets
        self.input_manager = InputManager(self.player, self.player_bullets)
        self.font = pygame.font.Font(None, 74)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.input_manager.handle_input(keys)
            
            if self.enemy:
                self.enemy.update(self.player)

            self.check_collisions()

            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            if self.enemy:
                self.enemy.draw(self.screen)

            # Draw the Block objects
            for block in objects:
                block.draw()

            self.update_bullets(self.player_bullets, self.enemy)
            self.update_bullets(self.enemy_bullets, self.player)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        raise SystemExit

    def update_bullets(self, bullets, target):
        for bullet in bullets[:]:
            bullet.update()
            if bullet.off_screen(self.width, self.height):
                bullets.remove(bullet)
            else:
                # Check for collision with blocks
                for block in objects:
                    if bullet.rect.colliderect(block.rect):
                        bullets.remove(bullet)
                        break  # No need to check other blocks once bullet is removed

                # Check for collision with the enemy
                if isinstance(target, Enemy) and bullet.collides_with(target):
                    bullets.remove(bullet)
                    self.handle_enemy_explosion(target)

        for bullet in bullets:
            bullet.draw(self.screen)
    
    def check_collisions(self):
        # Handle player collision with blocks
        for block in objects:
            if self.player.rect.colliderect(block.rect):
                self.handle_player_block_collision(block)

        # Handle enemy collision with blocks
        if self.enemy:
            for block in objects:
                if self.enemy.rect.colliderect(block.rect):
                    self.handle_enemy_block_collision(block)

        # Handle player collision with enemy
        if self.enemy and self.player.rect.colliderect(self.enemy.rect):
            self.handle_player_enemy_collision()

    def handle_player_block_collision(self, block):
        # Adjust player's position based on the collision with a block
        if self.player.direction == 'up':
            self.player.rect.top = block.rect.bottom
        elif self.player.direction == 'down':
            self.player.rect.bottom = block.rect.top
        elif self.player.direction == 'left':
            self.player.rect.left = block.rect.right
        elif self.player.direction == 'right':
            self.player.rect.right = block.rect.left

    def handle_enemy_block_collision(self, block):
        # Adjust enemy's position based on the collision with a block
        if self.enemy.angle == 0:  # Moving down
            self.enemy.rect.bottom = block.rect.top
        elif self.enemy.angle == 90:  # Moving left
            self.enemy.rect.left = block.rect.right
        elif self.enemy.angle == 180:  # Moving up
            self.enemy.rect.top = block.rect.bottom
        elif self.enemy.angle == 270:  # Moving right
            self.enemy.rect.right = block.rect.left


    def handle_player_enemy_collision(self):
        #self.display_game_over()
        pass
        
    def handle_enemy_explosion(self, enemy):
    # Load and scale the explosion image
        explosion_image = pygame.image.load('images/explode.png')  # Ensure this path is correct
        explosion_image = pygame.transform.scale(explosion_image, (enemy.rect.width, enemy.rect.height))

    # Draw the explosion effect (ensure the image is centered in the enemy's rectangle)
        explosion_rect = explosion_image.get_rect(center=enemy.rect.center)
        self.screen.blit(explosion_image, explosion_rect)

        pygame.display.flip()  # Update the display to show the explosion

    # Pause for a moment to display the explosion
        pygame.time.delay(300)  # Adjust the delay as needed

    # Remove the enemy from the screen
        self.enemy = None
    # def display_game_over(self):
    #     game_over_text = self.font.render('Game Over', True, (255, 255, 255))
    #     self.screen.blit(game_over_text, (260, 250))

    #     pygame.display.flip()
    #     pygame.time.wait(2000)
    #     pygame.quit()
    #     raise SystemExit

if __name__ == '__main__':
    game = Game()
    game.run()