import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Reformation")

WHITE = (255, 255, 255)

FPS = 60
VEL = 5

MT_LUTHER_WIDTH, MT_LUTHER_HEIGHT = 300, 100
MT_LUTHER_IMAGE = pygame.image.load(os.path.join('assets', 'MTLuther.png'))
MT_LUTHER = pygame.transform.scale(MT_LUTHER_IMAGE, (200, 200))

GROUND_WIDTH, GROUND_HEIGHT = 100, 45
GROUND_IMAGE = pygame.image.load(os.path.join('assets', 'ground.png'))


def draw_window(luther, ground):
    WIN.fill(WHITE)
    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        WIN.blit(GROUND_IMAGE, (ground[i].x, ground[i].y))
    WIN.blit(MT_LUTHER, (luther.x, luther.y))
    pygame.display.update()


def main():
    luther = pygame.Rect(200, 255, MT_LUTHER_WIDTH, MT_LUTHER_HEIGHT)
    ground = []
    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        ground.append(pygame.Rect((100 * i), 455, GROUND_HEIGHT, GROUND_WIDTH)
    clock = pygame.time.Clock()
    run = True
    while run::
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        keys_pressed=pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            for i in [0, 1, 2, 3, 4, 5, 6, 7]:
                ground[i].x += VEL

        if keys_pressed[pygame.K_RIGHT]:
            for i in [0, 1, 2, 3, 4, 5, 6, 7]:
                ground[i].x -= VEL

        draw_window(luther, ground)

    pygame.quit()


if __name__ == "__main__":
    main()
