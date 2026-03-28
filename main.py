import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game 🎮")

font = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 128, 255)

state = "menu"
max_num = 100
number = 0
input_text = ""

running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_btn.collidepoint(event.pos):
                    max_num = 50
                    number = random.randint(1, max_num)
                    state = "game"

                if medium_btn.collidepoint(event.pos):
                    max_num = 100
                    number = random.randint(1, max_num)
                    state = "game"

                if hard_btn.collidepoint(event.pos):
                    max_num = 200
                    number = random.randint(1, max_num)
                    state = "game"

        elif state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(input_text)
                        if guess == number:
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

    # ===== GAME SCREEN =====
    elif state == "game":
        prompt = font.render(f"Guess (1-{max_num}): {input_text}", True, BLACK)
        screen.blit(prompt, (100, 150))

        if 'result' in locals():
            res_text = font.render(result, True, BLACK)
            screen.blit(res_text, (250, 200))

    # ===== WIN SCREEN =====
    elif state == "win":
        win_text = font.render("🎉 You Won!", True, BLACK)
        screen.blit(win_text, (220, 150))

    pygame.display.update()

pygame.quit()
sys.exit()