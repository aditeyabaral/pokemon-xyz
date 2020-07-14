import random
import pygame
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
 
# Screen dimensions
SCREEN_WIDTH = 955
SCREEN_HEIGHT = 700
background_img = pygame.image.load('map.png')
photo1=pygame.image.load('Syc.png') 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super(Player,self).__init__()
 
        # Set height, width
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
        self.rect.centerx=SCREEN_WIDTH/2
        self.rect.bottom=SCREEN_HEIGHT-2
 
        # Make our top-left corner the passed-in location.
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
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

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(photo1,(90,120))
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.x=387
        self.rect.y=227
        
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Pokemon X, Y and Z')

#Set icons
icon = pygame.image.load('XYZ.png')
pygame.display.set_icon(icon)

# List to hold all the sprites
all_sprites = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprites.add(wall)
mobs=pygame.sprite.Group()
mob=Mob()
all_sprites.add(mob)
mobs.add(mob)
all_sprites.add(mob)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprites.add(wall)
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
wall16= Wall(793,66,90,262)
wall17= Wall(615,220,92,200)
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
 
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprites.add(wall)
wall=Wall(200,200,200,200)
wall_list.add(wall)
all_sprites.add(wall)
 
# Create the player paddle object
player = Player(718,263)
player.walls = wall_list
 
all_sprites.add(player)
 
clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
                player.image=pygame.transform.scale(player.images[3],(60,60))
                player.image.set_colorkey(WHITE)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
                player.image=pygame.transform.scale(player.images[5],(60,60))
                player.image.set_colorkey(WHITE) 
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
                player.image=pygame.transform.scale(player.images[7],(60,60))
                player.image.set_colorkey(WHITE)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
                player.image=pygame.transform.scale(player.images[1],(60,60))
                player.image.set_colorkey(WHITE)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
                player.image=pygame.transform.scale(player.images[3],(60,60))
                player.image=pygame.transform.scale(player.images[2],(60,60))
                player.image.set_colorkey(WHITE)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
                player.image=pygame.transform.scale(player.images[5],(60,60))
                player.image=pygame.transform.scale(player.images[4],(60,60))
                player.image.set_colorkey(WHITE) 
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
                player.image=pygame.transform.scale(player.images[7],(60,60))
                player.image=pygame.transform.scale(player.images[6],(60,60))
                player.image.set_colorkey(WHITE)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
                player.image=pygame.transform.scale(player.images[1],(60,60))
                player.image=pygame.transform.scale(player.images[0],(60,60))
                player.image.set_colorkey(WHITE)
 
    all_sprites.update()
 
    screen.blit(background_img.convert(),[0,0])
 
    all_sprites.draw(screen)
    block_hit_list = pygame.sprite.spritecollide(player,mobs, False)
    if block_hit_list:
        pygame.quit()
        import Starter
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
