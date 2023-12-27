import pygame
import random
import os
pygame.init()
pygame.font.init()


WIDTH = 1000
HEIGHT = 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (255, 50, 50)

GAME_OVER_FONT = pygame.font.SysFont('montserrat black', 100)
SCORE_FONT = pygame.font.SysFont('montserrat black', 50)

VEL = 10
FPS = 25

GRASS = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'GRASS.jpg')), (WIDTH, HEIGHT))
EGG = pygame.transform.scale(pygame.image.load(os.path.join('Assets','EGG.png')), (12, 15))
SNAKE_HEAD = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'snake_head.png')), (20, 20))
SNAKE_BODY = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'snake_body.png')), (20, 20))
SNAKE_TAIL = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'snake_tail.png')), (20, 20))

def draw_text_score(snake_pos):
    SCORE_TEXT = SCORE_FONT.render('SCORE: ' + str(len(snake_pos) - 4), 1, BLACK)
    WIN.blit(SCORE_TEXT, (0, 0))
    
    pygame.display.update()
    
def game_over():
    GAME_OVER_DISPLAY = GAME_OVER_FONT.render("GAME OVER", 1, WHITE)
    WIN.blit(GAME_OVER_DISPLAY, (WIDTH//2 - GAME_OVER_DISPLAY.get_width()//2, HEIGHT//2 - GAME_OVER_DISPLAY.get_height()//2))
    pygame.display.update()
    pygame.time.delay(3000)
    

def main():
    
    
    snake_pos = [
        [100, 50],
        [80, 50],
        [60, 50],
        [40, 50]
    ]
    
    new_x = 100
    new_y = 50
    
    left = False
    right = True
    up = False
    down = False
    
    run = True
    
    clock = pygame.time.Clock()
    
    fruit = pygame.Rect(random.randint(0, 985), random.randint(0, 788), 10, 10)
    
    rotate = 0
    
    while run:
        
        clock.tick(FPS)
        
        WIN.blit(GRASS, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        key = pygame.key.get_pressed()
        
        
        if left == True:
            new_x -= VEL
            rotate = 180
        if right == True:
            new_x += VEL
            rotate = 0
        if up == True:
            new_y -= VEL
            rotate = 90
        if down == True:
            new_y += VEL
            rotate = 270
            
            
        snake_pos.insert(0, [new_x, new_y])
        snake_pos.pop()
        
        if key[pygame.K_LEFT]:
            left = True
            right = False
            up = False
            down = False
        if key[pygame.K_RIGHT]:
            left = False
            right = True
            up = False
            down = False
        if key[pygame.K_UP]:
            left = False
            right = False
            up = True
            down = False
        if key[pygame.K_DOWN]:
            left = False
            right = False
            up = False
            down = True
            
        for block in snake_pos:
            
            if block == snake_pos[0]:
                WIN.blit(pygame.transform.rotate(SNAKE_HEAD, rotate), (block[0], block[1]))     
            elif block == snake_pos[len(snake_pos) - 1]:
                WIN.blit(pygame.transform.rotate(SNAKE_TAIL, rotate), (block[0], block[1])) 
            else:
                WIN.blit(pygame.transform.rotate(SNAKE_BODY, rotate), (block[0], block[1]))
                 
            
        WIN.blit(EGG, fruit)
            
        draw_text_score(snake_pos)
        
        if snake_pos[0][0] + 10 <= fruit.x + 12 and snake_pos[0][0] + 10 >= fruit.x and snake_pos[0][1] + 10 <= fruit.y + 15 and snake_pos[0][1] + 10 >= fruit.y:
            snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1]])
            fruit = pygame.Rect(random.randint(0, 985), random.randint(0, 788), 10, 10)
            WIN.blit(EGG, fruit)
            
        if snake_pos[0][0] + 20 >= WIDTH or snake_pos[0][0] <= 0 or snake_pos[0][1] <= 0 or snake_pos[0][1] + 20 >= HEIGHT:
            game_over()
            break
        
        pygame.display.update()
        
if __name__ == "__main__":
    main()