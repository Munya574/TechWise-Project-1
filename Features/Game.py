import pygame
from Tank import Player
from Bullets import Bullet
from Controls import InputManager

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tanks")
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.bullets = []
        self.input_manager = InputManager(self.player, self.bullets)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.input_manager.handle_input(keys)
            for bullet in self.bullets:
                bullet.update()
                if bullet.off_screen(self.width, self.height):
                    self.bullets.remove(bullet)

            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            for bullet in self.bullets:
                bullet.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        raise SystemExit

if __name__ == '__main__':
    game = Game()
    game.run()