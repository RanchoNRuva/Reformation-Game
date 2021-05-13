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


def draw_window(luther, ground, ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8):
    WIN.fill(WHITE)
    WIN.blit(GROUND_IMAGE, (ground.x, ground.y))
    WIN.blit(GROUND_IMAGE, (ground1.x, ground1.y))
    WIN.blit(GROUND_IMAGE, (ground2.x, ground2.y))
    WIN.blit(GROUND_IMAGE, (ground3.x, ground3.y))
    WIN.blit(GROUND_IMAGE, (ground4.x, ground4.y))
    WIN.blit(GROUND_IMAGE, (ground5.x, ground5.y))
    WIN.blit(GROUND_IMAGE, (ground6.x, ground6.y))
    WIN.blit(GROUND_IMAGE, (ground7.x, ground7.y))
    WIN.blit(GROUND_IMAGE, (ground8.x, ground8.y))
    WIN.blit(MT_LUTHER, (luther.x, luther.y))
    pygame.display.update()


def main():
    luther = pygame.Rect(200, 255, MT_LUTHER_WIDTH, MT_LUTHER_HEIGHT)
    ground = pygame.Rect(0, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground1 = pygame.Rect(100, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground2 = pygame.Rect(200, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground3 = pygame.Rect(300, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground4 = pygame.Rect(400, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground5 = pygame.Rect(500, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground6 = pygame.Rect(600, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground7 = pygame.Rect(700, 455, GROUND_HEIGHT, GROUND_WIDTH)
    ground8 = pygame.Rect(800, 455, GROUND_HEIGHT, GROUND_WIDTH)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            #if ground.x < 0:
               # ground.x += ground8.x + 100
            #else:
            ground.x += VEL
            ground1.x += VEL
            ground2.x += VEL
            ground3.x += VEL
            ground4.x += VEL
            ground5.x += VEL
            ground6.x += VEL
            ground7.x += VEL
            ground8.x += VEL

        if keys_pressed[pygame.K_RIGHT]:
            ground.x -= VEL
            ground1.x -= VEL
            ground2.x -= VEL
            ground3.x -= VEL
            ground4.x -= VEL
            ground5.x -= VEL
            ground6.x -= VEL
            ground7.x -= VEL
            ground8.x -= VEL
        
        draw_window(luther, ground, ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8)

    pygame.quit()


if __name__ == "__main__":
    main()
