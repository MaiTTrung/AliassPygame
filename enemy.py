import pygame
 

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, type = "creep"):
        super().__init__(group)
        
        self.type = type
        self.dict = self.take_attribute()
        
        self.image = pygame.Surface((self.dict["height"], self.dict["width"]))
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()

        self.speed = 50

    
    def take_attribute(self):
        if self.type == "creep":
            return {"hp": 500, "damge": 50,"height":32, "width":32}
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


    def move(self, dt, player):
        self.define_direct(player)

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x 

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    
    def update(self, dt, player, display_surface):
        self.move(dt, player)
        self.hp_bar = Enemy_hp_bar(self)
        self.hp_bar.update()
        self.hp_bar.draw(display_surface)
        

        #self.define_direct(player)


class Enemy_hp_bar():
    def __init__(self, enemy):

        self.image = pygame.Surface((enemy.dict["width"], 20))
        self.image.fill("red")
        self.rect = self.image.get_rect(center = enemy.pos)
        self.enemy_height = enemy.dict["height"]
        self.enemy_pos = enemy.rect.centery

    def follow_object(self):
        self.rect.centery = self.enemy_pos - (self.enemy_height/2 + 30)

    def update(self):
        self.follow_object()

    def draw(self, display_surface):
        
        pygame.draw.rect(display_surface,"red", self.rect)
