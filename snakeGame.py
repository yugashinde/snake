import pygame
import sys
import random

# TO DO
# rescritct snake from going in the direction of its head

# add "lives" concept 
# add high score concept 
# pause feature 
# cuter animations?

pygame.init()
rows = 25
columns = 25 
tile_size = 25
board_width = tile_size * columns
board_height = tile_size * rows
s_velocity = (0,0)
s_size = 1
canvas =   pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
exit = False 


def get_rand(limit):
    return random.randint(0,limit-1)*tile_size
food = pygame.Rect(get_rand(columns),get_rand(rows),tile_size, tile_size)
snake = []
snake.append(pygame.Rect(get_rand(columns),get_rand(rows),tile_size, tile_size))


 # velocity = movement of the snake in x and y direction.

while not exit: # game loop 
    for event in pygame.event.get(): # listening for events like click 
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP,pygame.K_w) and s_velocity != (1, 0):
                s_velocity = (0,-tile_size)
            elif event.key in (pygame.K_DOWN,pygame.K_s):
                s_velocity = (0,tile_size)
            elif event.key in (pygame.K_LEFT,pygame.K_a):
                s_velocity = (-tile_size,0)
            elif event.key in (pygame.K_RIGHT,pygame.K_d):
                s_velocity = (tile_size,0)

        # move 
        for i in range(len(snake)-1,0,-1): # copy the position of the previous segment to the current segment.
            snake[i]= snake[i-1].copy()
            
            
        snake[0].move_ip(s_velocity)

        # check if snake eats food 
        if snake[0].center == food.center:
            snake.append(food)
            food = pygame.Rect(get_rand(columns),get_rand(rows),tile_size, tile_size) # generate new food 

        # check if snake hits the wall, reset the game if yes 
        if not canvas.get_rect().contains(snake[0]):
            snake.clear()
            food = pygame.Rect(get_rand(columns),get_rand(rows),tile_size, tile_size)
            snake.append(pygame.Rect(get_rand(columns),get_rand(rows),tile_size, tile_size))

        # check if snake hits itself or goes towards head, reset the game if yes
        

        canvas.fill("black")
        pygame.draw.rect(canvas, "red", food) # (x,y) is the top left corner of 25x25 pix square. 
        for s in snake:
            pygame.draw.rect(canvas, "green", s)

        pygame.display.update()
        clock.tick(10) # processing changes 10 frames per second

