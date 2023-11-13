import pygame
import random
from button import Button

# to initialize pygame
pygame.init()

# to display screen window
screen = pygame.display.set_mode((800, 600))

# to change title and icon
pygame.display.set_caption("Brick Breaker")
icon = pygame.image.load('brick.png').convert_alpha()
pygame.display.set_icon(icon)

def get_font(size): 
    return pygame.font.Font("font.ttf", size)
def play():
    # positioning the paddle and ball on screen
    playerImg = pygame.image.load('bar.png')
    playerX = 350
    playerY = 480
    playerX_change = 0

    ball_velocity = [0.5, 0.5]
    ballImg = pygame.image.load('ball.png')
    ballX = 340
    ballY = 450

    running = True

    # function for drawing the paddle and ball at new coordinates
    def draw(x, y):
        screen.blit(playerImg, (x, y))
        screen.blit(ballImg, (ballX, ballY))


    brick_map = [
        [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        [4, 4, 5, 5, 7, 5, 5, 4, 4, 4, 4, 4, 4],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # function for creating the bricks
    def bricks(box):
        score = 0
        brick_colour = {
            2: (0, 0, 0),
            3: (172, 0, 44),
            4: (250, 155, 0),
            5: (170, 8, 144),
            6: (8, 156, 234),
            7: (100, 79, 244),
        }

        gap = 2
        brick_height = (400 / len(brick_map)) - 2
        brick_width = (800 / len(brick_map[0])) - 2

        for row_index, row in enumerate(brick_map):
            for col_index, col in enumerate(row):
                if col != 0:
                    y = row_index * (brick_height + gap) + gap // 2
                    x = col_index * (brick_width + gap) + gap // 2
                    b = pygame.Rect(x, y, brick_width, brick_height)
                    pygame.draw.rect(screen, brick_colour[col], b)
                    if box.colliderect(b):
                        brick_map[row_index][col_index] = 0
                        pygame.draw.rect(screen, (0, 0, 0), b)
                        score += 5
                        ball_velocity[1] *= -1


    # to close window when exit button is pressed
    while running:
        # screen colour, fill(Red, green, blue)
        screen.fill((0, 0, 0))

        # to close window when exit button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.8
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.8
            if event.type == pygame.KEYUP:
                playerX_change = 0
        if playerX <= 0:
            playerX = 0
            playerX_change = 0.8
        if playerX >= 670:
            playerX = 670
            playerX_change = -0.8

        pBox = pygame.Rect(playerX - 5, playerY + 55, 140, 25)
        pygame.draw.rect(screen, (0, 0, 0), pBox, 1)
        bBox = pygame.Rect(ballX, ballY , 25, 25)
        pygame.draw.rect(screen, (0, 0, 0), bBox, 1)
        if ballX < 0 or ballX > 772:
            ball_velocity[0] *= -1
        if ballY < 0:
            ball_velocity[1] *= -1
        if ballY > 568:
            pygame.time.wait(3000)
            running = False
        if bBox.colliderect(pBox):
            ball_velocity[1] *= -1
            ball_velocity[0] = random.choice([-1,1])
        bricks(bBox)
        ballX += ball_velocity[0]
        ballY += ball_velocity[1]
        playerX += playerX_change
        draw(playerX, playerY)
        pygame.display.update()
        

       

def main_menu():
    while True:
        screen.blit('Background.png', (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menubox = menu_text.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(menu_text, menubox)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(mouse_pos):
                    play()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    pygame.quit()
                    exit()

        pygame.display.update()

main_menu()

