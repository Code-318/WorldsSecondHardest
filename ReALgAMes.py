import pygame
import sys
import webbrowser

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Worlds Second Hardest Game")

PLAYER_COLOUR = (255, 100, 0)
PLATFORM_COLOUR = (87, 153, 6)
COIN_COLOUR = (255, 223, 0)
FONT = pygame.font.Font(None, 36)
FONT2 = pygame.font.Font(None, 60)
FONT3 = pygame.font.Font(None, 160)
FONT4 = pygame.font.Font(None, 40)
LABEL_COLOUR = (255, 255, 255)
GROUND_COLOUR = (87, 153, 6)
BLACK = (0,0,0)
SPIKE_COLOUR = (255,0,0)

player = pygame.Rect(5, 525, 50, 50)
player_speed = 5

level = 1
coins = 0
coin_collected = False

islands = [
    pygame.Rect(200, 390, 150, 20),
    pygame.Rect(400, 290, 150, 20),
    pygame.Rect(600, 190, 150, 20),
]

platforms = []
spikes = []
loop_done = True
platform_x = 100

coin = pygame.Rect(660, 150, 30, 30)

ground = pygame.Rect(0, 570, 800, 30)

jump_power = 0
gravity = False
jump_allowed = True
ground_y = 525

clock = pygame.time.Clock()


def draw_gradient_background(surface, top_COLOUR, bottom_COLOUR):
    """Draw a vertical gradient background."""
    for y in range(surface.get_height()):
        COLOUR = [
            top_COLOUR[i] + (bottom_COLOUR[i] - top_COLOUR[i]) * y // surface.get_height()
            for i in range(3)
        ]
        pygame.draw.line(surface, COLOUR, (0, y), (surface.get_width(), y))

def show_intro_screen():
    intro_text = FONT4.render("This may be an old version of the game.", True, LABEL_COLOUR)
    intro_text2 = FONT4.render("If so, click here to get the latest version:", True, LABEL_COLOUR)
    intro_text3 = FONT.render("https://code-318.github.io/WorldsSecondHardest/Game.html", True, LABEL_COLOUR)
    press_key_text = FONT2.render("Press any key to start!", True, LABEL_COLOUR)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                running = False
                return  # Exit the intro screen

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detect click on the link area (simple click detection based on position)
                if 100 <= pygame.mouse.get_pos()[0] <= 700 and 300 <= pygame.mouse.get_pos()[1] <= 320:
                    webbrowser.open("https://code-318.github.io/WorldsSecondHardest/Game.html")
                    running = False
                    return  # Exit the intro screen
        
        screen.fill(BLACK)
        screen.blit(intro_text, (135, 200))
        screen.blit(intro_text2, (135, 250))
        screen.blit(intro_text3, (45, 300))
        screen.blit(press_key_text, (180, 450))
        
        pygame.display.flip()
        clock.tick(60)
def show_end_screen():
    end_text = FONT4.render("You have completed the whole game (For Now)", True, LABEL_COLOUR)
    end_text2 = FONT4.render("Make Sure To Download Latest Verion:", True, LABEL_COLOUR)
    end_text3 = FONT.render("https://code-318.github.io/WorldsSecondHardest/Game.html", True, LABEL_COLOUR)
    press_key_text = FONT2.render("(This Is Edition 4)", True, LABEL_COLOUR)
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                running = False
                return  # Exit the intro screen

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detect click on the link area (simple click detection based on position)
                if 100 <= pygame.mouse.get_pos()[0] <= 700 and 300 <= pygame.mouse.get_pos()[1] <= 320:
                    webbrowser.open("https://code-318.github.io/WorldsSecondHardest/Game.html")
                    running = False
                    return  # Exit the intro screen
        
        screen.fill(BLACK)
        screen.blit(end_text, (80, 150))
        screen.blit(end_text2, (135, 250))
        screen.blit(end_text3, (45, 300))
        screen.blit(press_key_text, (225, 450))
        
        pygame.display.flip()
        clock.tick(60)

