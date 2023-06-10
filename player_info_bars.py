import pygame
from settings import *


class Bar(pygame.sprite.Sprite):
    def __init__(self, pos, group, height, width ,bar_class ,type, color = "black"):
        super().__init__(group)
        
        self.max_width_bar = width
        self.bar_width = width
        self.bar_height = height
        self.bar_color = color
        self.image = pygame.Surface((self.max_width_bar,self.bar_height))
        self.image.fill(color)
        self.rect =self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.bar_class = bar_class
        self.bar_type = type
           

    
    def get_text(self):
        pass

    def follow_object(self):
        pass
        # if self.bar_type == "small":
        #     if self.bar_class == "hp" or self.bar_class == "hp_max":
        #         self.pos.x = player.pos.x - 50
        #         self.pos.y = player.pos.y - 74
        #     elif self.bar_class == "energy" or self.bar_class == "energy_max":
        #         self.pos.x = player.pos.x - 50
        #         self.pos.y = player.pos.y - 64
        #     elif self.bar_class == "stamina" or self.bar_class == "stamina_max":
        #         self.pos.x = player.pos.x - 50
        #         self.pos.y = player.pos.y - 54
        # else:
        #     pass

        # self.rect = self.pos

    def update_hp_bar(self, player):
        if self.bar_class == "hp":

            self.bar_width = player.hp * (self.max_width_bar / player.hp_max) 
            self.image = pygame.Surface((self.bar_width,self.bar_height))
            self.image.fill(self.bar_color) 
        else:
            pass
    
    def update_stamina_bar(self, player):
        if self.bar_class == "stamina":

            self.bar_width = player.stamina * (self.max_width_bar / player.stamina_max) 
            self.image = pygame.Surface((self.bar_width,self.bar_height))
            self.image.fill(self.bar_color) 
        else:
            pass
    
    def update_energy_bar(self, player):
        if self.bar_class == "energy":

            self.bar_width = player.energy * (self.max_width_bar / player.energy_max) 
            self.image = pygame.Surface((self.bar_width,self.bar_height))
            self.image.fill(self.bar_color) 
        else:
            pass



    def update(self, dt, player):
        self.get_text()
        self.follow_object()
        self.update_hp_bar(player)
        self.update_energy_bar(player)
        self.update_stamina_bar(player)
        