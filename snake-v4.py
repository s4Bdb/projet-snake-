 ==================================================
# VERSION 4 : Fonction pour générer la pomme
# ==================================================

import pygame
import random

pygame.init()

LARGEUR = 600
HAUTEUR = 400
TAILLE_CASE = 10

screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Snake V4")

score = 0
font = pygame.font.SysFont(None, 30)

pomme_img = pygame.image.load("assets/pomme.png").convert_alpha()
pomme_img = pygame.transform.scale(pomme_img, (TAILLE_CASE, TAILLE_CASE))

snake = [(100, 100), (90, 100), (80, 100)]
direction = (TAILLE_CASE, 0)

clock = pygame.time.Clock()


def generer_pomme(snake):
    pomme = (
        random.randrange(0, LARGEUR, TAILLE_CASE),
        random.randrange(0, HAUTEUR, TAILLE_CASE)
    )

    while pomme in snake:
        pomme = (
            random.randrange(0, LARGEUR, TAILLE_CASE),
            random.randrange(0, HAUTEUR, TAILLE_CASE)
        )

    return pomme


food = generer_pomme(snake)

running = True

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, TAILLE_CASE):
                direction = (0, -TAILLE_CASE)

            elif event.key == pygame.K_DOWN and direction != (0, -TAILLE_CASE):
                direction = (0, TAILLE_CASE)

            elif event.key == pygame.K_LEFT and direction != (TAILLE_CASE, 0):
                direction = (-TAILLE_CASE, 0)

            elif event.key == pygame.K_RIGHT and direction != (-TAILLE_CASE, 0):
                direction = (TAILLE_CASE, 0)

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    if new_head[0] < 0 or new_head[0] >= LARGEUR or new_head[1] < 0 or new_head[1] >= HAUTEUR:
        running = False

    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = generer_pomme(snake)
    else:
        snake.pop()

    screen.fill((0, 0, 0))

    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, TAILLE_CASE, TAILLE_CASE))

    screen.blit(pomme_img, food)

    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()