show_intro_screen()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and jump_allowed:
        jump_power = -20
        gravity = True
        jump_allowed = False

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.x > 5:
        player.x -= player_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        player.x += player_speed
    
    if player.x > 800 and coins == level:
        player.x = -20
        level += 1
        coin_collected = False
    
    for spike in spikes:
        if player.colliderect(spike):
            player.x = 5
            player.y = 535
            if coin_collected:
                coins -= 1
                coin_collected = False
    
    if level == 2:
        coin = pygame.Rect(555, 115, 30, 30)
        islands = [
            pygame.Rect(400, 490, 150, 20),
            pygame.Rect(200, 350, 150, 20),
            pygame.Rect(500, 150, 150, 20),
        ]
    if level == 3:
        coin = pygame.Rect(660, 150, 30, 30)
        islands = [
            pygame.Rect(200, 390, 150, 20),
            pygame.Rect(0, 190, 150, 20),
            pygame.Rect(300, 100, 150, 20),
            pygame.Rect(600, 190, 150, 20),
        ]
        spikes = [
            pygame.Rect(260, 340, 30, 50),
            pygame.Rect(60, 140, 30, 50),
            pygame.Rect(360, 50, 30, 50),
        ]
    if level == 4:
        coin = pygame.Rect(700, 150, 30, 30)
        islands = [
            pygame.Rect(270, 210, 150, 20),
            
            pygame.Rect(150, 420, 70, 150),
        ]
        spikes = [
            pygame.Rect(720, 550, 50, 30)
        ]
    if level == 5:
        coin = pygame.Rect(535, 150, 30, 30)
        islands = [
            pygame.Rect(0, 100, 150, 20),
            pygame.Rect(0, 220, 150, 20),
            pygame.Rect(474, 190, 150, 20),
    
            pygame.Rect(200, 420, 70, 150),
        ]
        spikes = [
            pygame.Rect(580, 180, 40, 10)
        ]
    if level == 6:
        coin = pygame.Rect(70, 215, 30, 30)
        islands = [
            pygame.Rect(10, 255, 150, 20),
            pygame.Rect(670, 400, 150, 20),
            pygame.Rect(474, 190, 150, 20),
        ]
        spikes = [
            pygame.Rect(575, 180, 40, 10),
            pygame.Rect(100, 560, 40, 10),
            pygame.Rect(210, 560, 40, 10),
            pygame.Rect(320, 560, 40, 10),
            pygame.Rect(430, 560, 40, 10),
            pygame.Rect(540, 560, 40, 10),
        ]
    if level == 7:
        coin = pygame.Rect(30, 30, 30, 30)
        platform2_x = (platform_x * -1) + 600
        islands = [
            pygame.Rect(670, 200, 150, 20),
            pygame.Rect(platform_x, 400, 150, 20),
            pygame.Rect(platform2_x, 100, 150, 20),
            pygame.Rect(180, 50, 25, 80),
        ]
        spikes = [
            pygame.Rect(130, 555, 575, 30),
            pygame.Rect(400, 300, 40, 300),
            pygame.Rect(400, -249, 40, 300)
        ]
    if level == 8:
        coin = pygame.Rect(765, 520, 30, 30)
        islands = [
            pygame.Rect(0, 0, 50, 500),
            pygame.Rect(250, 70, 50, 500)
        ]
        spikes = [
            pygame.Rect(245, 420, 5, 150),
            pygame.Rect(50, 270, 5, 150),
            pygame.Rect(245, 150, 5, 150),
            pygame.Rect(50, 0, 5, 150),
            pygame.Rect(300, 565, 250, 50),
            pygame.Rect(610, 565, 140, 50),
        ]
    if level == 9:
        running = False
        show_end_screen()
    if player.colliderect(coin):
        if not coin_collected:
            coins += 1
        coin_collected = True
    
    for island in islands:
        if player.colliderect(island):
            if player.x < island.x:
                player.x -= 5
                if player.y + player.height <= island.y + island.height and level >= 7:
                    jump_allowed = True
            elif player.x > island.x - island.width:
                player.x += 5
                if player.y + player.height <= island.y + island.height and level >= 7:
                    jump_allowed = True

    if gravity:
        player.y += jump_power
        jump_power += 1

        if player.y >= ground_y:
            player.y = ground_y
            gravity = False
            jump_allowed = True

        for island in islands:
            if player.colliderect(island):
                if (
                    player.y + player.height <= island.y + 10
                    and jump_power > 0
                ):
                    player.y = island.top - player.height
                    gravity = False
                    jump_allowed = True
                    jump_power = 0
                elif player.y > island.y:
                    jump_power = +3
                elif jump_power > 5:
                    player.y = island.top - player.height
                    gravity = False
                    jump_allowed = True
                    jump_power = 0

    if not gravity:
        on_island = False
        for island in islands:
            if (
                player.colliderect(island)
                and player.y + player.height == island.top
            ):
                on_island = True
                break
        if not on_island and player.y + player.height < ground_y:
            gravity = True

    draw_gradient_background(screen, (50, 100, 200), (153, 200, 240))

    for island in islands:
        pygame.draw.rect(screen, PLATFORM_COLOUR, island)
    for spike in spikes:
        pygame.draw.rect(screen, SPIKE_COLOUR, spike)
    if not loop_done:
        platform_x += 2
        if platform_x >= 600:
            loop_done = True
    elif loop_done:
        platform_x -= 2
        if platform_x <= 0:
            loop_done = False
    if not coin_collected:
        pygame.draw.rect(screen, COIN_COLOUR, coin)
    else:
        arrow_label = FONT3.render("-->", True, BLACK)
        screen.blit(arrow_label, (620, 400))
    pygame.draw.rect(screen, GROUND_COLOUR, ground)
    pygame.draw.rect(screen, PLAYER_COLOUR, player)
    
    level_label = FONT.render(f"Level: {level}", True, LABEL_COLOUR)
    coins_label = FONT.render(f"Coins: {coins}", True, LABEL_COLOUR)
    # Display the labels in the top-left corner
    screen.blit(level_label, (10, 10))  # Draw "Level" at (10, 10)
    screen.blit(coins_label, (10, 50))  # Draw "Coins" at (10, 50)   
    
    if level == 1:
        tutorial_label1 = FONT2.render("Collect The Coin", True, LABEL_COLOUR)
        screen.blit(tutorial_label1, (240, 70))
    elif level ==3:
        tutorial_label2 = FONT2.render("Watch out for spikes!", True, LABEL_COLOUR)
        screen.blit(tutorial_label2, (220, 5))
    elif level == 4:
        tutorial_label3 = FONT2.render("Use an Air Jump", True, LABEL_COLOUR)
        screen.blit(tutorial_label3, (247, 40))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

