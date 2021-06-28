import pygame
import time

SCREENRECT = pygame.Rect(0, 0, 640, 480)

# Initialize pygame
if pygame.get_sdl_version()[0] == 2:
    pygame.mixer.pre_init(44100, 32, 2, 1024)
pygame.init()
if pygame.mixer and not pygame.mixer.get_init():
    print("Warning, no sound")
    pygame.mixer = None

# Set the display mode
fullscreen = False
winstyle = 0  # |FULLSCREEN
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

# decorate the game window
# icon = pygame.transform.scale(Alien.images[0], (32, 32))
# pygame.display.set_icon(icon)
pygame.display.set_caption("Pygame Flappy-Bird")
pygame.mouse.set_visible(0)

# create the background, tile the bgd image
background = pygame.Surface(SCREENRECT.size)
screen.blit(background, (0, 0))
pygame.display.flip()

# Create Some Starting Values
clock = pygame.time.Clock()
running = True

# Run our main loop whilst the player is alive.
while running: # player.alive():

    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            break
    
    keystate = pygame.key.get_pressed()

    # game logic

    # updating
    pygame.display.update()

    # cap the framerate at 60fps. Also called 60HZ or 60 times per second.
    clock.tick(60)

pygame.quit()