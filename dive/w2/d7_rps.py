'''
DIA 7
Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario 
jugar piedra, papel o tijeras contra la computadora.
'''

# Terminal version
# pip install keyboard

import keyboard
import random
import winsound

class Color:
    RED_CLR = '\x1b[31m'
    GREEN_CLR = '\x1b[32m'
    BLUE_CLR = '\x1b[34m'
    END_CLR = '\033[0m'
    BG_RED = '\x1b[41m'	
    BG_GREEN = '\x1b[42m'
    BG_YELLOW = '\x1b[43m'

def menu():
    print(f"""
    {GREEN}Rock Paper Scissors Game{END}
    1. Play Game
    2. Instructions
    3. Exit
    """)
    choice = input("Select an option: ")
    if choice == '1':
        rounds = int(input("Enter amount of rounds to play: "))
        game(rounds=rounds)
    elif choice == '2':
        print(f"""
        {BLUE}Instructions:{END}
        - Press 1 to select Rock ✊
        - Press 2 to select Paper 🖐️
        - Press 3 to select Scissors ✌️
        The game will compare your choice with the CPU's choice and determine the winner.
        """)
        menu()
    elif choice == '3':
        print("Thank you for playing!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")
        menu()

def run_func():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == '1':
                return 'r'
            elif event.name == '2':
                return 'p'
            elif event.name == '3':
                return 's'
            
def emojify(pick):
    if pick == 'r':
        return '✊'
    elif pick == 'p':
        return '🖐️'
    else:
        return '✌️'
    
def play_sound(result):
    if result == "You Win":
        winsound.Beep(750, 800)
    elif result == "You Lose":
        winsound.Beep(250, 800)
    else:
        winsound.Beep(500, 800)

# Determines round winner or draw
def determine_winner(player: str, cpu: str):
    if player == cpu:
        return "Draw"
    elif player == "r" and cpu == "s" or player == "p" and cpu == "r" or player == "s" and cpu == "p":
        return "You Win"
    else:
        return "You Lose"

# Determines game winner or draw
def check_winner(player_wins, cpu_wins):
    if player_wins > cpu_wins:
        print(f"\n{GREEN_BG}You Win!{END}")
    elif player_wins < cpu_wins:
        print(f"\n{RED_BG}You Lost{END}")
    else: 
        print(f"\n{YELLOW_BG}Draw{END}")
    
def game(rounds):
    player_wins = 0
    cpu_wins = 0

    count = 0

    while count != rounds:
        print("Press: ")
        player_pick = run_func()
        cpu_pick = random.choice(rps_list)

        result = determine_winner(player=player_pick, cpu=cpu_pick)
        play_sound(result=result)
        
        player_emoji = emojify(player_pick)
        cpu_emoji = emojify(cpu_pick)

        print(f"You: {player_emoji}, CPU: {cpu_emoji}  - {result}")
        
        if result == "You Win":
            player_wins += 1
        elif result == "You Lose":
            cpu_wins += 1
        
        count += 1

    check_winner(player_wins, cpu_wins)
    print(f"\nFinal Score:\nYou: {player_wins}\nCPU: {cpu_wins}")

# Colors for text and text background
RED = Color.RED_CLR
GREEN = Color.GREEN_CLR
BLUE = Color.BLUE_CLR

RED_BG = Color.BG_RED
GREEN_BG = Color.BG_GREEN
YELLOW_BG = Color.BG_YELLOW

END = Color.END_CLR

# List of choices for CPU

rps_list = ["r", "p", "s"]

menu()

# Pygame version
# Inspired by: https://rockpaperscissors-ai.vercel.app/

