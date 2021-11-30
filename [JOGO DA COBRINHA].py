import pygame
from pygame.locals import *
import random

def on_grid_random():

    x = random.randint(0, 1350)
    y = random.randint(0, 710)
    return (x//10 * 10, y//10 * 10)

def colisao(c1, c2):
    return (c1[0]==c2[0] and c1[1] == c2 [1])

def perde(p1, p2):
    return (p1[0]==p2[0] and p1[1]==p2[1])

#posicoes

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

pygame.init()
screen = pygame.display.set_mode((1360, 720))
pygame.display.set_caption('[SNAKE GAME]')

snake = [(300, 300), (310, 300), (320, 300)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 255, 0))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 2))
apple_pos = on_grid_random()

myDirection = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(18)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                myDirection = UP
            if event.key == K_DOWN:
                myDirection = DOWN
            if event.key == K_RIGHT:
                myDirection = RIGHT
            if event.key == K_LEFT:
                myDirection = LEFT

    if colisao(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
    if perde(snake, snake[1]):
        snake.clear()
        pygame.quit()

    if myDirection == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if myDirection == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if myDirection == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if myDirection == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    for c in range(len(snake) - 1, 0, -1):
        snake[c] = (snake[c-1][0], snake[c-1][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)
    pygame.display.update()
