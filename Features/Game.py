import pygame
from Tank import Player
from Bullets import Bullet
from Controls import InputManager
from Enemy import Enemy
from Graphics import Block

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
            
            self.enemy.update(self.player)
            self.check_collisions()
            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)

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
            elif bullet.collides_with(target):
                bullets.remove(bullet)
                # Add damage to target here

        for bullet in bullets:
            bullet.draw(self.screen)
    
    def check_collisions(self):
        if self.player.rect.colliderect(self.enemy.rect):
            game_over_text = self.font.render('Game Over', True, (255, 255, 255))
            self.screen.blit(game_over_text, (260, 250))

            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            raise SystemExit

if __name__ == '__main__':
    game = Game()
    game.run()