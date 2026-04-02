#making a game of space invader using python and pygame
import pygame as p 
import random as r
import math as m 
#constant

Screen_width,Screen_height=1000,800
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=2
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


running=True
while running:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in p.event.get():
        if event.type== p.QUIT:
            running=False
        
        
        
        
        
    p.display.update()
