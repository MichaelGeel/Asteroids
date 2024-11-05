import pygame
import constants

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    GAME_ON = True
    game_clock = pygame.time.Clock()
    dt = 0
    while GAME_ON:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("#000000")
        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        print(dt)


if __name__ == "__main__":
    main()
