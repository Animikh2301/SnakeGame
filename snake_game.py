import pygame
import random

pygame.init()

# Defining of Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

screen_width = 1200
screen_height = 600

# Creating Window of the game
gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("SnakeGame with Animikh")
pygame.display.update()



# Defining Clock
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])



# Game loop
def gameloop():

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 30
    fps = 40
    velocity_x = 0
    velocity_y = 0
    score = 0
    init_velocity = 5
    snk_list = []
    snk_length = 1

    # with open("hiscore.txt","r") as f:
    #     hiscore = f.read()

    # Food
    food_x = random.randint(0, screen_width - 10)
    food_y = random.randint(0, screen_height - 10)


    while not exit_game:

        if game_over:
            # with open("hiscore.txt","w") as f:
            #     f.write(str(hiscore))
            gameWindow.fill(black)
            text_screen("GAME OVER! Press Enter to Restart.", red, 260, 280)

            for event in pygame.event.get():
                print(event)
                
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                print(event)
                
                if event.type == pygame.QUIT:
                    exit_game = True
            
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y       


            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
                score += 1
                # print("SCORE: ",score*10)
                food_x = random.randint(0, screen_width - 10)
                food_y = random.randint(0, screen_height - 10)
                snk_length += 5
                # if (score > int(hiscore)):
                #     hiscore = score

            gameWindow.fill(white)
            text_screen("SCORE: " + str(score*10), red, 5, 5)
            pygame.draw.rect(gameWindow, blue, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                print("GAME OVER")


            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

        # pygame.quit()
        # quit()


gameloop()