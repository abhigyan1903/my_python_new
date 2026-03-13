import pygame

def main():                     
    pygame.init()                
    screen = pygame.display.set_mode((400, 300)) 
    pygame.display.set_caption("Blank Window") 

    running = True
    while running:                
        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                running = False

    pygame.quit()
if __name__ == "__main__":
    main()                  