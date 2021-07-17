import pygame
from settings import Settings
from monster import Monster, Player, Monster_2, Monster_3
import gameFunctions as gf
import time
import sys
import pygame.freetype
import bloodmoonGateway

# font stuff
pygame.init()
big_font = pygame.font.Font(None, 150)
small_font = pygame.font.Font(None, 75)
global success
bloodmoonGateway.new_success = None


def runGame():
    pygame.init()
    bloodmoonSettings = Settings()
    screen = pygame.display.set_mode((bloodmoonSettings.screen_width, bloodmoonSettings.screen_height))
    pygame.display.set_caption("Bloodmoon")
    coordsUpdateTimer = 0  # time since last checked player coordinates for monster movement
    coordsUpdateTimer_2 = 0
    coordsUpdateTimer_3 = 0
    timeSinceShake = 0  # time since monster shook
    timeSinceTP = 0  # time since monster teleported
    timeSinceTP_2 = 0
    timeSinceTP_3 = 0
    global score
    score = 0
    clock = pygame.time.Clock()

    # playtime clock

    monster = Monster(screen)
    monster_2 = Monster_2(screen)
    monster_3 = Monster_3(screen)
    player = Player(screen, bloodmoonSettings)

    gf.check_events(player)
    player.update()
    gf.update_screen(bloodmoonSettings, screen, monster, player, monster_2, monster_3, str(score), small_font)

    while True:
        # Watch for keyboard and mouse events; update the screen
        gf.check_events(player)
        player.update()
        gf.update_screen(bloodmoonSettings, screen, monster, player, monster_2, monster_3, str(score), small_font)
        gf.detect_collision(player, monster, monster_2, monster_3)
        if gf.dead:
            gf.game_over(screen)
            gf.print_message(screen, "GAME OVER", big_font, (300, 50))
            time.sleep(3)
            print("You died.")
            bloodmoonGateway.new_success = False
            sys.exit()

        # the clock is ticking...
        dt = clock.tick()
        coordsUpdateTimer += dt
        coordsUpdateTimer_2 += dt
        coordsUpdateTimer_3 += dt
        timeSinceShake += dt
        timeSinceTP += dt
        timeSinceTP_2 += dt
        timeSinceTP_3 += dt

        # coords updates
        if coordsUpdateTimer > 1500:
            player.find_player()
            player.printPos()
            monster.shake()
            coordsUpdateTimer = 0
            timeSinceTP = 2000
        if coordsUpdateTimer_2 > 2500:
            player.find_player_2()
            monster_2.unShake()
            player.printPos_2()
            coordsUpdateTimer_2 = 0
            timeSinceTP_2 = 3500
        if coordsUpdateTimer_3 > 5000:
            player.find_player_3()
            player.printPos_3()
            coordsUpdateTimer_3 = 0
            monster_3.unShake()
            timeSinceTP_2 = 6000

            # change to 1 for a good time
            for i in range(3):
                monster.shake()
                monster_2.shake()
                monster_3.unShake()
                gf.update_screen(bloodmoonSettings, screen, monster, player, monster_2, monster_3, str(score),
                                 small_font)
                pygame.time.wait(25)
                monster.unShake()
                monster_2.unShake()
                monster_3.shake()
                gf.update_screen(bloodmoonSettings, screen, monster, player, monster_2, monster_3, str(score),
                                 small_font)
            timeSinceShake = 0

        # teleportation
        if timeSinceTP > 3000:
            monster.teleport()
            monster_3.shake()
            timeSinceTP = 0
            score += 1
        if timeSinceTP_2 > 6000:
            monster_2.teleport()
            monster.unShake()
            timeSinceTP_2 = 0
            score += 1
        if timeSinceTP_3 > 9500:
            monster_3.teleport()
            monster_2.shake()
            timeSinceTP_3 = 0
            score += 1

        if score >= 10:
            gf.victory(screen)
            time.sleep(3)
            bloodmoonGateway.new_success = True
            sys.exit()


if __name__ == '__main__':
    runGame()
