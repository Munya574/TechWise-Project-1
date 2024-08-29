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
        self.enemies = [Enemy() for _ in range(5)]
        self.enemy_bullets = self.enemy.bullets
        self.input_manager = InputManager(self.player, self.player_bullets)
        self.font = pygame.font.Font(None, 74)
        self.reset_game()
        self.player_hits = 0
        
    def reset_game(self):
        # Reinitialize game state
        self.player = Player()
        self.player_bullets = []
        self.enemies = [Enemy() for _ in range(5)]
        self.enemy_bullets = []
        self.input_manager = InputManager(self.player, self.player_bullets)
        self.player_hits = 0
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.input_manager.handle_input(keys)
            
            for enemy in self.enemies:
                enemy.update(self.player)

            self.check_collisions()

            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)

            for enemy in self.enemies:
                enemy.draw(self.screen)

            # Draw the Block objects
            for block in objects:
                block.draw()

            self.update_bullets(self.player_bullets, self.enemies)
            
            for enemy in self.enemies:
                self.update_bullets(enemy.bullets, self.player)

            if not self.enemies:  # Check if all enemies are defeated
                self.display_victory_message()
                pygame.time.wait(2000)  # Wait for 2 seconds to show the victory message
                self.reset_game()

            if self.player_hits >= 5:  # Check if the player has been hit 5 times
                    self.display_game_over_message()
                    pygame.time.wait(2000)  # Wait for 2 seconds to show the game over message
                    self.reset_game()
                
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        raise SystemExit

    def update_bullets(self, bullets, targets):
        if not isinstance(targets, list):
            targets = [targets]

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
                for target in targets:
                    if bullet.collides_with(target):
                        bullets.remove(bullet)
                        if isinstance(target, Enemy):
                            self.handle_enemy_explosion(target)
                            if target in self.enemies:
                                self.enemies.remove(target)
                        break

                if isinstance(targets[0], Player):
                    if bullet.collides_with(self.player):
                       # bullets.remove(bullet)
                        self.player_hits += 1
        for bullet in bullets:
            bullet.draw(self.screen)
    
    def check_collisions(self):
        for block in objects:
            if self.player.rect.colliderect(block.rect):
                self.handle_player_block_collision(block)

        for enemy in self.enemies:
            for block in objects:
                if enemy.rect.colliderect(block.rect):
                    self.handle_enemy_block_collision(enemy, block)

        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
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

    def handle_enemy_block_collision(self, enemy, block):
        if enemy.rect.colliderect(block.rect):
            if enemy.angle == 0:  # Moving down
                enemy.rect.bottom = block.rect.top
            elif enemy.angle == 90:  # Moving left
                enemy.rect.left = block.rect.right
            elif enemy.angle == 180:  # Moving up
                enemy.rect.top = block.rect.bottom
            elif enemy.angle == 270:  # Moving right
                enemy.rect.right = block.rect.left
            enemy.move_count = 0

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
        self.enemies.remove(enemy)

    def display_victory_message(self):
        victory_text = self.font.render('You Won!', True, (255, 255, 255))
        self.screen.blit(victory_text, (self.width // 2 - victory_text.get_width() // 2,
                                        self.height // 2 - victory_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)

    def display_game_over_message(self):
        game_over_text = self.font.render('Game Over', True, (255, 0, 0))
        self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2,
                                          self.height // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()