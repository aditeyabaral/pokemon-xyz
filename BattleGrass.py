
import pygame
import random
WIDTH = 950
HEIGHT = 700
FPS = 15
pygame.font.init()
smallText=pygame.font.Font('freesansbold.ttf',15)
smallText1=pygame.font.Font('freesansbold.ttf',22)
def text_objects(text, font):
    textSurface=font.render(text,True,BLACK)
    return textSurface, textSurface.get_rect()

#colour definitions so that we need not look at internet
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
phealth=136
ehealth=252


# initialize pygame and create window(do not copy this part)
#make sure you have the same data names as i have used
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))




photo1 = pygame.image.load('Yveltal.png')
photo2= pygame.image.load('Chestnaught.png')




pygame.display.set_caption("Pokemon X,Y and Z")
background_img = pygame.image.load('battle_ground.png').convert()
clock = pygame.time.Clock()
#now the actual sprites begin
#i have created a list of sprtes so that we can update everything at once
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super(Wall,self).__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.image.set_colorkey(BLUE)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

def Attack1():
    global ehealth
    global phealth
    ehealth-=20
    phealth-=random.randint(0,40)
def Attack2():
    global ehealth
    global phealth
    ehealth-=50
    phealth-=random.randint(0,40)
def Attack3():
    global ehealth
    global phealth
    ehealth-=60
    phealth-=random.randint(0,40)
def Attack4():
    global ehealth
    global phealth
    ehealth-=30
    phealth-=random.randint(0,40)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(photo2,(200,236))
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH/2
        self.rect.bottom=HEIGHT-2
        self.speedx=0
        self.speedy=0
        self.walls=None

    def update(self):
        self.speedx=0
        self.speedy=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-5
        if keystate[pygame.K_RIGHT]:
            self.speedx=5
        if keystate[pygame.K_DOWN]:
            self.speedy=5
        if keystate[pygame.K_UP]:
            self.speedy=-5
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.top>HEIGHT:
            self.rect.top=HEIGHT
        if self.rect.bottom<0:
            self.rect.bottom=0
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
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(photo1,(200,236))
        self.rect=self.image.get_rect()
        self.rect.x=659
        self.rect.y=254
        #self.speedx=random.randrange(1,8)
        #self.speedy=random.randrange(1,3)




mobs=pygame.sprite.Group()
player=Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
m=Mob()
all_sprites.add(m)
mobs.add(m)


wall_list=pygame.sprite.Group()
wall = Wall(20, 40, 10, 600)
wall1 = Wall(745,7, 203, 333)
wall2 = Wall(20, 40, 10, 600)
wall3 = Wall(20, 40, 10, 600)
wall4 = Wall(20, 40, 10, 600)
wall5 = Wall(20, 40, 10, 600)
wall6 = Wall(20, 40, 10, 600)
wall7 = Wall(20, 40, 10, 600)
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
player.walls=wall_list

health=142

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
    #collision
    collide= pygame.sprite.spritecollide(player,mobs,False)
    block_hit_list = pygame.sprite.spritecollide(player,wall_list, False)
    '''for block in block_hit_list:
        # Reset our position based on the top/bottom of the object.
        if player.speedy > 0:
            player.rect.bottom = player.rect.bottom
        else:
            player.rect.top = block.rect.bottom'''
    if collide:
        health-=10
    if health<0:
        collide= pygame.sprite.spritecollide(player,mobs,True)


    # Draw / render
    screen.blit(background_img,[0,0])
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()



    pygame.draw.rect(screen,GREEN,(0,565,180,105))
    pygame.draw.rect(screen,GREEN,(190,565,180,105))
    pygame.draw.rect(screen,GREEN,(380,565,180,105))
    pygame.draw.rect(screen,GREEN,(570,565,180,105))





    textSurf1, textRect1=text_objects('Bite',smallText)
    textSurf2, textRect2=text_objects('Hammer Arm',smallText)
    textSurf3, textRect3=text_objects('Land Pledge',smallText)
    textSurf4, textRect4=text_objects('Mud Shot',smallText)
    textSurf5, textRect5=text_objects("Player:"+str(phealth)+"/136",smallText1)
    textSurf6, textRect6=text_objects("Enemy:"+str(ehealth)+"/252",smallText1)
    textRect1.center=((0+(180/2)),(565+(105/2)))
    textRect2.center=((190+(180/2)),(565+(105/2)))
    textRect3.center=((380+(180/2)),(565+(105/2)))
    textRect4.center=((570+(180/2)),(565+(105/2)))
    textRect5.center=((760+(180/2)),(565+(105/2)))
    textRect6.center=((760+(180/2)),(600+(105/2)))
    if 180>mouse[0]>0 and 670>mouse[1]>565:
        if click[0]==1:
            Attack1()
    if 370>mouse[0]>190 and 670>mouse[1]>565:
        if click[0]==1:
            Attack2()
    if 560>mouse[0]>380 and 670>mouse[1]>565:
        if click[0]==1:
            Attack3()
    if 750>mouse[0]>570 and 670>mouse[1]>565:
        if click[0]==1:
            Attack4()
    
    screen.blit(textSurf1, textRect1)
    screen.blit(textSurf2, textRect2)
    screen.blit(textSurf3, textRect3)
    screen.blit(textSurf4, textRect4)
    screen.blit(textSurf5, textRect5)
    screen.blit(textSurf6, textRect6)
    if phealth<0:
        import tt1
        pygame.quit()
    if ehealth<0:
        import Win

    pygame.display.update()
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
