import pgzrun as pgz
import random

WIDTH = 600
HEIGHT = 600
WHITE = 255, 255, 255

snake =Rect (300, 300, 20, 20) 
dx = 0
dy = 0
def snakemove():
    snake.x += dx
    snake.y += dy
    print ("ok")
    
clock.schedule_interval(snakemove, 0.5)


def draw():
    screen.clear()
    screen.draw.filled_rect(snake, WHITE)


def update():
    global dx
    global dy
    if keyboard.right and snake.left <= WIDTH:
        dx = 20
        dy = 0
    elif keyboard.left and snake.right >= 0:
        dx = -20
        dy = 0
    
    if keyboard.down and snake.bottom <= HEIGHT:
         dy = 20
         dx = 0
    elif keyboard.up and snake.top >= 0:
        dy = -20
        dx = 0
        
pgz.go()
