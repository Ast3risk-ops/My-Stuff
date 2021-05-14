import pygame
import random
pygame.init()
dis_width = 800
dis_height = 600
dis=pygame.display.set_mode((dis_width, dis_height), pygame.FULLSCREEN)
pygame.display.update()
pygame.display.set_caption("Snake.py")
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red=(255,0,0)
green = (0,255,0)
gold = (255,215,0)
clock = pygame.time.Clock()
x1 = dis_width/2
y1 = dis_height/2
x1_change = 0
y1_change = 0
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None,50)
score_font = pygame.font.SysFont("papyrus",35)
def Score(score):
    value = score_font.render("Your score: " + str(score), True, green)
    dis.blit(value, [0,0]) # Coordinates of text placement
def snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
def message(msg, color):
    img = font_style.render(msg, True, color)
    dis.blit(img, [dis_width/10, dis_height/2])
def gameLoop():
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    game_over = False
    game_close = False
    foodx = round(random.randrange(0, dis_width - snake_block)/20.0)*10.0
    foody = round(random.randrange(0, dis_width - snake_block)/20.0)*10.0
    game_close = False
    while not game_over:
        while game_close == True:
            dis.fill(red)
            message("You Lost! Press Q to Quit or C to Play Again", black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        dis.fill(white)
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change =0
                if event.key ==pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change =0
                if event.key ==pygame.K_UP:
                    x1_change = 0
                    y1_change =-snake_block
                if event.key ==pygame.K_DOWN:
                    x1_change = 0
                    y1_change =snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_head:
                game_close = True
        snake(snake_block, snake_List)
        Score(Length_of_snake - 1) # - because initial snake length is 1
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block)/20.0)*10.0
            foody = round(random.randrange(0, dis_width - snake_block)/20.0)*10.0
            Length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
