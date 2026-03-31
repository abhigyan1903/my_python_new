import pygame as p 
import random
p.init()
screen_height,screen_width=400,500
speed=5
font_size=72
bg_image=p.transform.scale(p.image.load("yes.jpg"),(screen_width,screen_height))
font=p.font.SysFont("Arial",font_size)

class sprite(p.sprite.Sprite):
    def __init__ (self,color,height,width):
        super().__init__()
        self.image=p.Surface((width,height))
        self.image.fill (p.Color("lightblue"))
        p.draw.rect(self.image,color,p.Rect(0,0,width,height)) 
        self.rect=self.image.get_rect()
    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change,screen_width-self.rect.width),0) 
        self.rect.y=max(min(self.rect.y+y_change,screen_height-self.rect.height),0)
screen=p.display.set_mode((screen_width,screen_height))
p.display.set_caption("Sprite Collision")
all_sprite=p.sprite.Group()
sprite1=sprite(p.Color("red"),40,80)
sprite1.rect.x=random.randint(0,screen_width-sprite1.rect.width)
sprite1.rect.y=random.randint(0,screen_height-sprite1.rect.height)
all_sprite.add(sprite1)
sprite2=sprite(p.Color("blue"),50,40) 
sprite2.rect.x=random.randint(0,screen_width-sprite2.rect.width)
sprite2.rect.y=random.randint(0,screen_height-sprite2.rect.height)
all_sprite.add(sprite2)
running=True
won=False
clock=p.time.Clock()
while running:
    for event in p.event.get():
        if event.type==p.QUIT:
            running=False
    if not won:                      
        keys=p.key.get_pressed()
        x_change=(keys[p.K_RIGHT]-keys[p.K_LEFT])*speed
        y_change=(keys[p.K_DOWN]-keys[p.K_UP])*speed
        sprite1.move(x_change,y_change)
        
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprite.remove(sprite2)
            won=True
    screen.blit(bg_image,(0,0))
    all_sprite.draw(screen)
    if won:                         
        win_text=font.render("You Win!!!",True,p.Color("yellow"))
        screen.blit(win_text,((screen_width-win_text.get_width())//2,(screen_height-win_text.get_height())//2))
    p.display.flip()
    clock.tick(90)
p.quit()    