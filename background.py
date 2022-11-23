import pygame
from settings import vertical_tile_number, tile_size, screen_width

# def draw_bg(screen):
#     # Define game variable
#     scroll = 0
#
#     bg_images = []
#
#     for i in range(1, 7):
#         image = pygame.image.load(f'./graphics/bg/{8 - i}.png').convert_alpha()
#         bg_image = pygame.transform.scale(image, (500, screen_height))
#         bg_images.append(bg_image)
#
#     bg_width = bg_images[0].get_width()
#
#     for x in range(6):
#         speed = 1
#         for k in bg_images:
#             screen.blit(k, ((x * bg_width) - scroll*speed, 0))
#             speed += 0.2



class background:
    def __init__(self, horizon, style='level'):
        self.top = pygame.image.load('./graphics/bg/1.png').convert()
        self.bottom = pygame.image.load('./graphics/bg/2.png').convert()
        self.middle = pygame.image.load('./graphics/bg/3.png').convert()
        self.horizon = horizon

        # self.style = style
        # if self.style == 'overworld':
        #     palm_surfaces = import_folder('../graphics/overworld/palms')
        #     self.palms = []
        #
        #     for surface in [choice(palm_surfaces) for image in range(10)]:
        #         x = randint(0, screen_width)
        #         y = (self.horizon * tile_size) + randint(50, 100)
        #         rect = surface.get_rect(midbottom=(x, y))
        #         self.palms.append((surface, rect))
        #
        #     cloud_surfaces = import_folder('../graphics/overworld/clouds')
        #     self.clouds = []
        #
        #     for surface in [choice(cloud_surfaces) for image in range(10)]:
        #         x = randint(0, screen_width)
        #         y = randint(0, (self.horizon * tile_size) - 100)
        #         rect = surface.get_rect(midbottom=(x, y))
        #         self.clouds.append((surface, rect))

    def draw(self, surface):
        for row in range(vertical_tile_number):
            y = row * tile_size
            if row < self.horizon:
                surface.blit(self.top, (0, y))
            elif row == self.horizon:
                surface.blit(self.middle, (0, y))
            else:
                surface.blit(self.bottom, (0, y))