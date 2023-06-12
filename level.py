import pygame
from settings import *
from player import Player
from tile import Tile
from player_info_bars import *
from enemy import *
from readmap import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.display_surface.fill("green")
        #sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.UI_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_hp_bar_sprite = pygame.sprite.Group()
        self.create_map()
        self.setup()


    def setup(self):
        #self.player = Player( pos = (640,360), group = self.player_sprites)
        self.enemy = Enemy(pos = (450,500), group = self.enemy_sprites, type = "boss")
        self.enemy = Enemy(pos = (0, 0 ), group = self.enemy_sprites, type = "creep")
        
        # UI bars
        self.big_hp_max_bar = Bar(pos=(0,5), group= self.UI_sprites, height = 20, width = 350, bar_class = "hp_max",type = "big")
        self.big_hp_bar = Bar(pos=(0,7), group= self.UI_sprites, height = 16, width = 330, bar_class = "hp",type = "big", color = "red")

        self.big_energy_max_bar = Bar(pos=(0,23), group= self.UI_sprites, height = 20, width = 300, bar_class = "energy_max",type = "big")
        self.big_energy_bar = Bar(pos=(0,25), group= self.UI_sprites, height = 16, width = 280, bar_class = "energy",type = "big", color = "blue")

        self.big_sta_max_bar = Bar(pos=(0,41), group= self.UI_sprites, height = 20, width = 250, bar_class = "hp_max",type = "big")
        self.big_sta_bar = Bar(pos=(0,43), group= self.UI_sprites, height = 16, width = 230, bar_class = "stamina",type = "big", color = "yellow")

        #self.skill_bar = Bar(pos=(0,600), group = self.UI_sprites, height = 100, width = 1280, bar_class = "stamina_max",type = "big" )

    def create_map(self):
        for row_index, row in enumerate(map_1):
            for col_index, col in enumerate(row):
                x = col_index * TITLE_SIZE
                y =  row_index * TITLE_SIZE
                if col == 1:
                    Tile((x,y),self.visible_sprites)
                if col == 'p':
                    self.player = Player((x,y), self.player_sprites, self.enemy_sprites)
                



    def run(self, dt):
        self.display_surface.fill("green")
        

        self.visible_sprites.draw(self.display_surface)
        self.enemy_sprites.draw(self.display_surface)
        self.player_sprites.draw(self.display_surface)
        self.UI_sprites.draw(self.display_surface)
        

        self.visible_sprites.update(self.display_surface)
        self.enemy_sprites.update( dt, self.player, self.display_surface) 
        self.player_sprites.update(dt)
        self.UI_sprites.update(dt, self.player)
        

        #print()

        


