import sys

import pygame

from settings import Settings
from ship import Ship
from bulletpanks import Treat

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

    ## full screen setting:
       # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
       # self.settings.screen_width = self.screen.get_rect().width
       # self.settings.screen_height = self.screen.get_rect().height

    ## windowed mode:
        self.screen = pygame.display.set_mode(
             (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.treats = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_treats()
            self._update_screen()
            
        # Redraw the screen during each pass through the loop.
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        print("Checking events")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _check_keydown_events(self, event):
        """Respond to Keypress."""
        print("Keydown event")
        if event.key == pygame.K_RIGHT:
                    # Move the ship to the right.
                self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  
                    # Move the ship to the left.
                self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
             self._fire_treat()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
    
    def _fire_treat(self):
         """Create a new treat and add it to the treats group."""
         print("Firing treat")  
         if len(self.treats) < self.settings.treats_allowed:
            new_treat = Treat(self, self.ship)
             # Set the treat's initial position relative to the ship's position
            new_treat.rect.midtop = self.ship.rect.midtop
            self.treats.add(new_treat)
            

    def _update_treats(self):
        """Update psootion of treats and get rid of old treats."""
        # Update treat positions.
        self.treats.update()
        # Get rid of treats that have disappeared.
        for treat in self.treats.copy():
            if treat.rect.bottom <= 0:
                self.treats.remove(treat)
            # print number of treats out to verify they are being properly removed : : print(len(self.treats))
    
    def _update_screen(self):
         """Update images on the screen, and flip to the new screen."""
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()
         self.treats.draw(self.screen)  # Use draw method to draw all treats

         
         # Make the most recently drawn screen visible.
         pygame.display.flip()
         

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
