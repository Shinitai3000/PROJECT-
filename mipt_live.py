
from obj import Player, Mob, Bullet
from obj import *
from os import path

pygame.display.set_caption("Та-да-да-дам")
clock = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load(path.join(img_dir, "gametime.jpg")).convert()
background_rect = background.get_rect()



for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

k = 0

running = True

 

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)


    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:   
        running = False


    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()