import pygame
import random

from os import path
WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

img_dir = path.join(path.dirname(__file__), 'img')

player_img = pygame.image.load(path.join(img_dir, "student.png")).convert()
mob_img = pygame.image.load(path.join(img_dir, "water.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "bull.png")).convert()
boss_img = pygame.image.load(path.join(img_dir, "boss.png")).convert()

all_sprites = pygame.sprite.Group()

mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()



class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (100, 80))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 5
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):    
        bullet = Bullet( self.rect.centerx,  self.rect.top)
        print(bullet.rect.bottom)
        all_sprites.add(bullet)
        bullets.add(bullet)

player = Player()
all_sprites.add(player)

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(boss_img, (200, 160))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.top = 100
        self.speedy = random.randrange(1, 4)
        self.speedx = 0
        
    def update(self):
        self.speedx = player.speedx 
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > 150 or self.rect.bottom < 30:
            self.speedy = - self.speedy


boss = Boss()
all_sprites.add(boss)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.transform.scale(mob_img, (50, 38))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = boss.rect.x
        self.rect.y = boss.rect.y
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):


    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (30, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
            



    




