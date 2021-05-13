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


def draw_window(luther, ground, ground1, ground2, ground3):
    WIN.fill(WHITE)
    WIN.blit(GROUND_IMAGE, (ground.x, ground.y))
    WIN.blit(GROUND_IMAGE, (ground1.x, ground1.y))
    WIN.blit(GROUND_IMAGE, (ground2.x, ground2.y))
    WIN.blit(GROUND_IMAGE, (ground3.x, ground3.y))
    WIN.blit(MT_LUTHER, (luther.x, luther.y))
    pygame.display.update()


def main():
    luther = pygame.Rect(200, 255, MT_LUTHER_WIDTH, MT_LUTHER_HEIGHT)
    ground = pygame.Rect(0, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground1 = pygame.Rect(100, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground2 = pygame.Rect(200, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground3 = pygame.Rect(300, 455, GROUND_HEIGHT, GROUND_WIDTH)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            ground.x += VEL
            ground1.x += VEL
            ground2.x += VEL
            ground3.x += VEL

        if keys_pressed[pygame.K_RIGHT]:
            ground.x -= VEL
            ground1.x -= VEL
            ground2.x -= VEL
            ground3.x -= VEL
        
        draw_window(luther, ground, ground1, ground2, ground3)

    pygame.quit()


if __name__ == "__main__":
    main()