#making my firts gaming screen with pygame
import pygame as x
x.init()
screen_width,screen_height=1000,1000
screen=x.display.set_mode((screen_width,screen_height))
#load and scale images directly
bg=x.transform.scale(x.image.load("haunted_castle.jpeg").convert(),(screen_width,screen_height))
pn=x.transform.scale(x.image.load("start_35.png").convert_alpha(),(200,200))-
pn_rect=pn.get_rect(center=(screen_width//2,screen_height//2-30))
text_1=x.font.Font(None,46).render(" Beware of this scary haunted game!",True,x.Color("red"))
text_1_rect=text_1.get_rect(center=(screen_width//2,screen_height//2+110))
text=x.font.Font(None,46).render("The Haunted Castle Game",True,x.Color("brown"))
text_rect=text.get_rect(center=(screen_width//2,screen_height//2-120))
def game():
    clock=x.time.Clock()
    running=True
    while running:
        for event in x.event.get():
            if event.type==x.QUIT:
                runnig=False
        screen.blit(bg,(0,0))
        screen.blit(pn,pn_rect)
        screen.blit(text,text_rect)
        screen.blit(text_1,text_1_rect)
        x.display.flip()
        clock.tick(30)
    x.quit()
if __name__=="__main__":
    game()
                    
    