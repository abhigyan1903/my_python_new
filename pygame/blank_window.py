#hello i am making a blank window
import pygame as x
x.init()
x.display.set_mode((600,700))
running=True
while running:
    for event in x.event.get():
        if event.type==x.QUIT:
            running=False
x.quit()