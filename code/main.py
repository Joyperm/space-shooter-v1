import pygame
from os.path import join

from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter :)")
running = True

# plain surface
w, h = 100, 200
surf = pygame.Surface((w,h))
surf.fill("blue")
x = 100

# import image
# path = join('images','player.png') This method avoid having issue with / or \ in os system. Relative path is ok but using 'join' is better
player_surface = pygame.image.load(join('images','player.png')).convert_alpha() #use .convert/convert_alpha for better performance (> frame rate)
# load star.png and place 20 of them randomly
star_surf = pygame.image.load(join("images","star.png")).convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #trigger x button on surface/window
            running = False

    # draw the game (order matters!!: here we want ship over star)
    # fill window with red color
    display_surface.fill('darkgrey')
    x += 0.1

    # disply star
    for pos in star_position:
        display_surface.blit(star_surf, pos)  

    # show ship (line 13) at this position (x,y)
    display_surface.blit(player_surface, (x,150))
    
    pygame.display.update()

# IMPORTANT!! Close game after init in line 4
pygame.quit()