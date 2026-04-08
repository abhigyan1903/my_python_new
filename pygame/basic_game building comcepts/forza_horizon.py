#making a forza horizon game screen
#lets add sprites
#in itializing
import pygame as p      
p.init()
Screen_width,Screen_height=500,500
display_1=p.display.set_mode((Screen_width,Screen_height))
p.display.set_caption("Forza Horizon 7")\

bg_image=p.transform.scale(p.image.load("car.png").convert(), (Screen_width,Screen_height))     
sprite=p.transform.scale(p.image.load("car selection.png").convert_alpha(),(500,200))
sprite_rect=sprite.get_rect(center=(Screen_width//2,Screen_height//2+200))
text=p.font.Font(None,30).render("Forza Horizon 7",True,p.Color("white"))
text_rect=text.get_rect(center=(Screen_width//2,Screen_height//2-200))

#main loop
def game_Loop():
 running=True
 clock=p.time.Clock()

 while running:
    for event in p.event.get():
        if event.type==p.QUIT:
            running=False
    display_1.blit(bg_image,(0,0))
    display_1.blit(sprite,sprite_rect)
    display_1.blit(text,text_rect)
    p.display.flip()
    
    clock.tick(30)
 p.quit()
 
if __name__=="__main__":
    game_Loop()
