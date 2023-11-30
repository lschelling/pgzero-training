from enum import Enum 
import pgzrun as pgz
import random

BOARD_SIZE = 30
SEGMENT_SIZE = 20
WIDTH = 600
HEIGHT = 600
WHITE = 255, 255, 255

class Direction(Enum):
    E = 1
    N = 2
    W = 3
    S = 4
    X = 5

class Segment:
    def __init__(self, posx, posy):
        self.xpos = posx
        self.ypos = posy

class Snake:
    def __init__(self, posx, posy):
        self.segments = []
        self.segments.append(Segment(posx, posy))
        self.segments.append(Segment(posx+1, posy))
        self.segments.append(Segment(posx+2, posy))
        self.grow = False
        
    def move(self, direction):
        dy=dx=0
        if direction == Direction.E:
            dx=1
        elif direction == Direction.N:
            dy=-1
        if direction == Direction.W:
            dx=-1
        elif direction == Direction.S:
            dy=1

        self.segments.insert(0, Segment(self.segments[0].xpos+dx, self.segments[0].ypos+dy))

        if self.grow:
            self.grow=False
        else:
            self.segments.pop()        

    def draw(self, screen):
        for s in self.segments:
            seg = Rect (s.xpos * SEGMENT_SIZE, s.ypos * SEGMENT_SIZE, SEGMENT_SIZE, SEGMENT_SIZE)
            screen.draw.filled_rect(seg, WHITE)

    def eat(self):
        self.grow = True

snake = Snake(15,15)
direction = Direction(Direction.X)

def snakemove():
    global direction
    snake.move(direction)
    
clock.schedule_interval(snakemove, 0.5)

def draw():
    screen.clear()
    snake.draw(screen)

def update():
    global direction
    if keyboard.right:
        direction = Direction.E
    elif keyboard.left:
        direction = Direction.W
    if keyboard.down:
        direction = Direction.S
    elif keyboard.up:
        direction = Direction.N        

    if keyboard.space:
        snake.eat()

pgz.go()
