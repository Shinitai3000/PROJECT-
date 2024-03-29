
from obj import Player, Mob, Bullet
from obj import *
from os import path
import math

pygame.display.set_caption("Та-да-да-дам")

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load(path.join(img_dir, "gametime.jpg")).convert()
background_rect = background.get_rect()

clock = pygame.time.Clock()

running = True
timer = 0

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_hp_bar(surf, x, y, color, hp):
    if hp < 0:
        hp = 0
    bar_length = 100
    bar_height = 10
    fill = (hp / 100) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, color, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)
game_over=True
def show_go_screen():
    screen.blit(background,background_rect)
    draw_text(screen, "6ка!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Управление на стрелочки, огонь на пробел ", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Нажми кнопку, чтобы начать", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def flux():
    mob = Mob(mob_img2)
    r = ((player.rect.x - boss.rect.x)**2 + (player.rect.y - boss.rect.y)**2 )**0.5
    a = math.asin((player.rect.x - boss.rect.x) / r)
    mob.speedx = 8 * math.sin(a)
    mob.speedy = 8 * math.cos(a)
    all_sprites.add(mob)
    mobs.add(mob)
    water2_snd.play()
    


while running:
    if game_over:
        show_go_screen()
        time.sleep(1)
        game_over=False
        boss.hp = 100
        player.hp = 100
        boss.speedx = random.randrange(-4, 4)
        boss.speedy = random.randrange(-4, 4)
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 5


    clock.tick(FPS)
    if boss.hp >= 76 and boss.hp >= 0:
        timer = (timer + 1) % 15
        if (timer == 0):
            shoot()
    elif boss.hp <= 75 and boss.hp >= 0:
        timer = (timer + 1) % 17
        if (timer == 0):
            flux()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.QUIT:
                running = False

                
    
    
    all_sprites.update()
    
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.hp -= 5
    
    hits = pygame.sprite.spritecollide(boss, bullets, True, pygame.sprite.collide_circle)
    for hit in hits:
        pain_snd.play()
        boss.hp -= 1

    if player.hp == 0 or boss.hp == 0:
        game_over = True

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    
    draw_hp_bar(screen, WIDTH/2 - 50, 585 , RED, player.hp)
    if boss.hp >= 76:
        d = 0
        draw_hp_bar(screen, WIDTH/2 - 50, 10 , GREEN, boss.hp)
    elif boss.hp <= 75:
        if d == 0:
            stage2_snd.play()
            d = 1 
        draw_hp_bar(screen, WIDTH/2 - 50, 10 , YELLOW, boss.hp)

    
    
    pygame.display.flip()

pygame.quit()
