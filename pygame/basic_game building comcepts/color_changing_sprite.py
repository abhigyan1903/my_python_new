#amking a color changing sprite
import pygame as x
def main():
    x.init()
    screen=x.display.set_mode((400,500))
    
    x.display.set_caption("Color changing sprite")
    color= {
         'red': x.Color('red'),
         'blue':x.Color('blue'),
         'green':x.Color('green'),
         'yellow':x.Color('yellow'),
         'white':x.Color('white')
         
    }
    current_color=color['white']
    z,y=30,30
    width,height=60,60
    done=False
    clock=x.time.Clock()
    while not done:
        for event in x.event.get():
            if event.type==x.QUIT:
                done=True
        press=x.key.get_pressed()
        if press[x.K_LEFT]:
            z-=7
        if press[x.K_RIGHT]:
            z+=7
        if press[x.K_UP]:
            y-=7 
        if press[x.K_DOWN]:
            y+=7
        #keep inside the screen
        z=max(0,min(z,400-width))
        y=max(0,min(y,500-height))
        #color change on touching boundries
        if z<=0 :
            current_color=color['red']
        elif z>=400 - width:
            current_color=color['blue']
        elif y<=0:
            current_color=color['green']
        elif y>=500 - height:
            current_color=color['yellow']
        else:
            current_color=color['white']
        #draw the sprite
        screen.fill(('red'))
        x.draw.rect(screen,current_color,(z,y,width,height))
        x.display.flip()
        clock.tick(60)
    x.quit()
if __name__=="__main__":
    main()
            