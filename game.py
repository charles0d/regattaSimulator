import pygame
from boat import Boat
from polar import polar_function

HEIGHT = 600
WIDTH = 1000


def central_rotation(image, angle, xc, yc):
    rotated_image = pygame.transform.rotate(image, angle)
    rot_rect = rotated_image.get_rect(
        center=image.get_rect(center=(xc, yc)).center)

    return rotated_image, rot_rect


vrPolar = polar_function("polar.pol")
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 128, 255))
done = False

b = Boat('1', WIDTH-800, HEIGHT-500, 45, vrPolar)

starboardImage = pygame.image.load('images/blueStarboard.png')
starboardImage = pygame.transform.rotozoom(starboardImage, -45, 0.3)
portImage = pygame.image.load('images/bluePort.png')
portImage = pygame.transform.rotozoom(portImage, 45, 0.3)
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if b.bearing == 0:
            b.bearing = 359
        else:
            b.bearing -= 1
    if pressed[pygame.K_RIGHT]:
        if b.bearing == 359:
            b.bearing = 0
        else:
            b.bearing += 1
    screen.fill((0, 128, 255))
    if b.bearing < 180:
        img = portImage
    else:
        img = starboardImage

    rot_image, new_rect = central_rotation(img, -b.bearing, 1000-b.x, 600-b.y)
    screen.blit(rot_image, new_rect.topleft)
    pygame.display.flip()
    clock.tick(250)
    b.update_position()

pygame.quit()
print("Game terminated")
