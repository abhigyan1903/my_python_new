#making a game screen and adding two rectangl;e sprites to it
import pygame as x
x.init()

def main():
      display=x.display.set_mode((800,600))
      x.display.set_caption("Forza horizon")
      bg_image=x.transform.scale(x.image.load("car.png").convert(), (800,600))
      sprite=x.transform.scale(x.image.load("car selection.png").convert_alpha(),(800,200))
      sprite_rect=sprite.get_rect(center=(800//2,600//2-200))
      done=True
      z,y=30,30
      width,height=60,60
      while done:
          clock=x.time.Clock()
          
          for event in x.event.get():
                  if event.type==x.QUIT:
                        
                        done=False
          display.blit(bg_image,(0,0))
          display.blit(sprite,sprite_rect)
          
             
          
          press=x.key.get_pressed()
          if press[x.K_LEFT]:
                z-=7
          if press[x.K_RIGHT]:
                z+=7
          if press[x.K_UP]:
                y-=7
          if press[x.K_DOWN]:
                y+=7
          z=max(0,min(z,400-width))
          y=max(0,min( y,500-height))
          rect_1=x.draw.rect(display,'red',(z,y,width,height))
          rect_2=x.draw.rect(display,'green',(240,460,45,70))
          x.display.flip()
          clock.tick(60)
      x.quit()     
                
          
if __name__=="__main__":
        main()    
      
       
       