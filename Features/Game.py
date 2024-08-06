import pygame
from Tank import Player
from Bullets import Bullet
from Controls import InputManager
#from Obstacles import Obstacles

class Game:
    def __init__(self):
        pygame.init()
        self.width , self.height = 800 , 600
        self.screen = pygame.display.set_mode((self.width , self.height))
        pygame.display.set_caption("Tanks")
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.bullets = []
        #self.obstacles = Obstacles()
        self.input = InputManager(self.player, self.bullets)

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
    
        keys = pygame.key.get_pressed()
        self.input.handle_input(keys)

        for bullet in self.bullets:
            bullet.update()
            if bullet.off_screen(self.width, self.height):
                self.bullets.remove(bullet)

        self.scree.fill((0, 0, 0))
        self.player.draw(self.screen)
        for bullet in self.bullets:
                bullet.draw(self.screen)
        for obstacle, color in self.obstacles:
            pygame.draw.rect(self.screen, color, obstacle)
        pygame.display.flip()
        self.clock.tick(60)

        pygame.quit()
        raise SystemExit

if __name__ == '__main__':
    game = Game()
    game.run()