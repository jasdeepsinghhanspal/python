import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Set up the snake
snake_head = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
snake_body = [[snake_head[0] - 1, snake_head[1]], [snake_head[0] - 2, snake_head[1]]]
snake_direction = "RIGHT"

# Set up the food
food_position = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Handle keypress events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move the snake
    if snake_direction == "UP":
        snake_head[1] -= 1
    if snake_direction == "DOWN":
        snake_head[1] += 1
    if snake_direction == "LEFT":
        snake_head[0] -= 1
    if snake_direction == "RIGHT":
        snake_head[0] += 1

    # Check collision with the food
    if snake_head == food_position:
        # Generate new food position
        food_position = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
        # Add a new segment to the snake
        snake_body.append([])

    # Check collision with the walls or itself
    if snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT or snake_head in snake_body[1:]:
        running = False
        pygame.quit()

    # Move the snake body
    snake_body.insert(0, list(snake_head))
    if len(snake_body) > 1:
        snake_body.pop()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the food
    pygame.draw.rect(screen, RED, (food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