'''
import pygame 
import random

pygame.init()

# Display dimensions
WIDTH = 320
HEIGHT = 300

# Colors
BLUE = (106, 144, 255)
GRAY = (220, 220, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rock Paper Scissors')

class Button:
    def __init__(self, text, x, y, width, height, choice):
        self.text = text 
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.choice = choice

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        text_surf = button_font.render(self.text, True, BLUE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self.choice
        return None

# Fonts
title_font = pygame.font.SysFont(None, 36, bold=True)
subtitle_font = pygame.font.SysFont(None, 24)
score_font = pygame.font.SysFont(None, 48)
label_font = pygame.font.SysFont(None, 32)
choice_font = pygame.font.SysFont(None, 28)
result_font = pygame.font.SysFont(None, 32)
button_font = pygame.font.SysFont(None, 24)

# Options
rps = ['Rock', 'Paper', 'Scissors']

# Scores
player_score = 0
cpu_score = 0

# Initial choices
player_pick = "Rock"
cpu_pick = "Scissors"
result_text_content = "Start"

# UI elements
title_text = title_font.render("Rock Paper Scissors", True, BLUE)
title_text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 12))

score_text = subtitle_font.render("Score", True, BLUE)
score_text_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 5.5))

player_score_text = score_font.render(str(player_score), True, BLUE)
player_score_text_rect = player_score_text.get_rect(midleft=(WIDTH // 2 - 100, HEIGHT // 2.5))

cpu_score_text = score_font.render(str(cpu_score), True, BLUE)
cpu_score_text_rect = cpu_score_text.get_rect(midright=(WIDTH // 2 + 100, HEIGHT // 2.5))

player_text = label_font.render("You", True, BLACK)
player_text_rect = player_text.get_rect(midleft=(WIDTH // 2 - 110, HEIGHT // 4))

cpu_text = label_font.render("CPU", True, BLACK)
cpu_text_rect = cpu_text.get_rect(midright=(WIDTH // 2 + 110, HEIGHT // 4))

rock_button = Button("Rock", 20, HEIGHT - 60, 80, 40, "Rock")
paper_button = Button("Paper", 120, HEIGHT - 60, 80, 40, "Paper")
scissors_button = Button("Scissors", 220, HEIGHT - 60, 80, 40, "Scissors")

def determine_winner(player, cpu):
    if player == cpu:
        return "Draw"
    elif (player == "Rock" and cpu == "Scissors") or (player == "Paper" and cpu == "Rock") or (player == "Scissors" and cpu == "Paper"):
        return "You Win"
    else:
        return "You Lose"

while True:
    screen.fill(WHITE)

    player_choice_text = choice_font.render(player_pick, True, BLACK)
    player_choice_rect = player_choice_text.get_rect(midleft=(WIDTH // 2 - 120, HEIGHT // 1.8))

    cpu_choice_text = choice_font.render(cpu_pick, True, BLACK)
    cpu_choice_rect = cpu_choice_text.get_rect(midright=(WIDTH // 2 + 120, HEIGHT // 1.8))

    result_text = result_font.render(result_text_content, True, BLUE)
    result_text_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))

    screen.blit(title_text, title_text_rect)
    screen.blit(score_text, score_text_rect)
    screen.blit(player_score_text, player_score_text_rect)
    screen.blit(cpu_score_text, cpu_score_text_rect)
    screen.blit(player_text, player_text_rect)
    screen.blit(cpu_text, cpu_text_rect)
    screen.blit(player_choice_text, player_choice_rect)
    screen.blit(cpu_choice_text, cpu_choice_rect)
    screen.blit(result_text, result_text_rect)
    pygame.draw.line(screen, BLUE, (WIDTH // 2, HEIGHT // 3.5), (WIDTH // 2, HEIGHT // 1.8))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        player_choice = rock_button.check_click(event) or paper_button.check_click(event) or scissors_button.check_click(event)
        if player_choice:
            player_pick = player_choice
            cpu_pick = random.choice(rps)
            result = determine_winner(player_pick, cpu_pick)
            result_text_content = result
            if result == "You Win":
                player_score += 1
            elif result == "You Lose":
                cpu_score += 1

            player_score_text = score_font.render(str(player_score), True, BLUE)
            cpu_score_text = score_font.render(str(cpu_score), True, BLUE)

    rock_button.draw(screen)
    paper_button.draw(screen)
    scissors_button.draw(screen)

    pygame.display.update()
'''