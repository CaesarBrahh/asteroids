import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Boot up
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Grouping 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Initialize players and asteroids
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
