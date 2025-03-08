import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set groups as containers
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT/2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # delta = the amount of time that has passed since the last frame was drawn
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Update the position
        updatable.update(dt)

        pygame.display.flip()
        
        # Pause the loop until 1/60th of a second has passed
        dt = clock.tick(60) / 1000

        # print(f"fps: {pygame.time.Clock.get_fps(clock)}")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()