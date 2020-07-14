import pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,400))
background_img = pygame.image.load('winn.png').convert()

running = True
while running:
    # keep loop running at the right speed
    clock.tick(30)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_img,[0,0])
    pygame.display.update()
    #all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
