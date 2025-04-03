import pygame
import sys
import math

pygame.init()

#screen
width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Paint')

#colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

# Button class 
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
        screen.blit(text_surface, text_rect)

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()  # Execute the action

# state variables
drawing = False
brush_color = black
drawing_shape = "line"
drawing_start_pos = None

shape_click_counts = {
    "rectangle": 0,
    "circle": 0,
    "square": 0,
    "right_triangle": 0,
    "equilateral_triangle": 0,
    "rhombus": 0
}

# functions for each shape
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

def toggle_shape(shape):
    global drawing_shape, shape_click_counts
    shape_click_counts[shape] += 1
    if shape_click_counts[shape] == 2:
        drawing_shape = "line"  # switch back to line after two clicks
        shape_click_counts[shape] = 0  
    else:
        drawing_shape = shape

def set_rectangle():
    toggle_shape("rectangle")

def set_circle():
    toggle_shape("circle")

def set_square():
    toggle_shape("square")

def set_right_triangle():
    toggle_shape("right_triangle")

def set_equilateral_triangle():
    toggle_shape("equilateral_triangle")

def set_rhombus():
    toggle_shape("rhombus")

# buttons for actions
buttons = [ 
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(380, 10, 60, 30, 'Exit', gray, exit_app),
    Button(450, 10, 60, 30, 'Rectangle', (64, 21, 25), set_rectangle),
    Button(520, 10, 60, 30, 'Circle', (64, 21, 25), set_circle),
    Button(590, 10, 60, 30, 'Square', (64, 21, 25), set_square),
    Button(660, 10, 60, 30, 'R.Triangle', (64, 21, 25), set_right_triangle),
    Button(730, 10, 60, 30, 'E.Triangle', (64, 21, 25), set_equilateral_triangle),
    Button(800, 10, 60, 30, 'Rhombus', (64, 21, 25), set_rhombus)
]

# initialize the screen
clear_screen()

def draw_equilateral_triangle(start, end):
    side_length = int(math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2))
    
    height = math.sqrt(3) / 2 * side_length

    center_x = (start[0] + end[0]) / 2
    center_y = (start[1] + end[1]) / 2 - height

    point1 = start
    point2 = end
    point3 = (center_x, center_y)

    pygame.draw.polygon(screen, brush_color, [point1, point2, point3], 5)

def draw_right_triangle(start, end):
    points = [
        start,
        (end[0], start[1]),  # right horizontal point
        (start[0], end[1])   # bottom vertical point
    ]
    pygame.draw.polygon(screen, brush_color, points, 5)  # outline with border width 5

def draw_rhombus(start, end):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    points = [
        (start[0], center_y),
        (center_x, start[1]),
        (end[0], center_y),
        (center_x, end[1])
    ]
    pygame.draw.polygon(screen, brush_color, points, 5) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                drawing_start_pos = pygame.mouse.get_pos()  # position where the mouse was clicked

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if drawing_shape == "line":
                    if drawing_start_pos:
                        pygame.draw.line(screen, brush_color, drawing_start_pos, (mouse_x, mouse_y), 5)

                elif drawing_shape == "rectangle" or drawing_shape == "square":
                    if drawing_start_pos:
                        rect_width = mouse_x - drawing_start_pos[0]
                        rect_height = mouse_y - drawing_start_pos[1]
                        if drawing_shape == "square":
                            rect_width = rect_height = min(abs(rect_width), abs(rect_height))
                        pygame.draw.rect(screen, brush_color, (drawing_start_pos[0], drawing_start_pos[1], rect_width, rect_height), 5)

                elif drawing_shape == "circle":
                    if drawing_start_pos:
                        radius = int(math.sqrt((mouse_x - drawing_start_pos[0])**2 + (mouse_y - drawing_start_pos[1])**2))
                        pygame.draw.circle(screen, brush_color, drawing_start_pos, radius, 5)

                elif drawing_shape == "right_triangle":
                    if drawing_start_pos:
                        draw_right_triangle(drawing_start_pos, (mouse_x, mouse_y))

                elif drawing_shape == "equilateral_triangle":
                    if drawing_start_pos:
                        draw_equilateral_triangle(drawing_start_pos, (mouse_x, mouse_y))

                elif drawing_shape == "rhombus":
                    if drawing_start_pos:
                        draw_rhombus(drawing_start_pos, (mouse_x, mouse_y))

                drawing_start_pos = None

        for button in buttons:
            button.check_action(event)

    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
