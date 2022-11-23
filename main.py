import pygame
import sys
from settings import *
from level import Level
from overworld import Overworld
from support import read_data, write_data
from ui import UI


class Game:
    def __init__(self):
        # stats
        self.level = None
        self.data = read_data()
        self.max_level = self.data['max_level']
        self.max_health = 100
        self.current_health = 100
        self.coins = 0

        # audio
        self.level_bg_music = pygame.mixer.Sound('./audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('./audio/overworld_music.wav')

        # overworld
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops=-1)

        # UI
        self.ui = UI(screen)

    def create_level(self, current):
        self.level = Level(current, screen, self.create_overworld, self.increase_coins, self.change_health)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops=-1)

    def create_overworld(self, current_level, new_max):
        if new_max > self.max_level:
            self.max_level = new_max
            write_data('max_level', new_max)
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops=-1)
        self.level_bg_music.stop()

    def increase_coins(self, amount):
        self.coins += amount

    def change_health(self, amount):
        self.current_health += amount

    def check_game_over(self):
        if self.current_health <= 0:
            self.current_health = 100
            self.coins = 0
            self.max_level = self.data['max_level']
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.current_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()


# Pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()
pygame.display.set_caption("CupHeads")

top = pygame.image.load('./graphics/bg/1.png').convert()
top = pygame.transform.scale(top, (screen_width, screen_height))
middle = pygame.image.load('./graphics/bg/2.png').convert()
middle = pygame.transform.scale(middle, (screen_width, screen_height))
bottom = pygame.image.load('./graphics/bg/3.png').convert()
bottom = pygame.transform.scale(bottom, (screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    screen.blit(top, (0, 0))
    screen.blit(middle, (0, 0))
    screen.blit(bottom, (0, 0))
    game.run()
    pygame.display.update()
    clock.tick(60)
