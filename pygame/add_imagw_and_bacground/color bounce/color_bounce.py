#color bounce game
import pygame as p
import random
p.init()
#making two variables
rect_color_change=p.USEREVENT+1
backg_color_change=p.USEREVENT+2
#colors of sprite
blue=p.Color("blue")
red=p.Color("red")
random_1=p.Color(12,58,67)
#setting up the screen color
black=p.Color("black")
pink=p.Color("pink")
orange=p.Color("orange")
random_2=p.Color(45,67,12)

class sprite(p.sprite.Sprite):
    
     def __init__(self,color,height,width):
         super().__init__()
         self.image=p.Surface((width,height))
         self.image.fill(color)
         self.rect=self.image.get_rect()
         self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
     def update(self):
         self.rect.move_ip(self.velocity) 
         boundary_hit=False
         if self.rect.left<=0 or self.rect.right>=500:
             self.velocity[0]=-self.velocity[0]
             bundary_hit=True
         if self.rect.top<=0 or self.rect.bottom>=400:
             self.velocity[1]=-self.velocity[1]
             boundary_hit=True
        #post event to change the color
         if boundary_hit:
             p.event.post(p.event.Event(rect_color_change))
             p.event.post(p.event.Event(backg_color_change))
         #def change color
     def change_color(self):
         self.image.fill(random.choice([blue,red,random_1]))      
def change_background_color():
    global backg_color
    bg_color=random.choice9([black,pink,orange,random_2])
#creating a group to hold the sprites
all_sprites=p.sprite.Group()
sp1=sprite(red,20,30)
sp1.rect.x=random.randint(1,480)
sp1.rect.y=random.randint(1,380)
all_sprites.add(sp1)

screen=p.display.set_mode((500,400))
p.display.set_caption("Color Bounce Game")
bg_color=black
screen.fill(bg_color)
exit=False
clock=p.time.Clock()
while not exit:
    for event in p.event.get():
        if event.type==p.QUIT:
            exit=True
        elif event.type==rect_color_change:
            sp1.change_color()
        elif event.type==backg_color_change:
            change_background_color()
    #update All sprites
    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)
    p.display.flip()
    clock.tick(250)
p.quit()