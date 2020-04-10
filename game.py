#Title: Rescue the Princess Sansa

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1440
screen_height = 780
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("Sir_Roland.png")
princess = pygame.image.load("Princess.png")

enemy1 = pygame.image.load("Zombie.png")
enemy1 = pygame.transform.scale(enemy1,(50,80))

enemy2 = pygame.image.load("Dracula.png")
enemy2 = pygame.transform.scale(enemy2,(50,80))

enemy3 = pygame.image.load("ogre.png")
enemy3 = pygame.transform.scale(enemy3,(50,80))

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

player_height = player.get_height()
player_width = player.get_width()
princess_height = princess.get_height()
princess_width = princess.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

# Store the positions of the player, princess and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

princessXPosition = 1350
princessYPosition = random.randint(0,screen_height - princess_height)

# Make the enemy start off screen and at a random y position.

enemyXPosition1 =  screen_width
enemyYPosition1 =  random.randint(50,200)

enemyXPosition2 =  screen_width
enemyYPosition2 =  random.randint(300,400)

enemyXPosition3 =  screen_width
enemyYPosition3 =  random.randint(550,700)

# This checks if the up or down key is pressed.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

running = True

while running is True: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 
    pygame.time.delay(20)
    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(princess, (princessXPosition, princessYPosition))
    screen.blit(enemy1, (enemyXPosition1, enemyYPosition1))
    screen.blit(enemy2, (enemyXPosition2, enemyYPosition2))
    screen.blit(enemy3, (enemyXPosition3, enemyYPosition3))
    
    pygame.display.flip()   # This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 5
    if keyDown == True:
        if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 5
    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerXPosition -= 5
    if keyRight == True:
        if playerXPosition < screen_width - player_width:# This makes sure that the user does not move the player below the window.
            playerXPosition += 5
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox1 = pygame.Rect(enemy1.get_rect())
    enemyBox1.top = enemyYPosition1
    enemyBox1.left = enemyXPosition1
    
    enemyBox2 = pygame.Rect(enemy2.get_rect())
    enemyBox2.top = enemyYPosition2
    enemyBox2.left = enemyXPosition2
    
    enemyBox3 = pygame.Rect(enemy3.get_rect())
    enemyBox3.top = enemyYPosition3
    enemyBox3.left = enemyXPosition3
    
    
    # Test collision of the boxes:

    if playerBox.colliderect(enemyBox1) or playerBox.colliderect(enemyBox2) or playerBox.colliderect(enemyBox3):
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quit game and exit window: 
        running = False
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:

    if (playerXPosition + player_width >= princessXPosition) and (playerYPosition <= princessYPosition + princess_height) and (playerYPosition + player_height > princessYPosition):
        
        print("You win!")
        
        # Quit game and exit window: 
        running = False
        pygame.quit()        
        exit(0)   
 
    
# Make enemy approach the player.
    isUp1 = random.randint(1,2)
    isUp2 = random.randint(1,2)
    isUp3 = random.randint(1,2)
    isLeft1 = random.randint(1,2)
    isLeft2 = random.randint(1,2)
    isLeft3 = random.randint(1,2)
    
    enemyXPosition1 -= random.randint(1,4)
    if isLeft1 == 1:
        enemyXPosition1 -= random.randint(3,6)
        if enemyXPosition1 < 0:
            enemyXPosition1 = 1400
    else:
        enemyXPosition1 += random.randint(3,6)
        if enemyXPosition1 > 1400:
            enemyXPosition1 -= 7

    enemyXPosition2 -= random.randint(1,4)
    if isLeft2 == 1:
        enemyXPosition2 -= random.randint(3,6)
        if enemyXPosition2 < 0:
            enemyXPosition2 = 1400
    else:
        enemyXPosition2 += random.randint(3,6)
        if enemyXPosition2 > 1400:
            enemyXPosition2 -= 7

    enemyXPosition3 -= random.randint(1,4)
    if isLeft3 == 1:
        enemyXPosition3 -= random.randint(3,6)
        if enemyXPosition3 < 0:
            enemyXPosition3 = 1400
    else:
        enemyXPosition3 += random.randint(3,6)
        if enemyXPosition3 > 1400:
            enemyXPosition3 -= 7

# Make enemy approach the player.
    
    if isUp1 == 1:
        enemyYPosition1 -= random.randint(3,6)
        if enemyYPosition1 < 0:
            enemyYPosition1 += 7
    else:
        enemyYPosition1 += random.randint(3,6)
        if enemyYPosition1 > 700:
            enemyYPosition1 -= 7

    enemyXPosition2 -= random.randint(1,4)
    
    if isUp1 == 1:
        enemyYPosition2 -= random.randint(3,6)
        if enemyYPosition2 < 0:
            enemyYPosition2 += 7
    else:
        enemyYPosition2 += random.randint(3,6)
        if enemyYPosition2 > 700:
            enemyYPosition2 -= 7
    enemyXPosition3 -= random.randint(1,4)
    
    if isUp1 == 1:
        enemyYPosition3 -= random.randint(3,6)
        if enemyYPosition3 < 0:
            enemyYPosition3 += 7
    else:
        enemyYPosition3 += random.randint(3,6)
        if enemyYPosition3 > 700:
            enemyYPosition3 -= 7
    
    # ================The game loop logic ends here. =============
