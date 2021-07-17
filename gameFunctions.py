import pygame
from settings import Settings
import sys
import time
import pygame.freetype
import pygame.font

dead = False

def keydownEvents(event, player):
    if event.key == pygame.K_RIGHT:  # move right
        player.moving_right = True
    elif event.key == pygame.K_LEFT:  # move left
        player.moving_left = True
    elif event.key == pygame.K_UP:  # move forward
        player.moving_forward = True
    elif event.key == pygame.K_DOWN:
        player.moving_backward = True

def keyupEvents(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_forward = False
    elif event.key == pygame.K_DOWN:
        player.moving_backward = False

def check_events(player):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydownEvents(event, player)
        elif event.type == pygame.KEYUP:
            keyupEvents(event, player)


def update_screen(bloodmoonSettings, screen, monster, player, monster_2, monster_3, message, font):
    bloodmoonSettings = Settings()
    # set bg
    screen.fill(bloodmoonSettings.bg_color)

    # generate monster
    monster.blitme()

    # generate player
    player.blitme()

    monster_2.blitme()

    monster_3.blitme()


    print_message(screen, message, font, (1100, 20))
    # update display
    pygame.display.flip()

def detect_collision(player, monster, monster_2, monster_3):
    global dead
    if player.rect.centerx < monster.rect.right and player.rect.centerx > monster.rect.left and player.rect.centery < monster.rect.bottom and player.rect.centery > monster.rect.top:
        print("DEATH")
        dead = True
    if player.rect.centerx < monster_2.rect.right and player.rect.centerx > monster_2.rect.left and player.rect.centery < monster_2.rect.bottom and player.rect.centery > monster_2.rect.top:
        print("DEATH")
        dead = True
    if player.rect.centerx < monster_3.rect.right and player.rect.centerx > monster_3.rect.left and player.rect.centery < monster_3.rect.bottom and player.rect.centery > monster_3.rect.top:
        print("DEATH")
        dead = True

def game_over(screen):
    """Print game over message/image"""
    time.sleep(1.1)
    bg_image = pygame.image.load('Bloodmoon Game Over.png').convert()
    bg_image = pygame.transform.scale(bg_image, (1200, 800))
    screen.blit(bg_image, [0,0])
    pygame.display.flip()
    time.sleep(0.5)

def print_message(screen, message, font, position):
    text = font.render(message, True, (179, 0, 0))
    screen.blit(text, position)
    pygame.display.update()


def victory(screen):
    time.sleep(1.1)
    victoryImage = pygame.image.load('VictoryNew.png').convert()
    victoryImage = pygame.transform.scale(victoryImage, (1200, 800))
    screen.blit(victoryImage, [0,0])
    pygame.display.flip()
