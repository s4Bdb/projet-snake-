# ==================================================
# VERSION 5 : Ajout de l’écran Game Over
# ==================================================

import pygame
import random

pygame.init()

LARGEUR = 600
HAUTEUR = 400
TAILLE_CASE = 10

screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Snake V5")

font = pygame.font.SysFont(None, 30)
grand_font = pygame.font.SysFont(None, 50)

pomme_img = pygame.image.load("assets/pomme.png").convert_alpha()
pomme_img = pygame.transform.scale(pomme_img, (TAILLE_CASE, TAILLE_CASE))

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


def afficher_game_over(score):
    screen.fill((0, 0, 0))

    titre = grand_font.render("GAME OVER", True, (255, 0, 0))
    texte_score = font.render(f"Score final : {score}", True, (255, 255, 255))

    screen.blit(titre, (190, 150))
    screen.blit(texte_score, (220, 220))

    pygame.display.flip()


snake = [(100, 100), (90, 100), (80, 100)]
direction = (TAILLE_CASE, 0)

score = 0
food = generer_pomme(snake)

running = True
game_over = False

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:

            if event.key == pygame.K_UP and direction != (0, TAILLE_CASE):
                direction = (0, -TAILLE_CASE)

            elif event.key == pygame.K_DOWN and direction != (0, -TAILLE_CASE):
                direction = (0, TAILLE_CASE)

            elif event.key == pygame.K_LEFT and direction != (TAILLE_CASE, 0):
                direction = (-TAILLE_CASE, 0)

            elif event.key == pygame.K_RIGHT and direction != (-TAILLE_CASE, 0):
                direction = (TAILLE_CASE, 0)

    if not game_over:

        head = snake[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])

        if new_head[0] < 0 or new_head[0] >= LARGEUR or new_head[1] < 0 or new_head[1] >= HAUTEUR:
            game_over = True

        if new_head in snake:
            game_over = True

        if not game_over:

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

    else:
        afficher_game_over(score)

pygame.quit()