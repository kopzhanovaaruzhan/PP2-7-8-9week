import pygame
import math
from datetime import datetime
import time
pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Task for mickey clock")

background = pygame.image.load("mickey.jpg")  
second_hand = pygame.image.load("left_hand.png")
minute_hand = pygame.image.load("right_hand.png")  

background = pygame.transform.scale(background, (WIDTH, HEIGHT))
minute_hand = pygame.transform.scale(minute_hand, (600,350))
second_hand = pygame.transform.scale(second_hand, (600,350))

center_x, center_y = WIDTH // 2, HEIGHT // 2

font = pygame.font.Font(None, 36)

def get_angle(units, total_units):
    return - (units * (360 / total_units))

tick_sound = pygame.mixer.Sound("clock_old.mp3") 
tick_sound.play(loops=-1, maxtime=0)

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(background, (0, 0)) 

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = get_angle(minutes, 60) 
    second_angle = get_angle(seconds, 60)  

    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)

    minute_rect = rotated_minute.get_rect(center=(center_x, center_y))
    second_rect = rotated_second.get_rect(center=(center_x, center_y))

    screen.blit(rotated_minute, minute_rect.topleft)
    screen.blit(rotated_second, second_rect.topleft)

    now=datetime.now()
    current_time_text = now.strftime("%H:%M:%S")
    text_surface = font.render(current_time_text, True, (0,0,0))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 30))
    screen.blit(text_surface, text_rect)

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)

pygame.quit()