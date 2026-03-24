#add image
import pygame
pygame.init()
screen_width,screen_height=500,500
screen=pygame.display.set_mode((screen_width,screen_height))
#load and scale images directly
bg=pygame.transform.scale(pygame.image.load("backg.png").convert(),(screen_width,screen_height))
pn=pygame.transform.scale(pygame.image.load("red_fire.jpeg").convert_alpha(),(200,200))
pn_rect=pn.get_rect(center=(screen_width//2,screen_height//2-30))
text=pygame.font.Font(None,36).render("Roblox",True,pygame.Color("white"))
text_rect=text.get_rect(center=(screen_width//2,screen_height//2+110))
def game():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                runnig=False
        screen.blit(bg,(0,0))
        screen.blit(pn,pn_rect)
        screen.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=="__main__":
    game()
                    