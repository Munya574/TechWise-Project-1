import pygame
import random

class Obstacle:
    def __init__(self, x, y, image):
        """
        Initialize the obstacle.
        :param x: The x-coordinate of the obstacle.
        :param y: The y-coordinate of the obstacle.
        :param image: The image used to represent the obstacle.
        """
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        """
        Draw the obstacle on the given surface.
        :param surface: The surface on which to draw the obstacle.
        """
        surface.blit(self.image, self.rect)

    def check_collision(self, player_rect):
        """
        Check if the obstacle collides with the player.
        :param player_rect: The player's rectangle (position and size).
        :return: True if there is a collision, False otherwise.
        """
        return self.rect.colliderect(player_rect)

    @staticmethod
    def load_obstacle_images(image_paths):
        """
        Load obstacle images from the given list of paths.
        :param image_paths: A list of paths to obstacle images.
        :return: A list of loaded images.
        """
        return [pygame.image.load(path).convert_alpha() for path in image_paths]

    @staticmethod
    def create_random_obstacles(count, screen_width, screen_height, obstacle_images):
        """
        Create a list of obstacles placed at random positions on the screen.
        :param count: Number of obstacles to create.
        :param screen_width: Width of the screen.
        :param screen_height: Height of the screen.
        :param obstacle_images: List of obstacle images to choose from.
        :return: A list of Obstacle instances.
        """
        obstacles = []
        for _ in range(count):
            while True:
                x = random.randint(0, screen_width - 40)
                y = random.randint(0, screen_height - 40)
                rect = pygame.Rect(x, y, 40, 40)
                if not any(ob.rect.colliderect(rect) for ob in obstacles):
                    obstacle = Obstacle(x, y, random.choice(obstacle_images))
                    obstacles.append(obstacle)
                    break
        return obstacles

# Example usage in a game setup
if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()
    
    # Create a display window
    screen = pygame.display.set_mode((800, 600))
    
    # Load obstacle images from file paths
    obstacle_image_paths = [
        'images/bricks.png',
        'images/blocks.png',
        'images/water.png',
    ]
    obstacle_images = Obstacle.load_obstacle_images(obstacle_image_paths)

    # Create a list of random obstacles
    obstacles = Obstacle.create_random_obstacles(20, 800, 600, obstacle_images)

    # Load player image and create a rect for positioning
    player_img = pygame.image.load('images/pic.png').convert_alpha()
    player_rect = player_img.get_rect(center=(400, 300))

    # Check for initial overlaps with obstacles
    for obstacle in obstacles:
        if obstacle.check_collision(player_rect):
            print("Initial overlap detected with an obstacle! Adjust player position.")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Draw obstacles
        for obstacle in obstacles:
            obstacle.draw(screen)

        # Draw the player on the screen
        screen.blit(player_img, player_rect)

        # Update the display
        pygame.display.flip()

    # Quit Pygame when the game loop ends
    pygame.quit()
