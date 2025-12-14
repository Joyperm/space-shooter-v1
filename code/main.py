import pygame
from os.path import join

from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space shooter :)")
running = True
clock = pygame.time.Clock()

# plain surface
w, h = 100, 200
surf = pygame.Surface((w,h))
surf.fill("blue")
player_x = 100

# import image
# path = join('images','player.png') This method avoid having issue with / or \ in os system. Relative path is ok but using 'join' is better
player_surface = pygame.image.load(join('images','player.png')).convert_alpha() #use .convert/convert_alpha for better performance (> frame rate)
# place the player at the center using float value (frect) for easier position anywhere
player_rect = player_surface.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
player_direction = pygame.math.Vector2(1, 1) #x,y
player_speed = 300


# load star.png and place 20 of them randomly
star_surf = pygame.image.load(join("images","star.png")).convert_alpha()
# star_position = [(randint(0, WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20)] #short hand
star_position = []
for i in range(20):
    x = randint(0,WINDOW_WIDTH)
    y = randint(0,WINDOW_HEIGHT)
    star_position.append((x,y))

meteor_surf = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(join("images","laser.png")).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

while running:
    # control frame rate
    dt = clock.tick() / 1000 #convert to second
    # print(clock.get_fps() )
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #trigger x button on surface/window
            running = False

    # draw the game (order matters!!: here we want ship over star)
    # fill window with red color
    display_surface.fill('darkgrey')    

    # disply star
    for pos in star_position:
        display_surface.blit(star_surf, pos) 
    
    # disply meteor
    display_surface.blit(meteor_surf, meteor_rect)

    #display laser
    display_surface.blit(laser_surf, laser_rect)

    # player movement
    if player_rect.bottom > WINDOW_HEIGHT or player_rect.top < 0:
        player_direction.y *= -1
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction.x *= -1
    # Added vector to tuple position
    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surface, player_rect.topleft)    

    pygame.display.update()

# IMPORTANT!! Close game after init in line 4
pygame.quit()