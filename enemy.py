import pygame
import math
 

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, type = "creep"):
        super().__init__(group)
        
        self.type = type
        self.dict = self.take_attribute()
        
        #self.image = pygame.Surface((self.dict["height"], self.dict["width"]))
        self.image = pygame.image.load("animations/enemy/creep.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()

        self.speed = 50

    
    def take_attribute(self):
        if self.type == "creep":
            return {"hp": 500, "damge": 50,"height":64, "width":64}
        elif self.type == "miniboss":
            return {"hp": 500, "damge": 50,"height":150, "width":150}
        else:
            return {"hp": 5000, "damge": 100,"height":300, "width":300}
        
    def define_direct(self, player):
        if player.pos.x - self.pos.x < 0:
            self.direction.x = -1
        elif player.pos.x - self.pos.x > 0:
            self.direction.x = 1
        else:
            self.direction.x = 0 

        if player.pos.y - self.pos.y < 0:
            self.direction.y = -1
        elif player.pos.y - self.pos.y > 0:
            self.direction.y = 1
        else:
            self.direction.y = 0

        #print(self.direction)

    def distanct (self, player):
        return ( math.sqrt( pow(self.pos.x - player.pos.x, 2) + pow(self.pos.y - player.pos.y, 2)) )
    
    def move(self, dt, player):
        self.define_direct(player)
        
        if self.distanct(player) < 1000:
            self.pos.x += self.direction.x * self.speed * dt
            self.rect.centerx = self.pos.x 

            self.pos.y += self.direction.y * self.speed * dt
            self.rect.centery = self.pos.y

    
    def update(self, dt, player, display_surface):
        self.move(dt, player)
        self.hp_bar = Enemy_hp_bar(self)
        self.hp_bar.update()
        self.hp_bar.draw(display_surface)
        self.distanct(player)

    
        

        #self.define_direct(player)


class Enemy_hp_bar():
    def __init__(self, enemy):

        self.height = self.bar_height(enemy)
        self.width = enemy.dict["width"]
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = enemy.pos)
        self.enemy_height = enemy.dict["height"]
        self.enemy_pos = enemy.rect.centery

    def follow_object(self):
        self.rect.centery = self.enemy_pos - (self.enemy_height/2 + 30)
        

    def bar_height(self, enemy):
        if enemy.type == "creep":
            return 10
        elif enemy.type == "miniboss":
            return 15
        else:
            return 20
        
    def update(self):
        self.follow_object()

    def draw(self, display_surface):
        
        pygame.draw.rect(display_surface,"red", self.rect)
