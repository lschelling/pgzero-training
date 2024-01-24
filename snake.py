import pgzrun as pgz
from pygame import Rect
import random
from maze import Maze

BOARD_SIZE = 16
SEGMENT_SIZE = 20
WIDTH = BOARD_SIZE * SEGMENT_SIZE
HEIGHT = BOARD_SIZE * SEGMENT_SIZE
WHITE = 255, 255, 255
GREEN = 0,255,0
RED = 255,0,0
GREY= 100,100,100
                
class Segment:
     def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

class Snake:
    
    def __init__(self, board_size, segment_size, apples_collect):
        self.segment_size=segment_size
        self.board_size=board_size
        self.segments=[]
        self.bricks=[]
        self.apples=[]
        self.setup_walls()
        self.setup_snake()
        self.setup_apples()
        self.score=0
        self.gameover=False
        self.collect_done = apples_collect
        self.cframe= 0
        self.speed= 20
    def add_apple (self):
        while True:
            free = True
            y=random.randint(2,BOARD_SIZE-2)
            x=random.randint(1,BOARD_SIZE-2)
        
            for s in self.segments:
                if x== s.xpos and y== s.ypos :
                    free = False
            for b in self.bricks:
                if x== b.xpos and y== b.ypos :
                    free = False
            for a in self.apples:
                if x== a.xpos and y== a.ypos :
                    free = False
        
            if free:
                break
        self.apples.append(Segment(x,y))

    


    def setup_apples(self):
        self.add_apple()

    def setup_snake(self):
        self.segments.append(Segment(self.board_size//2,self.board_size//2))
        self.segments.append(Segment(self.board_size//2,self.board_size//2+1))
        self.segments.append(Segment(self.board_size//2,self.board_size//2+2))

    def setup_walls(self):
        for x in range(0,BOARD_SIZE ):
            self.bricks.append(Segment(x,1))
            self.bricks.append(Segment(x,self.board_size-1))
        for y in range(2,BOARD_SIZE-1):
            self.bricks.append(Segment(0,y))
            self.bricks.append(Segment(self.board_size-1,y))
            
    def get_level_text(self):
        return 'Collect ' + str(self.collect_done) + ' apples'
    
    def draw(self,screen, level) :

        h = True
        for s in self.segments:
            r =Rect (s.xpos*self.segment_size, s.ypos*self.segment_size, self.segment_size, self.segment_size) 
            if h :
                screen.draw.filled_rect(r,WHITE)
                h = False
            else :
                screen.draw.filled_rect(r,GREEN)
        for b in self.bricks:
            r =Rect (b.xpos*self.segment_size, b.ypos*self.segment_size, self.segment_size, self.segment_size) 
            screen.draw.filled_rect(r,GREY)

        for a in self.apples:
            r =Rect (a.xpos*self.segment_size, a.ypos*self.segment_size, self.segment_size, self.segment_size) 
            screen.draw.filled_rect(r,RED)

        screen.draw.text('score__'+str(self.score),(0,0),color=(0,255,255))
        screen.draw.text('level__'+str(level),(self.board_size*self.segment_size-120,0),color=(0,255,255))
        
    def check_gameover(self,x,y):
        for s in self.segments:
            if x== s.xpos and y== s.ypos:
                return True
        for b in self.bricks:
            if x== b.xpos and y== b.ypos:
                return True
        return False
        

    def level_done(self):
        return self.score >= self.collect_done
        
    def update(self,richtung):
        self.cframe+=1
        if self.cframe % self.speed == 0:
            x = self.segments[0].xpos
            y = self.segments[0].ypos
            if richtung =='N':
                y = y+1
            elif richtung =='E':
                x = x+1
            elif richtung =='W':
                x= x-1
            elif richtung =='S':
                y= y-1
            else:
                return

            if False==self.check_gameover(x,y) :
                self.segments.insert(0,Segment(x,y))
                if self.apples[0].xpos==x and self.apples[0].ypos==y :
                    self.apples.remove(self.apples[0])
                    self.add_apple()
                    self.score+=1
                else:
                    self.segments.pop()
                    
            else : 
                self.gameover = True

        if self.cframe % (60*2) == 0 and self.speed > 2:
            self.speed-=1

class Snake2 (Snake):
    
    def setup_walls(self):
        super().setup_walls()
        ypos=random.randint(2,BOARD_SIZE-2)
        xpos=random.randint(1,BOARD_SIZE-2)
        self.bricks.append(Segment(xpos,ypos))

class SnakeMaze (Snake):
    def setup_walls(self):
        sizex=BOARD_SIZE//2-1
        sizey=BOARD_SIZE//2-1
        self.maze = Maze.generate(sizex,sizey)
        m = self.maze._to_str_matrix()
        for y in range(len(m)):
            for x in range(len(m[y])):
                if m[x][y]=='O':
                    self.bricks.append(Segment(x,y+1))

            
    def setup_snake(self):
        while True:
            free = True
            y=random.randint(2,BOARD_SIZE-2)
            x=random.randint(1,BOARD_SIZE-2)
        
            for s in self.segments:
                if x== s.xpos and y== s.ypos :
                    free = False
            for b in self.bricks:
                if x== b.xpos and y== b.ypos :
                    free = False
            for a in self.apples:
                if x== a.xpos and y== a.ypos :
                    free = False
        
            if free:
                break
        self.segments.append(Segment(x,y))

    def get_level_text(self):
        return 'Find the way to the apple '
        