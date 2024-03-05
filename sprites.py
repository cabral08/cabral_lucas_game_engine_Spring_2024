#  This file was created by: Lucas Cabral
#  This code was inspired by Zelda and informed by Chris Bradfield
import pygame as pg
from settings import *
#  This allows us to import pygame and imports game settings


#  PLayer class, subclass of pg.sprite.Sprite
class Player(pg.sprite.Sprite):
    #  Initializes the player class
    def __init__(self, game, x, y):
        # inits the super class
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #  makes dimensions for self.image
        self.image = pg.Surface((TILESIZE, TILESIZE))
        #  fills self.image with color (GREEN)
        self.image.fill(GREEN)
        # 
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.moneybag = 0
        self.speed = 300
        self.hitpoints = 100
    
   
    

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -self.speed  
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = self.speed
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -self.speed 
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = self.speed
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071
         
        
    # def move(self, dx=0, dy=0):
    #     if not self.collide_with_walls(dx, dy):
    #         self.x += dx
    #         self.y += dy

    # def collide_with_walls(self, dx=0, dy=0):
    #         for wall in self.game.walls:
    #             if wall.x == self.x + dx and wall.y == self.y + dy:
    #                 return True
    #         return False
            
    # checks collision for walls
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width 
                if self.vx < 0:
                    self.x = hits[0].rect.right
                    # When I pressed s and d i went through walls but I switched the indentation to fix it
                self.vx = 0
                self.rect.x = self.x      
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y 
    # made possible by Aayush's question!!!!
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Coin":
                self.moneybag += 1
            if str(hits[0].__class__.__name__) == "PowerUp":
                print(hits[0].__class__.__name__)
                self.speed += 300
            if str(hits[0].__class__.__name__) == "KillWall":
                print(hits[0].__class__.__name__)
                self.kill()
            if str(hits[0].__class__.__name__) == "Mob":
                print(hits[0].__class__.__name__)
                print("Collided with mob")

    def collide_with_powerup(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.powerups, True)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width 
                if self.vx < 0:
                    self.x = hits[0].rect.right
                    self.vx = 0
                    self.rect.x = self.x  


        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.powerups, True)
        if hits:
                 if self.vy > 0:
                   self.y = hits[0].rect.top - self.rect.height
                 if self.vy < 0:
                  self.y = hits[0].rect.bottom
                  self.vy = 0
                  self.rect.y = self.y 


    def kill(self):
        self.x = self.game.Pcol*TILESIZE
        self.y = self.game.Prow*TILESIZE


    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x 
        # add collision later
        self.collide_with_walls('x')
        # self.collide_with_powerup('x')
        self.rect.y = self.y 
        # add collision later
        self.collide_with_walls('y')
        # self.collide_with_powerup('y')
        self.collide_with_group(self.game.coins, True)
        # if self.collide_with_group(self.game.powerups, True):
        #     self.score += 1
        self.collide_with_group(self.game.power_ups, True)
        self.collide_with_group(self.game.killwall, False)
        self.collide_with_group(self.game.mobs, False)

        

class Wall(pg.sprite.Sprite):
     def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.walls
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(BROWN)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE

     
class KillWall(pg.sprite.Sprite):
     def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.killwall
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(LIGHTGREY)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE

        

# create new class for coin
class Coin(pg.sprite.Sprite):
     def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.coins
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE

class PowerUp(pg.sprite.Sprite):
     def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.power_ups
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(BLUE)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE
# creating a mob class for an enemy
class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx, self.vy = 100, 100
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 1
    def collide_with_walls(self, dir):
        if dir == 'x':
            # print('colliding on the x')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vx *= -1
                self.rect.x = self.x
        if dir == 'y':
            # print('colliding on the y')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vy *= -1
                self.rect.y = self.y
    def update(self):
        # self.rect.x += 1
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        # changed play to player1 so it tracks me
        if self.rect.x < self.game.player1.rect.x:
            self.vx = 100
        if self.rect.x > self.game.player1.rect.x:
            self.vx = -100    
        if self.rect.y < self.game.player1.rect.y:
            self.vy = 100
        if self.rect.y > self.game.player1.rect.y:
            self.vy = -100
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')


           
