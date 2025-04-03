import pygame
import sys
import math
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint')

white = (255, 255, 255)
black = (0, 0 , 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, white)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, (self.rect.x + 2, self.rect.y + 12))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

drawing = False
brush_color = black
drawing_shape = "line"  # drawing shape is a line
drawing_start_pos = None

rectangle_click_count = 0
circle_click_count = 0

def set_black():
    global brush_color
    brush_color = black

def set_green():
    global brush_color
    brush_color = green

def set_red():
    global brush_color
    brush_color = red

def set_blue():
    global brush_color
    brush_color = blue

def clear_screen():
    screen.fill(white)

def exit_app():
    pygame.quit()
    sys.exit()

def set_rectangle():
    global drawing_shape, rectangle_click_count
    rectangle_click_count += 1
    if rectangle_click_count == 2:
        drawing_shape = "line"  # switch back to line after two clicks
        rectangle_click_count = 0  # reset the counter
    else:
        drawing_shape = "rectangle"

def set_circle():
    global drawing_shape, circle_click_count
    circle_click_count += 1
    if circle_click_count == 2:
        drawing_shape = "line"
        circle_click_count = 0 
    else:
        drawing_shape = "circle" 

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(380, 10, 60, 30, 'Exit', gray, exit_app),
    Button(450, 10, 60, 30, 'Rectangle', gray, set_rectangle),
    Button(520, 10, 60, 30, 'Circle', gray, set_circle)
]

clear_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                drawing = True
                drawing_start_pos = pygame.mouse.get_pos()
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                drawing_start_pos = None 
                
        for button in buttons:
            button.check_action(event)

    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if drawing_shape == "line":
            if drawing_start_pos:
                pygame.draw.line(screen, brush_color, drawing_start_pos, (mouse_x, mouse_y), 5)
                drawing_start_pos = (mouse_x, mouse_y)

        elif drawing_shape == "rectangle":
            if drawing_start_pos:  # ensure start position is not None
                rect_width = mouse_x - drawing_start_pos[0]
                rect_height = mouse_y - drawing_start_pos[1]
                pygame.draw.rect(screen, brush_color, (drawing_start_pos[0], drawing_start_pos[1], rect_width, rect_height), 5)

        elif drawing_shape == "circle":
            if drawing_start_pos:  # ensure start position is not None
                radius = int(math.sqrt((mouse_x - drawing_start_pos[0])**2 + (mouse_y - drawing_start_pos[1])**2))
                pygame.draw.circle(screen, brush_color, drawing_start_pos, radius, 5)

    pygame.draw.rect(screen, gray, (0, 0, width, 50))  # background for buttons
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()  # update the display
