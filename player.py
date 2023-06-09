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
        self.status = "down_idle"

    def input(self):
        keys = pygame.key.get_pressed()
        # go up and down
        if keys[pygame.K_w] and keys[pygame.K_s]:
            self.direction.y = 0
        elif keys[pygame.K_w]:
            self.direction.y = -1
            self.status = "move_up"
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = "move_down"
        else :
            self.direction.y = 0


        # go left and right
        if keys[pygame.K_a] and keys[pygame.K_d]:
            self.direction.x = 0
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = "move_left"
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.status = "move_right"
        else :
            self.direction.x = 0
        
        
    def move(self, dt):

        self.input()

        if self.direction.x * self.direction.y != 0:
            self.direction = self.direction.normalize()
            

        # horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def animation(self):
        path = "/animations/" 

        self.animations = {"move_up":[], "move_down":[], "move_right":[], "move_left":[],
                          "up_idle":[], "down_idle":[], "right_idle":[], "left_idle":[]}
        for animation in self.animations.keys():
            print(path + animation)

    def update(self, dt):
        self.move(dt)
        self.animation()
        
