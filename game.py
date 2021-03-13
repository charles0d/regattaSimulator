import pygamefrom constants import *class Game:    def __init__(self, boat, buoy):        self.boat = boat        self.buoy = buoy    def run(self):        pygame.init()        screen = pygame.display.set_mode((WIDTH, HEIGHT))        done = False        clock = pygame.time.Clock()        while not done:            for event in pygame.event.get():                if event.type == pygame.QUIT:                    done = True            pressed = pygame.key.get_pressed()            if pressed[pygame.K_LEFT]:                self.boat.turn(LEFT, 1)            if pressed[pygame.K_RIGHT]:                self.boat.turn(RIGHT, 1)            if self.boat.is_arrived(self.buoy.rect.center):                done = True                print(f'Boat {self.boat.name} has arrived at the objective')            screen.fill((0, 128, 255))            screen.blit(self.boat.surf, self.boat.rect.topleft)            screen.blit(self.buoy.surf, self.buoy)            pygame.display.flip()            self.boat.update()            if pressed[pygame.K_ESCAPE]:                done = True                print('Game escaped')            clock.tick(50)        pygame.quit()        print("Game terminated")