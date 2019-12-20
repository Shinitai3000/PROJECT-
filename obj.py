import pygame
import random

from os import path
WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

player_img = pygame.image.load(path.join(img_dir, "student.png")).convert()
mob_img1 = pygame.image.load(path.join(img_dir, "water.png")).convert()
mob_img2 = pygame.image.load(path.join(img_dir, "water2.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "bull.png")).convert()
boss_img = pygame.image.load(path.join(img_dir, "boss.png")).convert()

shoot_snd = pygame.mixer.Sound(path.join(snd_dir, 'water.wav'))
shoot_snd.set_volume(0.2)
pain_snd = pygame.mixer.Sound(path.join(snd_dir, 'pain.wav'))
stage2_snd = pygame.mixer.Sound(path.join(snd_dir, 'stage2.wav'))

all_sprites = pygame.sprite.Group()

mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (100, 80))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 5
        self.speedx = 0
        self.speedy = 0
        self.hp = 100

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        
        if keystate[pygame.K_UP]:
            self.speedy = -8
        
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        
        self.rect.y += self.speedy
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        if self.rect.top > HEIGHT - 100:
            self.rect.top = HEIGHT - 100
        if self.rect.bottom < 100:
            self.rect.bottom = 100

    def shoot(self):    
        bullet = Bullet( self.rect.centerx,  self.rect.top)
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
        self.speedy = random.randrange(-4 , 4)
        self.speedx = random.randrange(-4 , 4)
        self.radius = 50
        self.hp = 100
        
    def update(self): 
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.top > 150 or self.rect.bottom < 120:
            self.speedy = - self.speedy
        if self.rect.left < -30 or self.rect.right > 540:
            self.speedx = - self.speedx
        if boss.hp < 0:
            boss.kill()
def shoot():
    mob = Mob(mob_img1)
    all_sprites.add(mob)
    mobs.add(mob)
    shoot_snd.play()


boss = Boss()
all_sprites.add(boss)

class Mob(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.transform.scale(img, (50, 38))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = boss.rect.x + 60
        self.rect.y = boss.rect.y + 95
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.radius = 30
    def update(self):
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.kill()


class Bullet(pygame.sprite.Sprite):


    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (30, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        self.radius = 10
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
            



    




