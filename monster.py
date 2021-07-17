import pygame
import random

class Monster():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('bloodmoonMonster6.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = 1300
        self.rect.centery = 1300

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def shake(self): # monster shaking animation
        movement_x = random.randrange(-15, 15)
        movement_y = random.randrange(-15, 15)
        self.rect.centerx += movement_x
        self.rect.centery += movement_y

    def unShake(self):
        movement_x = random.randrange(-15, 15)
        movement_y = random.randrange(-15, 15)
        self.rect.centerx -= movement_x
        self.rect.centery -= movement_y

    def teleport(self): # send monster to player
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        print("Monster 1")

class Monster_2():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('bloodmoonMonster6.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = 1300
        self.rect.centery = 1300

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def shake(self): # monster shaking animation
        movement_x = random.randrange(-15, 15)
        movement_y = random.randrange(-15, 15)
        self.rect.centerx += movement_x
        self.rect.centery += movement_y

    def unShake(self):
        movement_x = random.randrange(-15, 15)
        movement_y = random.randrange(-15, 15)
        self.rect.centerx -= movement_x
        self.rect.centery -= movement_y

    def teleport(self): # send monster to player
        self.rect.centerx = pos_x_2
        self.rect.centery = pos_y_2
        print("Monster 2")

class Monster_3():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('bloodmoonMonster6.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = 1300
        self.rect.centery = 1300

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def shake(self): # monster shaking animation
        movement_x = random.randrange(-15, 15)
        movement_y = random.randrange(-15, 15)
        self.rect.centerx += movement_x
        self.rect.centery += movement_y

    def unShake(self):
        movement_x = random.randrange(-15, 15)
        movement_y = random.randrange(-15, 15)
        self.rect.centerx -= movement_x
        self.rect.centery -= movement_y

    def teleport(self): # send monster to player FIX
        self.rect.centerx = pos_x_3
        self.rect.centery = pos_y_3
        print("Monster 3")


class Player():

    def __init__(self, screen, monsterSettings):
        self.screen = screen
        self.monsterSettings = monsterSettings
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.center = float(self.rect.centerx)
        self.upCenter = float(self.rect.centery + 250)

        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_forward = False
        self.moving_backward = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.monsterSettings.speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.monsterSettings.speed
        if self.moving_forward and self.rect.top > 0:
            self.upCenter -= self.monsterSettings.speed
        if self.moving_backward and self.rect.bottom < self.screen_rect.bottom:
            self.upCenter += self.monsterSettings.speed

        self.rect.centerx = self.center
        self.rect.centery = self.upCenter

    def find_player(self): # find player for monster 1
        global pos_x, pos_y
        pos_x = int(self.center)
        pos_y = int(self.upCenter)

    def find_player_2(self): # find player for monster 2
        global pos_x_2, pos_y_2
        pos_x_2 = int(self.center)
        pos_y_2 = int(self.upCenter)

    def find_player_3(self): # find player for monster 2
        global pos_x_3, pos_y_3
        pos_x_3 = int(self.center)
        pos_y_3 = int(self.upCenter)

    def printPos(self):
        print(pos_x, pos_y)

    def printPos_2(self):
        print(pos_x_2, pos_y_2)

    def printPos_3(self):
        print(pos_x_3, pos_y_3)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

