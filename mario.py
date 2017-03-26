import pygame, random, sys
from pygame.locals import *
pygame.init()
width=1200
height=600
blue = (0,0,255)
black = (0,0,0)


#fontrect=font.get_rect()
fps=25
level=0
addnewflame=20

class dragonn:
    up=False
    down=True
    v_dragon=15
    
    def __init__(self):
        self.dragon=pygame.image.load('dragon.png')
        self.dragonrect=self.dragon.get_rect()
        self.dragonrect.centerx=width-25
        self.dragonrect.centery=height/2
    def update(self):
        if(self.dragonrect.top<cactusrect.bottom):
            self.up=False
            self.down=True
        if(self.dragonrect.bottom>firerect.top):
            self.up=True
            self.down=False
        if(self.up):
            self.dragonrect.top-=self.v_dragon
        if(self.down):
            self.dragonrect.bottom+=self.v_dragon
        canvas.blit(self.dragon,self.dragonrect)
    def return_height(self):
        height=self.dragonrect.top
        return height


class flamess:
    v_flames=20
    def __init__(self):
        self.flames=pygame.image.load('flames.png')
        self.flamesrect=self.flames.get_rect()
        self.height=dragonobj.return_height()
        self.surface=pygame.transform.scale(self.flames,(20,20))
        self.flamesrect = pygame.Rect(width-110, self.height, 20, 20)
    def update(self):
        self.flamesrect.left-=self.v_flames
    def collision(self):
        if(self.flamesrect.left==0):
            return True
        else:
            return False
class mario:
    global moveup,movedown,gravity,cactusrect,firerect
    speed=10
    downspeed=20
    
    def __init__(self):
        self.mario=pygame.image.load('mario.png')
        self.mariorect=self.mario.get_rect()
        self.mariorect.centerx=50
        self.mariorect.centery=height/2
        self.score=0

    def update(self):
        if(moveup and (self.mariorect.top>cactusrect.bottom)):
            self.mariorect.top-=self.speed
            self.score+=1
        if(movedown and (self.mariorect.bottom<firerect.top)):
            self.mariorect.bottom+=self.downspeed
            self.score+=1
        if(gravity and (self.mariorect.bottom<firerect.top)):
            self.mariorect.bottom+=self.speed

"""class queen:
    v_queen=10
    def __init__(self):
        self.m_queen=pygame.image.load('mario_queen.png')
        self.m_queenrect=self.m_queen.get_rect()
        self.m_queenrect.centerx=width
        self.m_queenrect.centery=height/2
    def update(self):
        self.m_queenrect.left-=self.v_queen
    def queenmeetsmario(self):
        if(player.mariorect.right==self.m_queenrect.left):
            return True
        else:
            return False
"""    
def terminate():
    pygame.quit()
    sys.exit()

def waitforkey():
    while True:
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                terminate()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_ESCAPE):
                    terminate()
                return

def flamehitsmario(playerrect,flamess):
    for f in flame_list:
        if playerrect.colliderect(f.flamesrect):
            return True
        return False

def drawtext(text,font,surface,x,y):
    textobj=font.render(text,1,(0,255,255))
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def check_level(score):
    global height,level,cactusrect,firerect
    if(score in range(0,250)):
        cactusrect.bottom=50
        firerect.top=height-50
        level=1
    elif(score in range(250,500)):
        cactusrect.bottom=100
        firerect.top=height-100
        level=2
    elif(score in range(500,750)):
        cactusrect.bottom=150
        firerect.top=height-150
        level=3
    elif(score in range(750,1000)):
        cactusrect.bottom=200
        firerect.top=height-200
        level=4
    """else:
        player.mariorect.centerx=50
        player.mariorect.centery=height/2
        queenobj=queen()
        queenobj.update()
        pygame.display.update()
        canvas.blit(queenobj.m_queen,queenobj.m_queenrect)
        if(queenobj.queenmeetsmario()):
            drawtext('Score',font,canvas,width/2,height/2)
    """
        

def load_image(imagename):
    return image

mainClock=pygame.time.Clock()                         
canvas=pygame.display.set_mode((width,height))
pygame.display.set_caption('MARIO')

font=pygame.font.SysFont(None, 48)
scorefont=pygame.font.SysFont(None,28)




cactus=pygame.image.load('cactus.png')
fire=pygame.image.load('fire.png')
cactusrect=cactus.get_rect()
firerect=fire.get_rect()
startimage=pygame.image.load('start.png')
startimagerect=startimage.get_rect()
startimagerect.centerx=width/2
startimagerect.centery=height/2
endimage=pygame.image.load('end.png')
endimagerect=endimage.get_rect()
endimagerect.centerx=width/2
endimagerect.centery=height/2

pygame.mixer.music.load('mario_theme.wav')
gameover=pygame.mixer.Sound('mario_dies.wav')

drawtext('Mario',font,canvas,(width/3),(height/3))
canvas.blit(startimage,startimagerect)
pygame.display.update()

waitforkey()
topscore=0
dragonobj=dragonn()

while True:
    flame_list=[]
    player=mario()
    moveup=movedown=gravity=False
    flameaddcounter=0
    gameover.stop()
    pygame.mixer.music.play(-1,0.0)

    while True:
        for event in pygame.event.get():
            if(event.type==QUIT):
                terminate()
            if(event.type==KEYDOWN):
                if(event.key==K_UP):
                    moveup=True
                    movedown=False
                    gravity=False
                if(event.key==K_DOWN):
                    movedown=True
                    gravity=False
                    moveup=False
                
            if(event.type==KEYUP):
                if(event.key==K_UP):
                    moveup=False
                    gravity=True
                if(event.key==K_DOWN):
                    movedown=True
                    gravity=True
                if(event.key==K_ESCAPE):
                    terminate()
        flameaddcounter+=1
        check_level(player.score)
        if(flameaddcounter==addnewflame):
            flameaddcounter=0
            newflame=flamess()
            flame_list.append(newflame)

        for f in flame_list:
            flamess.update(f)
        for f in flame_list:
            if(f.flamesrect.left<=0):
                flame_list.remove(f)

        player.update()
        dragonobj.update()
        canvas.fill(black)
        canvas.blit(fire,firerect)
        canvas.blit(cactus,cactusrect)
        canvas.blit(player.mario,player.mariorect)
        canvas.blit(dragonobj.dragon,dragonobj.dragonrect)

        drawtext('Score : %s | Top score : %s | Level : %s' %(player.score, topscore, level), scorefont, canvas, 350, cactusrect.bottom + 10)
        for f in flame_list:
            canvas.blit(f.surface, f.flamesrect)
        if(flamehitsmario(player.mariorect, flame_list)):
            if player.score > topscore:
                topscore = player.score
            break
        if ((player.mariorect.top <= cactusrect.bottom) or (player.mariorect.bottom >= firerect.top)):
            if player.score > topscore:
                topscore = player.score
            break

        pygame.display.update()
        mainClock.tick(fps)
    pygame.mixer.music.stop()
    gameover.play()
    canvas.blit(endimage, endimagerect)
    pygame.display.update()
    waitforkey()
