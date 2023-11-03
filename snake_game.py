import pygame
import random
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20

WHITE = (255,255,255)
RED = (255,0,0)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

snake_pos = [[WIDTH//2, HEIGHT//2]]
snake_speed = [0, BLOCK_SIZE]


def generate_food():
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_pos = [x, y]
        if food_pos not in snake_pos:
            return food_pos


food_pos = generate_food()


def draw_objects():
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(win, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))


def update_snake():
    global food_pos
    new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]

    if new_head == food_pos:
        food_pos = generate_food()
    else:
        snake_pos.pop()

    snake_pos.insert(0, new_head)


def game_over():
    return (snake_pos[0] in snake_pos[1:] or snake_pos[0][0] > WIDTH - BLOCK_SIZE or
            snake_pos[0][0] < 0 or snake_pos[0][1] > HEIGHT - BLOCK_SIZE or snake_pos[0][1] < 0)


def run():
    global snake_speed, snake_pos, food_pos
    snake_pos = [[WIDTH//2, HEIGHT//2]]
    snake_speed = [0, BLOCK_SIZE]
    food_pos = generate_food()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_UP]:
                    if snake_speed[1] == BLOCK_SIZE:
                        continue
                    snake_speed = [0, -BLOCK_SIZE]
                if keys[pygame.K_DOWN]:
                    if snake_speed[1] == -BLOCK_SIZE:
                        continue
                    snake_speed = [0, BLOCK_SIZE]
                if keys[pygame.K_LEFT]:
                    if snake_speed[0] == BLOCK_SIZE:
                        continue
                    snake_speed = [-BLOCK_SIZE, 0]
                if keys[pygame.K_RIGHT]:
                    if snake_speed[0] == -BLOCK_SIZE:
                        continue
                    snake_speed = [BLOCK_SIZE, 0]
        update_snake()
        draw_objects()
        if game_over():
            break
        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    run()
