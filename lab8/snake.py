import pygame
import sys
import random

# initialize Pygame
pygame.init()

width, height = 500, 500
cell_size = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game for lab 8')

# images for head, body, tail, and food
head_img = pygame.image.load('head.png')
body_img = pygame.image.load('body.png')
tail_img = pygame.image.load('tail.png')
food_img = pygame.image.load('apple.png')

# scale images to fit the grid
head_img = pygame.transform.scale(head_img, (cell_size, cell_size))
body_img = pygame.transform.scale(body_img, (cell_size, cell_size))
tail_img = pygame.transform.scale(tail_img, (cell_size, cell_size))
food_img = pygame.transform.scale(food_img, (cell_size, cell_size))

# colors
background_color = pygame.Color('#00b7ef')
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# game variables
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = 'RIGHT'
change_to = direction

# random food generation
food_pos = [random.randrange(1, (width // cell_size)) * cell_size, random.randrange(1, (height // cell_size)) * cell_size]
food_spawn = True

# score and level
score = 0
level = 1
food_count = 0

# set up game clock
clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont('arial', 30)
    game_over_text = font.render(f'Game Over! Score: {score} Level: {level}', True, red)
    
    text_rect = game_over_text.get_rect()
    text_rect.center = (width // 2, height // 2)  # center
    
    screen.blit(game_over_text, text_rect)  # draw centered text
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# generatinig food
def generate_food():
    while True:
        food = [random.randrange(1, (width // cell_size)) * cell_size, random.randrange(1, (height // cell_size)) * cell_size]
        if food not in snake_body:
            return food

# draw the snake
def draw_snake():
    # draw the head
    head_direction = direction
    if head_direction == 'UP':
        head = pygame.transform.rotate(head_img, +90)
    elif head_direction == 'DOWN':
        head = pygame.transform.rotate(head_img, -90)
    elif head_direction == 'LEFT':
        head = pygame.transform.rotate(head_img, 180)
    else:
        head = head_img  # Right direction

    screen.blit(head, (snake_body[0][0], snake_body[0][1]))

    # draw the body 
    for i in range(1, len(snake_body) - 1):
        screen.blit(body_img, (snake_body[i][0], snake_body[i][1]))

    # draw the tail
    tail_direction = direction
    if tail_direction == 'UP':
        tail = pygame.transform.rotate(tail_img, 90)
    elif tail_direction == 'DOWN':
        tail = pygame.transform.rotate(tail_img, -90)
    elif tail_direction == 'LEFT':
        tail = pygame.transform.rotate(tail_img, 180)
    else:
        tail = tail_img  # right direction

    screen.blit(tail, (snake_body[-1][0], snake_body[-1][1]))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'

    direction = change_to

    # direction
    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

    # wall collision
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        game_over()

    snake_body.insert(0, list(snake_pos))

    # if snake eats food
    if snake_pos == food_pos:
        score += 10
        food_count += 1
        if food_count >= 3:
            level += 1
            food_count = 0
            clock.tick(10 + level) 
        food_spawn = False
    else:
        snake_body.pop()

    # food at a random position (not on snake or wall)
    if not food_spawn:
        food_pos = generate_food()
    food_spawn = True

    # if the snake collides with itself
    for block in snake_body[1:]:
        if block == snake_pos:
            game_over()

    # fill background with light blue color
    screen.fill(background_color)
    draw_snake()

    # apple image
    screen.blit(food_img, (food_pos[0], food_pos[1]))

    # score and level
    font = pygame.font.SysFont('arial', 20)
    score_text = font.render(f'Score: {score}', True, green)
    level_text = font.render(f'Level: {level}', True, blue)
    screen.blit(score_text, [10, 10])
    screen.blit(level_text, [10, 30])

    pygame.display.flip()
    clock.tick(10 + level)  #game speed based on the level

pygame.quit()
sys.exit()
