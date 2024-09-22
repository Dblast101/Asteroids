import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   

        for cursor in updatable:
            cursor.update(dt)
        
        for obj in asteroids:
            if obj.collision(player):
                print("Game over!")
                sys.exit()
            
            for bullet in shots:
                if obj.collision(bullet):
                    bullet.kill()
                    obj.split()

        screen.fill("black")
        
        for cursor in drawable:
            cursor.draw(screen)
        
        pygame.display.flip()

        dt = fps.tick(60) / 1000

    



if __name__ == "__main__":
    main()