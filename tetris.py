import pygame
import time


pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("test")

gameExit = False

dct = {}

objandtyp = []

class Tetrinimo():
        def __init__(self,typ,x,y):
                self.type = typ

                if self.type == 1:
                        self.blocks = [[x,y],[x+1,y+1],[x+2,y+2],[x+3,y+3]]
                
        def draw():
                for i in self.blocks():
                        pygame.draw.rect(gameDisplay, (255,0,0), [i[0], i[1], 10, 10], 1)



for i in range(8):
        dct[i] = 0

def new_b(x,y):
        pygame.draw.rect(gameDisplay, (255,0,0), [x, y, 10, 10], 1)

x = 400
y = 300

clock = pygame.time.Clock()
y_change = 10

while not gameExit:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True
                #print(event)

                tet = Tetrinimo(1,400,300)
        
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT and [[x-10,y]] not in objandtyp:
                                x-=10
                                y_change = 10
                        if event.key == pygame.K_RIGHT and [[x+10,y]] not in objandtyp:
                                x+=10
                                y_change = 10
        if  y<(500-dct[(x-360)//10]):
                y+=y_change
        else:
                t,s=x,y
                x=400
                y=300
                objandtyp.append([[t,s]])
                new_b(x,y)
                dct[(t-360)//10]+=10
                
                
                
        clock.tick(5)
        gameDisplay.fill((255,255,255))

        for _i in objandtyp:
                pygame.draw.rect(gameDisplay,(0,0,0),[_i[0][0],_i[0][1],10,10])

        for j in range(500,400,-10):
                c = True
                for i in range(360,440,10):
                        if [[i,j]] not in objandtyp:
                                c = False
                if c:
                        for k in range(360,440,10):
                                objandtyp.remove([[k,j]])

                        for k in dct.keys():
                                dct[k] -= 10

                        for k in objandtyp:
                                if k[0][1]<j:
                                        k[0][1]+=10
        
                


        pygame.draw.rect(gameDisplay,(0,0,0),[x,y,10,10])
        
        pygame.draw.line(gameDisplay,(0,0,0),[360,510],[360,0])
        pygame.draw.line(gameDisplay,(0,0,0),[440,510],[440,0])
        pygame.draw.line(gameDisplay,(0,0,0),[1000,510],[0,510])
        pygame.display.update()
        


pygame.quit()
quit()


        

        
