#making a game of space invader using python and pygame
import pygame as p 
import random as r
import math as m 

#constant

Screen_width,Screen_height=800,500
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27
#initialization
p.init()
screen=p.display.set_mode((Screen_width,Screen_height))
bg=p.image.load("space.jpg")
p.display.set_caption("Space Invader")
icon=p.image.load("player.png")
p.display.set_icon(icon)

#player
player_img=p.image.load("player.png")
playerx=player_start_x
playery=player_start_y
playerx_change=0

#enemy
enemy_image=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemy_image.append(p.image.load("enemy.png"))
    enemyx.append(r.randint(0,Screen_width-64))
    enemyy.append(r.randint(enemy_start_y_min,enemy_start_y_max))
    enemyx_change.append(enemy_speed_x)
    enemyy_change.append(enemy_speed_y)
    
#bullet
bullet_img=p.image.load("bullet.png")
bulletx=0
bullety=player_start_y
bulletx_change=0
bullety_change=bullet_speed_y
bullet_state="ready"

# lets add the score
score_value=0
font=p.font.Font(None,32)
text_x=10
text_y=10
over_font=p.font.Font(None,64)
def show_score(x,y):
  #displaying the score
  score=font.render("score: " + str(score_value),True,(255,255,255) )
  screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player( x,y):
    screen.blit(player_img,(x,y))
def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(x+16,y+10))
def collision(enemyx,enemyy,bulletx,bullety):
    distance=m.sqrt((enemyx-bulletx)**2 + (enemyy-bullety)**2)
    return distance < collision_distance
         
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in p.event.get():
        if event.type== p.QUIT:
            running=False
        if event.type==p.KEYDOWN:
            if event.key==p.K_LEFT:
                playerx_change=-5
            if event.key==p.K_RIGHT:
                playerx_change=5
            if event.key==p.K_SPACE and bullet_state=="ready":
                bulletx=playerx
                fire_bullet(bulletx,bullety)
        if event.type==p.KEYUP and (event.key in [p.K_LEFT,p.K_RIGHT]):
            playerx_change=0
    playerx+=playerx_change 
    playerx=max(0,min(playerx,Screen_width-64))
    
    for i in range(num_of_enemies):
        if enemyy[i]>340:
            for j in range(num_of_enemies):
                enemyy[j]=2000
            game_over_text()
            break
        
        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0 or enemyx[i]>=Screen_width-64:
            enemyx_change[i]*=-1
            enemyy[i]+=enemyy_change[i]
        
        if collision(enemyx[i],enemyy[i],bulletx,bullety):
              bullety=player_start_y
              bullet_state="ready"
              score_value+=1
              enemyx[i]=r.randint(0,Screen_width-64)
              enemyy[i]=r.randint(enemy_start_y_min,enemy_start_y_max)
        
        enemy(enemyx[i],enemyy[i],i)
        
    if bullety<=0:
        bullety=player_start_y
        bullet_state="ready"  
    elif bullet_state=="fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
        
        
    player(playerx,playery)
    show_score(text_x,text_y) 
    p.display.update()   
            
            
        
        
        
        

