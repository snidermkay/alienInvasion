import pygame
from pygame.sprite import Sprite

class Treat(Sprite):
    """A class to manage treats fired from the ship."""

    def __init__(self, ai_game, ship):
        """Create a treat object at the ship's initial position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/treat.bmp')
        self.rect = self.image.get_rect()
        self.ship = ship  # Store the ship instance

    def update(self):
        """Move the treat up the screen."""
        # Update the decimal portion of the treat.
        self.rect.y -= self.settings.treat_speed

        # Adjust treat position based on ship movement
        self.rect.x = self.ship.rect.x
        self.rect.y += self.ship.rect.y

    def draw_treat(self):
        """Draw the treat to the screen."""
        self.screen.blit(self.image, self.rect)
