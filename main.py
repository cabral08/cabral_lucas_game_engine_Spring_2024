# This file was created by: Lucas Cabral
# Added this comment to prove github is working
# new stuff
# Importing Modules
import pygame as pg 
from settings import *
from sprites import *
from random import randint 
import sys
from os import path
import os
from math import floor
# Makes me able to import pictures and graphics

# Alpha Project
'''
mob
killwall
animated sprites
start screen
'''

# Beta Project
'''
new level/s
'''
# Final addition
'''
shop
'''

# added levels for different maps
LEVEL1 = "lvl1.txt"
LEVEL2 = "lvl2.txt"

# Creating the Base blueprint
class Game:
    # Initializer -- sets up the game
    def __init__(self):
        # Settings -- set canvas width, height, and title
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption((TITLE))
        #  Setting up pygame clock
        self.clock = pg.time.Clock()
        # Boolean to check whether game is running or not
        self.load_data()

        # self.shop_open = False
        # self.shop_items = {
        #     "Sword": 50,
        #     "Shield": 30,
        #     "Potion": 20
        # }
        # self.player_money = 100
        # self.player_inventory = []
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.img_folder = path.join(self.game_folder, 'images')
        self.snd_folder = path.join(self.game_folder, 'sounds')

        self.map_data = []
        # 'r'     open for reading (default)
        # 'w'     open for writing, truncating the file first
        # 'x'     open for exclusive creation, failing if the file already exists
        # 'a'     open for writing, appending to the end of the file if it exists
        # 'b'     binary mode
        # 't'     text mode (default)
        # '+'     open a disk file for updating (reading and writing)
        # 'U'     universal newlines mode (deprecated)
        # below opens file for reading in text mode
        # with 
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        with open(path.join(self.game_folder, 'lvl1.txt'), 'rt') as f:
            for line in f:
                # print(line)
                self.map_data.append(line)

    def change_level(self, lvl):
        self.currlvl = lvl
        
        # kill all existing sprites first to save memory
        for s in self.all_sprites:
            s.kill()
        # reset criteria for changing level
        self.player1.moneybag = 0
        # reset map data list to empty
        self.map_data = []
        # open next level
        with open(path.join(self.game_folder, lvl), 'rt') as f:
            for line in f:
                # print(line)
                self.map_data.append(line)
        # repopulate the level with stuff
        for row, tiles in enumerate(self.map_data):
            # print(row)
            for col, tile in enumerate(tiles):
                # print(col)
                if tile == '1':
                    # print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                    print("change level")
                if tile == 'U':
                    PowerUp(self, col, row)
                if tile == 'H':
                    HealthPotion(self, col, row)
                if tile == 'T':
                    PlantTrap(self, col, row)
                # if tile == 'B':
                #     BossMob(self, col, row)

    # def draw_shop(self):
    #     self.screen.fill(BGCOLOR)
    #     self.draw_text(self.screen, "Welcome to the Shop", 48, BLUE, WIDTH/3.7, HEIGHT/2.2)
    #     # Display shop items and prices
    #     y = HEIGHT / 2
    #     for item, price in self.shop_items.items():
    #         self.draw_text(self.screen, f"{item}: ${price}", 24, WHITE, WIDTH/3, y)
    #         y += 30
    #     # Display player's money
    #     self.draw_text(self.screen, f"Your Money: ${self.player_money}", 24, WHITE, WIDTH/3, y+30)

    # def shop(self):
    #     self.show_start_screen()
    #     while True:
    #         self.draw_shop()
    #         pg.display.flip()
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 self.quit()
    #             elif event.type == pg.KEYUP:
    #                 if event.key == pg.K_SPACE:
    #                     return

    # def buy_item(self, item):
    #     if item in self.shop_items:
    #         price = self.shop_items[item]
    #         if self.player_money >= price:
    #             self.player_money -= price
    #             self.player_inventory.append(item)
    #             print(f"You bought {item} for ${price}")
    #         else:
    #             print("Not enough money!")
    #     else:
    #         print("Item not found in the shop.")

    # def show_inventory(self):
    #     print("Inventory:")
    #     for item in self.player_inventory:
    #         print("-", item)

    # def run(self):
    #     self.playing = True
    #     while self.playing:
    #         # Run game logic...
    #         if need_to_open_shop:
    #             self.shop()
    #             need_to_open_shop = False
    #         if need_to_display_inventory:
    #             self.show_inventory()
    #             need_to_display_inventory = False

    # def run(self):
    #     self.playing = True
    #     while self.playing:
    #         self.events()
    #         if self.shop_open:
    #             self.shop()
    #         else:
    #             # Run other game logic...
    #             pass

    # Create run method which runs the whole GAME
    def new(self):
        # create player
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        #self.all_sprites.add(self.player1)
        self.powerups = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.killwall = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            # print(row)
            for col, tile in enumerate(tiles):
                # print(col)
                if tile == '1':
                    # print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'K':
                    # print("death at", row, col)
                    KillWall(self, col, row)
                # spawns another player, but there are two
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'P':
                    self.player1 = Player(self, col, row)

    # def drawWeaponOverlay(self):
    #         for i, item in enumerate(self.player1.loadout):
    #          box = pg.draw.rect(self.screen, GREEN if item.enabled else LIGHTGREY, (20 + 80*i, HEIGHT - 80, 60, 60), 3)
    #         img = item.img_overlay.copy()
    #         img_rect = img.get_rect(center=box.center)
    #         self.screen.blit(img, img_rect)


   
    # Runs our game
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
    def quit(self):
         pg.quit()
         sys.exit()
#  updates the sprites
    def update(self):
         self.all_sprites.update()
         if self.player1.moneybag > 2:
             self.change_level(LEVEL2)

    def draw_grid(self):
         for x in range(0, WIDTH, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
         for y in range(0, HEIGHT, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        surface.blit(text_surface, text_rect)
                
    def draw(self):
          self.screen.fill(BGCOLOR)
          self.draw_grid()
          self.all_sprites.draw(self.screen)
          pg.display.flip()
        #   self.drawWeaponOverlay()

# Events such as moving, enemies spawning etc
    def events(self):
         for event in pg.event.get():
              if event.type == pg.QUIT:
                   self.quit()
# made a start scree: Project 4
    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(self.screen, "Press any button to play", 48, BLUE, WIDTH/3.7, HEIGHT/2.2)
        pg.display.flip()
        self.wait_for_key()
    
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False
        
# Instantiate the game...
g = Game()
#  use game method run to run
g.show_start_screen()
while True:
    #   create new game
    g.new()
    #   run the game
    g.run()
    #  g.show_go_screen
