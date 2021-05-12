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
MT_LUTHER = pygame.transform.scale(MT_LUTHER_IMAGE, (200, 140))


def draw_window(luther):
    WIN.fill(WHITE)
    WIN.blit(MT_LUTHER, (luther.x, luther.y))
    pygame.display.update()


def main():
    luther = pygame.Rect(200, 140, MT_LUTHER_WIDTH, MT_LUTHER_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            luther.x -= VEL

        if keys_pressed[pygame.K_RIGHT]:
            luther.x += VEL
        
        draw_window(luther)

    pygame.quit()


if __name__ == "__main__":
    main()
