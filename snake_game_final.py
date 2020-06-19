import pygame
import random
import time
import os.path

screen_width = 500
screen_height= 500

running =False
exit_game=False

black=0,0,0
white=255,255,255
red=255,0,0
green=0,255,0

block_size=10

apple_x = 40
apple_y = 40

snake_x= 100
snake_y= 100

FPS=10

x_left=x_right=y_up=y_down=0

block_size=10

event_gameover=True

pygame.init()

clock=pygame.time.Clock()

screen= pygame.display.set_mode((screen_width, screen_height))

img=pygame.image.load("snakehead5.png")     # Creating an image object
img_apple=pygame.image.load("apple1.0.png")     # Creating an image object

pygame.display.set_caption("snake game")


def message_to_screen(msg,color,font_size,x_msg,y_msg):
    font=pygame.font.SysFont("comicsansms",font_size)
    screen_text = font.render(msg,True, color)
    screen.blit(screen_text, [x_msg,y_msg])

    
def Game_over():
    screen.fill(black)
    message_to_screen("GAME OVER",red,60,90,170)
    message_to_screen("Press r to retry, q to quit",green,30,80,250) 
    pygame.display.update()
    event_gameover=True
    while event_gameover==True:
        for event_gor in pygame.event.get():
            if event_gor.type==pygame.KEYDOWN:
                if event_gor.key==pygame.K_q:
                    event_gameover=False
                    pygame.quit()
                    quit()
                if event_gor.key==pygame.K_r:
                    event_gameover=False
                    exit_game=False
                    #snake_x= 100
                    #snake_y= 100
                    #running=True

def snake(block_size,snakelist):
    screen.blit(img, (snakelist[-1][0],snakelist[-1][1]) )
    for xny in snakelist[:-1]:
        pygame.draw.rect(screen,red,[xny[0],xny[1],block_size,block_size])


def score(score):
    text_score=pygame.font.SysFont("comicsansms",25)
    screen_score = text_score.render("Score:"+str(score),True, red)
    screen.blit(screen_score, [0,0])
    

while exit_game==False:
    snake_x= 100
    snake_y= 100

    snakelist=[]
    snakelength=1
    
    # The intro message block
    screen.fill(white)
    message_to_screen("WELCOME TO SNAKE GAME",black,30,20,110)
    message_to_screen("The objective of thegame is to eat red appples",red,20,10,160)
    message_to_screen("The more apples you eat,the longer you get    ",red,20,10,190)
    message_to_screen("If you run into yourself, or the wall you die!",red,20,10,220)
    message_to_screen("At any time press q to quit",red,20,10,250)
    message_to_screen("Press s to start, q to quit",green,30,30,280)
    print("hai")
    for event_msg in pygame.event.get():
        print("hello")
        if event_msg.type==pygame.KEYDOWN:
            if event_msg.key==pygame.K_s:
                running=True
                exit_game=False
                print("s")
            if event_msg.key==pygame.K_q:
                running=False
                exit_game=True
                print("q")
    while running:
        print("running")
        screen.fill(black)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                exit_game=True
            elif event.type == pygame.KEYDOWN:     #To check wether the user pressed a key
                x_left=x_right=y_up=y_down=0
                if event.key == pygame.K_q:
                    running=False
                if event.key == pygame.K_r:
                    game_exit=True
                if event.key == pygame.K_LEFT: 
                    x_left=1
                elif event.key == pygame.K_RIGHT:
                    x_right=2
                elif event.key == pygame.K_UP:
                    y_up=3
                elif event.key == pygame.K_DOWN:
                    y_down=4

                        

        # To continue the movement after the key is released
        if x_left==1:
                    snake_x=snake_x-10
        elif x_right==2:
                    snake_x=snake_x+10
        elif y_up==3:
                    snake_y=snake_y-10
        elif y_down==4:
                    snake_y=snake_y+10
                
        #screen.fill(black)     # without this the program will draw all the path of the rectangle

        if snake_x>=screen_width-10:
                    snake_x=screen_width-10
                    running=False
                    Game_over()
        if snake_x<0:
                    snake_x=0
                    running=False
                    Game_over()
        if snake_y>=screen_height-10:
                    snake_y=screen_height-10
                    running=False
                    Game_over()
        if snake_y<0:
                    y_lead=0
                    running=False
                    Game_over()
                
        pygame.draw.rect(screen,red,[snake_x,snake_y,block_size,block_size])

        if snake_x==apple_x and snake_y==apple_y:
            apple_x= round(random.randrange(10, screen_width-20)/10.0)*10.0
            apple_y= round(random.randrange(10,screen_height-20)/10.0)*10.0
            snakelength+=1
        #pygame.draw.rect(screen,white,[apple_x,apple_y,block_size,block_size])
        screen.blit(img_apple, (apple_x,apple_y) )
#--------------------------------
        # a list which contains the location of the box in the previous movements
        snakehead=[]
        snakehead.append(snake_x)
        snakehead.append(snake_y)

        if len(snakelist) > snakelength: # To delete the latest head position whw
                   del snakelist[0]
        # To check for a collision, if the list contains the new position of the head then it is a collision
        for eachsegment in snakelist[:-1]:  
            if eachsegment == snakehead:
                running=False
                Game_over()
        snakelist.append(snakehead)
        snake(block_size,snakelist) # to draw snake
#--------------------------------
        score(snakelength-1)
        pygame.display.update()
            
        
        clock.tick(FPS)           
    pygame.display.update()
pygame.quit()

