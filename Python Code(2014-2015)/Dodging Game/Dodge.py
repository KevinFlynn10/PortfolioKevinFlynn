#Pair Programming Done By Kevin Flynn and Andrew Callahan
#October 2014
from pygame.locals import *
import random
import os, pygame.mixer, pygame.time

#constant strings
GAME_TITLE = "Fun Game"
gameOver = "Game Over"
final = "Final score: "
play = "To Play again press y, to quit press q."
bounds = "Out of bounds"
qPressed = "The 'q' key is pressed."
currentscore = "Your current score is "
fun = "Hold down s for fun!"

#window size
DISPLAY_SIZE = (600,600)
screen_width = 600
screen_height = 600
DESIRED_FPS = 30
pygame.init()

def funColors(currentcolor): #function to change colors ingame
    currentcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return currentcolor
def playAgain(score): #function to replay game
    pygame.quit() #ends current game
    print gameOver
    print final,score
    print play
    while True: #so player has to input something
        choice = raw_input("> ")
        if choice == 'y': #checks if player wants to play again
            pygame.init()
            main() #reruns game
            break
        elif choice == 'q':
            exit()#quits game
            break
def Score(score): #function to keep track of players score
    score += 1
    return score
def checkBounds(box_x,box_y,score, box_width, box_height): #function to continuously check if player is in bounds. Restarts if false
    if box_x > screen_width - box_width or box_x < 0:
        print bounds
        playAgain(score)
    if box_y > screen_height - 50 - box_height or box_y < screen_height/2:
        print bounds
        playAgain(score)
def currentScore(screen,score): #renders score onto the screen
    font = pygame.font.Font(None, 36)
    text = font.render(currentscore+str(score), 1, (10, 10, 10))
    screen.blit(text,[5,30])
def main():
    #sets constant colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    #creates display screen
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption(GAME_TITLE)
    
    fps_clock = pygame.time.Clock()
    game_running = True
    
    box_x = screen_width/2
    box_y = screen_height - 75
    box_width = 15
    box_height = 15
    
    enemy_width = 20
    enemy_height = 20
    
    score = 0
    count = 0
    
    currentcolor = WHITE
    screen.fill(currentcolor)
    run = True
    enemyxlist = []
    enemyylist = []
    speedlist = []
    enemybox = [] 
    #allows player movement
    while game_running:
        user_input = pygame.event.get()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_q]:
			print qPressed
        if pressed_keys[K_q]:
            game_running = False
        if pressed_keys[K_UP]:
            box_y -= 10
        if pressed_keys[K_DOWN]:
            box_y += 10
        if pressed_keys[K_LEFT]:
            box_x -= 10
        if pressed_keys[K_RIGHT]:
            box_x += 10
        
        if pressed_keys[K_s]:
            count += 1
            if count == 10:
                currentcolor = funColors(currentcolor)
                count = 0
        #draws screen with enemies and players
        screen.fill(currentcolor)
        font = pygame.font.Font(None, 36)
        text = font.render(fun, 1, (10, 10, 10))
        screen.blit(text,[5,50])
        
        currentScore(screen,score)
        
        pygame.draw.rect(screen,GREEN,[0,screen_height/2,screen_width,screen_height/2 -50],5)
        pygame.draw.rect(screen,RED,[box_x,box_y,box_width,box_height],0)
        player_box = Rect(box_x, box_y, box_width, box_height)
        #initials enemies and individual properties
        if run == True:
            for i in range(25):
                rando = random.randint(0,screen_width - enemy_width)
                rands = random.randint(-250,0)
                speeds = random.randint(2,12)
                speedlist.append(speeds)
                enemyxlist.append(rando)
                enemyylist.append(rands)
                enemybox.append(Rect(0,0,0,0))
            run = False
        #draws enemies moving and checks for collisions
        for x in range(25):
            pygame.draw.rect(screen,BLACK,[enemyxlist[x],enemyylist[x],enemy_width,enemy_height],0)
            
            enemyylist[x] += speedlist[x]
            
            enemybox[x] = (Rect(enemyxlist[x], enemyylist[x], enemy_width, enemy_height))
            if enemyylist[x] >= screen_height:
                enemyxlist[x] = random.randint(0,screen_width - enemy_width)
                enemyylist[x] = random.randint(-250,0)
            if enemybox[x].colliderect(player_box):
                game_running = False
        #outputs score to user as well as making sure player is in bounds
        score = Score(score)
        checkBounds(box_x,box_y,score,box_width,box_height)
        pygame.display.flip() 

		
        fps_clock.tick(DESIRED_FPS)
    playAgain(score)
    
main()
