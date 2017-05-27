import pygame

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)

#initialize pygame
pygame.init()

#set the height and width of the screen
width = 800
height = 480

mainScreen = pygame.display.set_mode([width,height])

#A list of all of the sprites in the game
all_sprites_list = pygame.sprite.Group()


def sprite_sheet_load(colorKey, spriteLocX, spriteLocY, spriteSizeX, spriteSizeY, fileName):
    '''Purpose: to extract a sprite from a sprite sheet at the chosen location'''
    '''credit to SO user hammyThePig for original code'''

    sheet = pygame.image.load(fileName).convert() #loads up the sprite sheet. convert makes sure the pixel format is coherent
    sheet.set_colorkey(colorKey) #sets the color key

    sprite = sheet.subsurface(pygame.Rect(spriteLocX, spriteLocY, spriteSizeX, spriteSizeY)) #grabs the sprite at this location

    return sprite

class newPlayer(pygame.sprite.Sprite):
    '''class that builds up the player'''
     #constructor function
    def __init__(self): #create a self variable to do stuff

        #call up the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        img = "download.jpg"

        #size of each sprite
        sprite_sizeX = 35
        sprite_sizeY = 37

        #List of images for different types of movement
        self.imagesLeft = []

        self.imagesRight = []

        self.imagesUp = []

        self.imagesDown = []

        #these two variables go and help reset the position variables of the sprites
        xInit = 35
        yInit = 37

        #inital positions of sprites on the sheet
        positionX = 0
        positionY = 0

        colorKey = white #colorKey to pass to the function

        self.imagesUp.append(sprite_sheet_load(black, positionX, positionY, sprite_sizeX, sprite_sizeY, img))


        #the best image to use by default is the one that has the player facing the screen.
        self.image=self.imagesUp[0]


        self.rect = self.image.get_rect()

newplayer = newPlayer()
all_sprites_list.add(newplayer)
newplayer.rect.x = 300
newplayer.rect.y = 300

#a conditional for the loop that keeps the game running until the user Xes out
done = False

#clock for the screen updates
clock = pygame.time.Clock()


while done==False:
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT: #if the user hit the close button
                done=True

    mainScreen.fill(white)#makes the background white, and thus, the white part of the images will be invisible

    #draw the sprites
    all_sprites_list.draw(mainScreen)

    #limit the game to 20 fps
    clock.tick(20)

    #update the screen on the regular
    pygame.display.flip()

pygame.quit()