import pygame
import pytmx
import pyscroll

class Game():
    def __init__(self):
        pygame.display.set_caption("My_Game")
        self.screen = pygame.display.set_mode((800,600))

        tmx_data = pytmx.load_pygame("maps/carte_world.tmx", pixelalpha=True)
    
        self.map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(self.map_data, (800,600))
        self.map_layer.zoom = 2

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=2)

    def run(self):
        run = True
        while run:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False          

        pygame.quit()