import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacle_sprites):
        super().__init__(group)

        #animation sprite 
        self.image = pygame.image.load("animations/idle/0.png")
        #self.image.fill("black")
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.obstacle_sprites = obstacle_sprites
        # attributes
        self.hp_max = 10
        self.hp = 10
        self.stamina_max = 10
        self.stamina = 10
        self.energy_max = 200
        self.energy = 200
        self.speed = 200
        self.status = "idle"
        
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left

                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0 :
                        self.rect.top = sprite.rect.bottom
                        
    def input(self,dt):
        # get button & mouse
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        #print(mouse)
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
            
        # leftshift
        if keys[pygame.K_LSHIFT]:
            self.speed_up(dt)
        else:
            self.speed = 200
            self.back_stamina(dt)
    
    

    def speed_up(self,dt):
        if self.stamina > 0 and self.direction.magnitude() > 0:
            self.speed = 400
            self.stamina = self.stamina - (1  * 1.7 * dt)

        else:
            self.speed = 200

            
    def back_stamina(self, dt):
        if self.stamina < self.stamina_max:
                self.stamina = self.stamina + (1  * dt)
            
    def move(self, dt):

        self.input(dt)

        if self.direction.x * self.direction.y != 0:
            self.direction = self.direction.normalize()
        elif self.direction.x + self.direction.y == 0:
            self.status = "idle"    

        # horizontal
        self.rect.x += self.direction.x * self.speed * dt
        #self.rect.centerx = self.pos.x
        self.pos.x = self.rect.centerx
        self.collision("horizontal")
        # vertical
        self.rect.y += self.direction.y * self.speed * dt
        #self.rect.centery = self.pos.y
        self.pos.y = self.rect.centery
        self.collision("vertical")

    def animation(self):
        path = "/animations/" 

        self.animations = {"move_up":[], "move_down":[], "move_right":[], "move_left":[],
                          "idle":[]}
        for animation in self.animations.keys():
            animation_path = (path + animation)



    def get_player_infor(self):
        return {"status": self.status, "hp": self.hp, "hp_max": self.hp_max, "speed":self.speed, "stamina": self.stamina, "max_stamina": self.stamina_max
                , "energy": self.energy, "energy_max": self.energy_max}
    
    def attack():
        pass
    
    def update(self, dt):
        self.move(dt)
        self.animation()
        
