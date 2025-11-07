import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt=0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_colision(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.check_colision(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
