# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up,
# Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of
# pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave
# of the screen should be ignored

import pygame
pygame.init()

side = 500
screen = pygame.display.set_mode((side, side))
pygame.display.set_caption("red ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
x, y = side // 2, side // 2 
speed = 20  

piano = pygame.mixer.Sound("piano.mp3") 
piano.play(loops=-1, maxtime=0)

running = True
while running:
    screen.fill(WHITE)  
    pygame.draw.circle(screen, RED, (x, y), radius)  
    pygame.display.update() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - radius - speed >= 0:
                y -= speed
            if event.key == pygame.K_DOWN and y + radius + speed <= side:
                y += speed
            if event.key == pygame.K_LEFT and x - radius - speed >= 0:
                x -= speed
            if event.key == pygame.K_RIGHT and x + radius + speed <= side:
                x += speed

pygame.quit()