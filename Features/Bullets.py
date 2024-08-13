import pygame

class Bullet:
    def __init__(self, x, y, speed, direction, image_path, size=(15, 10)):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, size) 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = direction

    def update(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def off_screen(self, width, height):
        return (self.rect.bottom < 0 or self.rect.top > height or
                self.rect.right < 0 or self.rect.left > width)
    
    def collides_w_enemy(self, enemy):
        return self.rect.colliderect(enemy.rect)