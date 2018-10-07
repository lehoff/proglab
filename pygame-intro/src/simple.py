
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# ----- Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ----- END Setup



def draw_simple():
    pygame.draw.ellipse(screen, BLACK, [10,10, 20,30], 2)

# -------- Main Program Loop -----------
while not done:

    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    # --- Drawing Code

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    
    
    # ----- Do your own drawing
    draw_simple()

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

