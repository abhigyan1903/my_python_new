#hello
import pygame
pygame.init()
screen = pygame.display.set_mode((2500, 1300))
pygame.display.set_caption("roblox")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()                    

                