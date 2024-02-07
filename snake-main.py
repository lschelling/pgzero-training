import pgzrun as pgz
import random
from enum import Enum
from snake import Snake, Snake2, SnakeMaze

BOARD_SIZE = 16
SEGMENT_SIZE = 20
WIDTH = BOARD_SIZE * SEGMENT_SIZE
HEIGHT = BOARD_SIZE * SEGMENT_SIZE
WHITE = 255, 255, 255
GREEN = 0,255,0
RED = 255,0,0
GREY= 100,100,100

richtung = ''

class GameState(Enum):
    START = 1
    PLAY = 2
    SUCCESS = 3
    GAMEOVER = 4

class Game():

    def __init__(self):
        self.level=0
        self.transitionStart()

    def transitionPlay(self):
        self.state=GameState.PLAY

    def transitionStart(self):
        self.level+=1
        self.snake= self.Snakefactory()
        self.state=GameState.START
    
    def Snakefactory(self):
        self.Success= False
        if (self.level==1):
            return Snake(BOARD_SIZE, SEGMENT_SIZE, 4)
        elif (self.level==2):
            return Snake(BOARD_SIZE, SEGMENT_SIZE, 8)
        elif (self.level==3):
            return Snake2(BOARD_SIZE, SEGMENT_SIZE, 4)
        elif (self.level==4):
            return Snake2(BOARD_SIZE, SEGMENT_SIZE, 8)
        elif (self.level==5):
            self.Success= True
            return SnakeMaze(BOARD_SIZE, SEGMENT_SIZE, 2) 

    def transitionSuccess(self):
        self.level+=1
        self.state=GameState.SUCCESS

    def transitionGameover(self):
        self.state=GameState.GAMEOVER
        self.level=0

game=Game()


def draw_start(screen):
    screen.draw.text(game.snake.get_level_text(),(WIDTH//2-100,HEIGHT//2),color=(0,255,255))
    screen.draw.text('Press space to start',(WIDTH//2-100,HEIGHT//2+20),color=(0,255,255))

def draw_gameover(screen):
    screen.draw.text('Gameover',(WIDTH//2-100,HEIGHT//2),color=(0,255,255))

def draw_gamedone(screen, score, level):
    screen.draw.text('You Win',(WIDTH//2-100,HEIGHT//2),color=(0,255,255))


def draw():
    screen.clear()
    if game.state==GameState.START:
        draw_start(screen)
    if game.state==GameState.PLAY:
        game.snake.draw(screen, game.level)
    if game.state==GameState.SUCCESS:
        draw_gamedone(screen, game.snake.score, game.level)
    if game.state==GameState.GAMEOVER:
        draw_gameover(screen)
       

def update():
    global richtung
    if keyboard.right or keyboard.KP6  :
        richtung = 'E'
    elif keyboard.left or keyboard.KP4:
        richtung = 'W'
    elif keyboard.down or keyboard.KP2 :
         richtung = 'N'
    elif keyboard.up or keyboard.KP8:
        richtung = 'S'

    if game.state==GameState.START:
        if keyboard.space:
            richtung = ''
            game.transitionPlay()
    if game.state==GameState.PLAY:
        game.snake.update(richtung)
        if game.snake.level_done():
            richtung = ''
            if game.Success:
                game.transitionSuccess()
            else:
                game.transitionStart()
            
        if game.snake.gameover:
            richtung = ''
            game.transitionGameover()
    if game.state==GameState.SUCCESS:
        if keyboard.space:
            richtung = ''
            exit()
    if game.state==GameState.GAMEOVER:
        if keyboard.space:
            richtung = ''
            game.transitionStart()

pgz.go()
