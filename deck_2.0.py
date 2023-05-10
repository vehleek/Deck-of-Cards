
import pygame
import random

# Initialize Pygame
pygame.init()

# Define the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the card images
card_images = {}
suits = ['hearts', 'diamonds', 'clubs', 'spades']
for suit in suits:
    for rank in range(1, 14):
        filename = f'{rank}_of_{suit}.png'
        card_images[(suit, rank)] = pygame.image.load(filename)

# Build the deck of cards
deck = []
for suit in suits:
    for rank in range(1, 14):
        deck.append((suit, rank))

# Shuffle the deck
random.shuffle(deck)

# Draw a card
def draw_card():
    if deck:
        suit, rank = deck.pop()
        card_image = card_images[(suit, rank)]
        scaled_card_image = pygame.transform.scale(card_image, (int(card_image.get_width()/2), int(card_image.get_height()/2)))
        screen.blit(scaled_card_image, (SCREEN_WIDTH/2 - scaled_card_image.get_width()/2, SCREEN_HEIGHT/2 - scaled_card_image.get_height()/2))
        #screen.blit(card_image, (SCREEN_WIDTH/2 - card_image.get_width()/2, SCREEN_HEIGHT/2 - card_image.get_height()/2))
        
# Iterate through the deck and print each card
for card in deck:
    suit, rank = card
    print(f"{rank} of {suit}")

# Start the event loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # The user closed the window
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # The user pressed the enter button
                draw_card()

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()