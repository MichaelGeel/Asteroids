import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    GAME_ON = True
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while GAME_ON:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        dt = game_clock.tick(60)/1000
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.check_collision(player):
                print("Game over!")
                return
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()