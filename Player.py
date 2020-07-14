import pygame
import random

WIDTH = 955
HEIGHT = 700
FPS = 40

#colour definitions so that we need not look at internet
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window(do not copy this part)
#make sure you have the same data names as i have used
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Whatte Player!!!")
clock = pygame.time.Clock()
background_img = pygame.image.load('map.png').convert()
#player_img = pygame.image.load("P ().bmp").convert()

#now the actual sprites begin
#i have created a list of sprites so that we can update everything at once
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super(Wall,self).__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        #self.image.fill(BLUE)
        self.image.set_colorkey(BLACK)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #pygame.Surface((40,50))
        #self.image.fill(GREEN)
       
        self.images = []
        self.images.append(pygame.image.load('P(1).png'))
        self.images.append(pygame.image.load('P(2).png'))
        self.images.append(pygame.image.load('P(3).png'))
        self.images.append(pygame.image.load('P(4).png'))
        self.images.append(pygame.image.load('P(5).png'))
        self.images.append(pygame.image.load('P(6).png'))
        self.images.append(pygame.image.load('P(7).png'))
        self.images.append(pygame.image.load('P(8).png'))
        self.image=pygame.transform.scale(self.images[0],(60,60))
        self.rect=self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-2
        self.speedx=0
        self.speedy=0
    def update(self):
        self.image=pygame.transform.scale(self.images[0],(60,60))
        self.image.set_colorkey(WHITE)
        self.speedx=0
        self.speedy=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-2
            self.image=pygame.transform.scale(self.images[3],(60,60))
            self.image.set_colorkey(WHITE)
        if keystate[pygame.K_RIGHT]:
            self.speedx=2
            self.image=pygame.transform.scale(self.images[5],(60,60))
            self.image.set_colorkey(WHITE) 
        if keystate[pygame.K_DOWN]:
            self.speedy=1
            self.image=pygame.transform.scale(self.images[1],(60,60))
            for i in range(0,10000,1):
                pass
            self.image=pygame.transform.scale(self.images[1],(60,60))
            self.image.set_colorkey(WHITE)
        if keystate[pygame.K_UP]:
            self.speedy=-1
            self.image=pygame.transform.scale(self.images[7],(60,60))
            self.image.set_colorkey(WHITE)
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0
        '''if self.rect.>HEIGHT:
            self.rect.up=HEIGHT
        if self.rect.down<0:
            self.rect.down=0'''
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.speedx > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.speedy
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.speedy> 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

player=Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
wall_list=pygame.sprite.Group()
wall = Wall(20, 40, 10, 600)
wall1 = Wall(512, 480,62,31)
wall2 = Wall(321, 478, 61, 31)
wall3 = Wall(20, 40, 10, 600)
wall4 = Wall(20, 40, 10, 600)
wall5 = Wall(20, 40, 10, 600)
wall6 = Wall(20, 40, 10, 600)
wall7 = Wall(20, 40, 10, 600)
wall7 = Wall(955,700, 26, 44)
wall8 = Wall(512,506,26,39)
wall9 = Wall(352, 503, 25,38)
wall10 = Wall(90, 70, 153,352)
wall11 = Wall(304, 70, 120,359)
wall12= Wall(247,67, 49,182)
wall13= Wall(512,67, 344,147)
wall14= Wall(414,67, 66,151)
wall15= Wall(485,67,33,342)
wall16= Wall(778,66,117,358)
wall17= Wall(615,220,103,187)
wall18 = Wall(26, 246, 68,2)
wall19 = Wall(513,212,54,193)
wall20 = Wall(891,414,3,127)
wall21 = Wall(23,246,6,454)
all_sprites.add(wall)
wall_list.add(wall)
all_sprites.add(wall1)
wall_list.add(wall1)
all_sprites.add(wall2)
wall_list.add(wall2)
all_sprites.add(wall3)
wall_list.add(wall3)
all_sprites.add(wall4)
wall_list.add(wall4)
all_sprites.add(wall5)
wall_list.add(wall5)
all_sprites.add(wall6)
wall_list.add(wall6)
all_sprites.add(wall7)
wall_list.add(wall7)
all_sprites.add(wall8)
wall_list.add(wall8)
all_sprites.add(wall9)
wall_list.add(wall9)
all_sprites.add(wall10)
wall_list.add(wall10)
all_sprites.add(wall11)
wall_list.add(wall11)
all_sprites.add(wall12)
wall_list.add(wall12)
all_sprites.add(wall13)
wall_list.add(wall13)
all_sprites.add(wall14)
wall_list.add(wall14)
all_sprites.add(wall15)
wall_list.add(wall15)
all_sprites.add(wall16)
wall_list.add(wall16)
all_sprites.add(wall17)
wall_list.add(wall17)
all_sprites.add(wall18)
wall_list.add(wall18)
all_sprites.add(wall19)
wall_list.add(wall19)
all_sprites.add(wall20)
wall_list.add(wall20)
all_sprites.add(wall21)
wall_list.add(wall21)
player.walls=wall_list
# Game loop
running = True
while running:
    # keep loop running at the right speed
    
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.blit(background_img,[0,0])
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
