#imports

import pygame,os,sys,random,math
pygame.font.init()
pygame.mixer.init()
from pygame import mixer
from pygame.locals import *


#Window properties

pygame.font.init()
pygame.mixer.init()
width,height=1280,720
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Duck Hunt")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)
bg=pygame.image.load("bg.png")
menu=pygame.image.load("menu.png")
creds=pygame.image.load("creds.png")
pause=pygame.image.load("pause.png")
background=menu
mixer.music.load("Megalovania.wav")
mixer.music.set_volume(0.08)
mixer.music.play(-1)


#Colours

sky_blue=(0,255,255)
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)

#duck (mid x=68,y=45)

duck_y=514
duck_x=random.randint(50,1080)
duck=pygame.image.load("Flying duck.png")
duck_velx=20
duck_vely=-8

#movement

def duckmovement(x,y):
    window.blit(duck,(duck_x,duck_y))
    
#collision

def duckboom(mx,my,x,y):
    distance=math.sqrt((math.pow((mx-x),2)) +math.pow((my-y),2))
    if distance<50:
        return True
    else:
        return False
    
def collisionrect():
    global duck_x,duck_y
    duck_rect=pygame.draw.rect(window, pygame.Color(0, 255, 0, 0),[duck_x,duck_y,150,70])
    centrex=duck_x+75
    centrey=duck_y+35
    return centrex,centrey 

def gameovert():

    gameovertext=gameoverfont.render("GAME OVER(Enter to replay)",True,(255,255,255))
    window.blit(gameovertext,(250,250))
def score_display():
    score=scoretext.render('Score:'+str(score_value),True,(255,255,255))
    window.blit(score,(20,640))
     

   
#Game variables

running=True
FPS=60
score_value=0
mouseclicky=100000
mouseclickx=100000
gameover=False

#Clock
  
clock=pygame.time.Clock()

#Text
gameoverfont=pygame.font.Font("ARCADE_I.ttf",36)
scoretext=pygame.font.Font("ARCADE_I.ttf",48)



#Main game loop

while running:
    mouseclicky=100000
    mouseclickx=100000
    window.fill(white)
    window.blit(background,(0,0))

    mousex, mousey = pygame.mouse.get_pos()
    
    #FPS
    clock.tick(FPS)
    #Event Loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                if background==menu:
                    running=False
                    continue
                else:
                    background=menu
                    window.blit(background,(0,0))
                    continue    
            if event.key==pygame.K_LCTRL or event.key==pygame.K_RCTRL :
                if background==menu:
                    background=creds
                    window.blit(background,(0,0))
                elif background==bg:
                    background=pause
                    window.blit(background,(0,0))
                    
                                        
            if event.key==pygame.K_RETURN:
                background=bg
                window.blit(background,(0,0))
                
                
        #mouse interfacing
        
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                Shotgun=mixer.Sound('shotgun.wav')
                Shotgun.set_volume(0.02)
                Shotgun.play()
                mouseclickx,mouseclicky=mousex,mousey
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                pass
    
    #Game 
    
    if background==bg:
        
        duck_x=duck_x+duck_velx
        duck_y=duck_y+duck_vely
        if duck_y>=570 and duck_y<=900:
            duck_vely=0
            duck_velx=0
            duck_y=3000
            duck_x=4000
            gameover=True
            
        if duck_x>=1100 :
            duck_velx=-duck_velx
            duck=pygame.transform.flip(duck, True, False)
        if duck_x<=-100:
            duck_velx=-duck_velx
            duck=pygame.transform.flip(duck, True, False)
        if duck_y<=-50:
            duck_vely=-duck_vely
        #Collision
        
        centre=collisionrect()
        window.blit(background,(0,0))
        score_display()
        collision=duckboom(mouseclickx,mouseclicky,centre[0],centre[1])
        if collision:
            dead=mixer.Sound('dead.wav')
            dead.set_volume(0.02)
            dead.play()
            score_value+=1
            duck_x=random.randint(50,1080)
            duck_y=514
            duck=pygame.image.load("Flying duck.png")
            duck_velx=20
            duck_vely=-8
        duckmovement(duck_x,duck_y)
    
    #gameover screen
    
    if gameover==True: 
        
        gameovert()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                    background=bg
                    window.blit(background,(0,0))
                    gameover=False
                    duck_x=random.randint(50,1080)
                    duck_y=514
                    duck=pygame.image.load("Flying duck.png")
                    duck_velx=20
                    duck_vely=-8
                    score_value=0
            if event.key==pygame.K_ESCAPE:
                running=False
                    
                
            

    
    #Update the screen
    
    pygame.display.update() 
        
                    
            
            

        
    

