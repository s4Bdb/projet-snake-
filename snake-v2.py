 ==================================================
# VERSION 2 : Ajout du score et de l’image pomme
# ==================================================

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake V2")

score = 0
font = pygame.font.SysFont(None, 30)

pomme_img = pygame.image.load("assets/pomme.png").convert_alpha()
pomme_img = pygame.transform.scale(pomme_img, (10, 10))

snake = [(100, 100), (90, 100), (80, 100)]
direction = (10, 0)

food = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -10)
            elif event.key == pygame.K_DOWN:
                direction = (0, 10)
            elif event.key == pygame.K_LEFT:
                direction = (-10, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (10, 0)

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    if new_head[0] < 0 or new_head[0] >= 600 or new_head[1] < 0 or new_head[1] >= 400:
        running = False

    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = (random.randrange(0, 600, 10), random.randrange(0, 400, 10))
    else:
        snake.pop()

    screen.fill((0, 0, 0))

    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))

    screen.blit(pomme_img, food)

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
