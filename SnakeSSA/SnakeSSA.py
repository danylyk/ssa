import pygame

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake SSA")
        self.window = pygame.display.set_mode((900, 480))
        self.run = True
        self.fps = 17 # 1000/60 - 60 fps
        self.__Run()

    def __Run(self):
        while self.run:
            pygame.time.delay(self.fps)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False

            self.__Draw()
            pygame.display.update()
        
        pygame.quit()

    def __Draw (self):
        pygame.draw.rect(self.window, (255,0,0), (50, 50, 50, 50))


app = App()