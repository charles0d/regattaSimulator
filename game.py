import pygame


def central_rotation(image, angle, xc, yc):
    rotated_image = pygame.transform.rotate(image, angle)
    rot_rect = rotated_image.get_rect(
        center=image.get_rect(center=(xc, yc)).center)

    return rotated_image, rot_rect


pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((0, 128, 255))
done = False
x, y = 500, 400
a = 0

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
        if a == 180:
            a = -179
        else:
            a += 1
    if pressed[pygame.K_RIGHT]:
        if a == -180:
            a = 179
        else:
            a -= 1
    screen.fill((0, 128, 255))
    if a < 0:
        img = portImage
    else:
        img = starboardImage
    rot_image, new_rect = central_rotation(img, a, x, y)
    screen.blit(rot_image, new_rect.topleft)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
