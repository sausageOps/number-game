import os
import sys

def resource_path(relative_path):
    import os, sys
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

import pygame
import sys
import random

pygame.init()
pygame.mixer.init()

# Load sounds
click_sound = pygame.mixer.Sound(resource_path("click.wav"))
win_sound = pygame.mixer.Sound(resource_path("win.wav"))

# Window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game 🎮")

# Font
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)
RED = (255, 0, 0)
GREEN = (0, 150, 0)

# Game variables
state = "menu"
max_num = 100
number = 0
input_text = ""
result = ""

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ===== MENU EVENTS =====
        if state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_btn.collidepoint(event.pos):
                    click_sound.play()
                    max_num = 50
                    number = random.randint(1, max_num)
                    input_text = ""
                    result = ""
                    state = "game"

                if medium_btn.collidepoint(event.pos):
                    click_sound.play()
                    max_num = 100
                    number = random.randint(1, max_num)
                    input_text = ""
                    result = ""
                    state = "game"

                if hard_btn.collidepoint(event.pos):
                    click_sound.play()
                    max_num = 200
                    number = random.randint(1, max_num)
                    input_text = ""
                    result = ""
                    state = "game"

        # ===== GAME EVENTS =====
        elif state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(input_text)
                        if guess == number:
                            win_sound.play()
                            state = "win"
                        elif guess < number:
                            result = "Too Low"
                        else:
                            result = "Too High"
                    except:
                        result = "Invalid input"
                    input_text = ""

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    input_text += event.unicode

        # ===== WIN EVENTS =====
        elif state == "win":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_btn.collidepoint(event.pos):
                    click_sound.play()
                    state = "menu"

    # ===== DRAW MENU =====
    if state == "menu":
        title = font.render("Select Difficulty", True, BLACK)
        screen.blit(title, (180, 50))

        easy_btn = pygame.Rect(200, 120, 200, 40)
        medium_btn = pygame.Rect(200, 180, 200, 40)
        hard_btn = pygame.Rect(200, 240, 200, 40)

        pygame.draw.rect(screen, BLUE, easy_btn)
        pygame.draw.rect(screen, BLUE, medium_btn)
        pygame.draw.rect(screen, BLUE, hard_btn)

        screen.blit(font.render("Easy", True, WHITE), (270, 130))
        screen.blit(font.render("Medium", True, WHITE), (250, 190))
        screen.blit(font.render("Hard", True, WHITE), (270, 250))

    # ===== DRAW GAME =====
    elif state == "game":
        prompt = font.render(f"Guess (1-{max_num}): {input_text}", True, BLACK)
        screen.blit(prompt, (100, 150))

        if result:
            if result == "Too Low" or result == "Too High":
                color = RED
            else:
                color = GREEN

            res_text = font.render(result, True, color)
            screen.blit(res_text, (250, 200))

    # ===== DRAW WIN =====
    elif state == "win":
        win_text = font.render("🎉 You Won!", True, BLACK)
        screen.blit(win_text, (220, 150))

        restart_btn = pygame.Rect(200, 220, 200, 50)
        pygame.draw.rect(screen, BLUE, restart_btn)

        screen.blit(font.render("Play Again", True, WHITE), (220, 235))

    pygame.display.update()

pygame.quit()
sys.exit()