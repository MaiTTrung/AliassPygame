import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((32,64))
        self.image.fill("green")
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
    

    def input(self):
        keys = pygame.key.get_pressed()
        # go up and down
        if keys[pygame.K_w] and keys[pygame.K_s]:
            self.direction.y = 0
        elif keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else :
            self.direction.y = 0


        # go left and right
        if keys[pygame.K_a] and keys[pygame.K_d]:
            self.direction.x = 0
        elif keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else :
            self.direction.x = 0
        
        
    def move(self, dt):

        self.input()

        if self.direction.x * self.direction.y != 0:
            self.direction = self.direction.normalize()
            print(self.direction)

        # calculate position 
        self.pos += self.direction * self.speed * dt
        self.rect = self.pos

    def update(self, dt):
        self.move(dt)
        