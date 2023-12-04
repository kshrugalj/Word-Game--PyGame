import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Guessing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
words = ['ruby', 'emerald', 'diamond', 'topaz', 'sapphire']
current_word = random.choice(words).upper()
guessed_letters = set()
MAX_TRIES = 10
tries = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key >= 97 and event.key <= 122:  # Check if the key pressed is a lowercase letter
                letter = chr(event.key).upper()
                if letter not in guessed_letters:
                    guessed_letters.add(letter)
                    if letter not in current_word:
                        tries += 1

    # Display the game information
    window.fill(WHITE)

    # Display the guessed letters
    guessed_text = font.render(f"Guessed letters: {' '.join(guessed_letters)}", True, BLACK)
    window.blit(guessed_text, (300, 100))

    # Display the current word
    display_word = ""
    for letter in current_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    text = font.render(display_word, True, BLACK)
    window.blit(text, (300, 300))

    # Display the number of chances left
    chances_text = font.render(f"Chances left: {MAX_TRIES - tries}", True, BLACK)
    window.blit(chances_text, (300, 400))

    # Display if the last guessed letter was correct or wrong
    last_guess_text = font.render(
        f"Last guess: {'Correct' if current_word[-1] in guessed_letters else 'Wrong'}", True, BLACK
    )
    window.blit(last_guess_text, (300, 500))

    # Check for win or lose
    if set(current_word) == guessed_letters:
        font = pygame.font.Font(None, 74)
        text = font.render("You win!", True, GREEN)
        window.blit(text, (250, 200))
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    if tries >= MAX_TRIES:
        font = pygame.font.Font(None, 74)
        text = font.render("You lose!", True, RED)
        window.blit(text, (250, 200))
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
