import pygame
from settings import *
from player import Player
from player_info_bars import *


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        #sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        self.player = Player( pos = (640,360), group = self.all_sprites)
        
        # UI bars
        self.big_hp_max_bar = Bar(pos=(0,5), group= self.all_sprites, player = self.player, height = 20, width = 350, bar_class = "hp_max",type = "big")
        self.big_hp_bar = Bar(pos=(0,7), group= self.all_sprites, player = self.player, height = 16, width = 330, bar_class = "hp",type = "big", color = "red")

        self.big_energy_max_bar = Bar(pos=(0,23), group= self.all_sprites, player = self.player, height = 20, width = 300, bar_class = "energy_max",type = "big")
        self.big_energy_bar = Bar(pos=(0,25), group= self.all_sprites, player = self.player, height = 16, width = 280, bar_class = "energy",type = "big", color = "blue")

        self.big_sta_max_bar = Bar(pos=(0,41), group= self.all_sprites, player = self.player, height = 20, width = 250, bar_class = "hp_max",type = "big")
        self.big_sta_bar = Bar(pos=(0,43), group= self.all_sprites, player = self.player, height = 16, width = 230, bar_class = "stamina",type = "big", color = "yellow")

        self.skill_bar = Bar(pos=(0,600), group = self.all_sprites, player = self.player, height = 100, width = 1280, bar_class = "stamina_max",type = "big" )

        #self.small_hp_max_bar = Bar(pos = (0,0), group = self.all_sprites, player = self.player, height = 10, width = 100, bar_class = "hp_max",type = "small")
        #self.small_hp_bar = Bar(pos = (0,0), group = self.all_sprites, player = self.player, height = 10, width = 100, bar_class = "hp",color = "red", type = "small")
        # self.small_energy_max_bar = Bar(pos = (0,0), group = self.all_sprites, player = self.player, height = 10, width = 100, bar_class = "energy_max", type = "small")
        # self.small_energy_bar = Bar(pos = (0,0), group = self.all_sprites, player = self.player, height = 10, width = 100, bar_class = "energy",color = "blue", type = "small")
        # self.small_stamina_max_bar = Bar(pos = (0,0), group = self.all_sprites, player = self.player, height = 10, width = 80, bar_class = "stamina_max", type = "small")
        # self.small_stamina_bar = Bar(pos = (0,0), group = self.all_sprites, player = self.player, height = 10, width = 80, bar_class = "stamina",color = "yellow", type = "small")
        

    def run(self, dt):
        self.display_surface.fill("green")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)     


