import pygame
import sys
from const import *

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Chess")

    def mainloop(self):
        
        while True:
            for event in pygame.events.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

main = Main()
main.mainloop()

