# This file was created by: Lucas Cabral


# Importing Modules
import pygame as pg 
from settings import *
from sprites import *
from random import randint 
import sys
# Makes me able to import pictures and graphics
from os import path




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
    def load_data(self):
        game_folder = path.dirname(__file__)
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
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
    # Create run method which runs the whole GAME
    def new(self):
        # create player
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player1 = Player(self, 1, 1)
        self.all_sprites.add(self.player1)
        self.powerups = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                # if tile == 'P':
                #     self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)
   
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

    def draw_grid(self):
         for x in range(0, WIDTH, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
         for y in range(0, HEIGHT, TILESIZE):
              pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
                
    def draw(self):
          self.screen.fill(BGCOLOR)
          self.draw_grid()
          self.all_sprites.draw(self.screen)
          pg.display.flip()
# Events such as moving, enemies spawning etc
    def events(self):
         for event in pg.event.get():
              if event.type == pg.QUIT:
                   self.quit()
          
# Instantiate the game...
g = Game()
#  use game method run to run
# g.show_start_screen()
while True:
    #   create new game
    g.new()
    #   run the game
    g.run()
    #  g.show_go_screen
