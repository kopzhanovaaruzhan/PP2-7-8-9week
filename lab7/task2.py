# Create music player with keyboard controller. You have to be able to press keyboard: play,
# stop, next and previous as some keys. Player has to react to the given command appropriately.


import pygame

pygame.init()
pygame.mixer.init()

side = 600
screen = pygame.display.set_mode((side, side))
pygame.display.set_caption("Music player")

shyda = pygame.transform.scale(pygame.image.load("shyda.jpg"), (side, side))
ozingana = pygame.transform.scale(pygame.image.load("ozin_gana.jpg"), (side, side))
taspa = pygame.transform.scale(pygame.image.load("taspa.jpg"), (side, side))

arrP = [shyda, ozingana, taspa]
arrM = ["shyda.mp3" , "ozingana.mp3" , "taspa.mp3"]

index = 0 
is_playing = False 


prev_button_rect = pygame.Rect(20, side - 50, 50, 40)
next_button_rect = pygame.Rect(side - 70, side - 50, 50, 40)

def play_music():
    global is_playing
    pygame.mixer.music.load(arrM[index])
    pygame.mixer.music.play()
    is_playing = True

font = pygame.font.Font(None, 36) 
instructions_font = pygame.font.Font(None, 24)

play_instructions = instructions_font.render("Press Space to play or stop music", True, (255, 255, 255))
change_music_instructions = instructions_font.render("Click << to go to previous song, >> for next song", True, (255, 255, 255))

running = True
while running:
    screen.blit(arrP[index], (0, 0))  

    pygame.draw.rect(screen, (0, 0, 0), prev_button_rect)
    pygame.draw.rect(screen, (0, 0, 0), next_button_rect)
    
    prev_text = font.render("<<", True, (255, 255, 255))
    next_text = font.render(">>", True, (255, 255, 255))

    screen.blit(prev_text, (prev_button_rect.x + 10, prev_button_rect.y + 5))
    screen.blit(next_text, (next_button_rect.x + 10, next_button_rect.y + 5))

    screen.blit(play_instructions, (85, side - 60))
    screen.blit(change_music_instructions, (85, side - 30))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.stop()
                    is_playing = False
                else:
                    play_music()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if prev_button_rect.collidepoint(event.pos):
                index = (index - 1) % len(arrM)
                play_music()
            elif next_button_rect.collidepoint(event.pos):
                index = (index + 1) % len(arrM)
                play_music()

pygame.quit() 
