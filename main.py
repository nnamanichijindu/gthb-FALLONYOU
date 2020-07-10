import pygame
pygame.init()
gray=(119,118,110)
win_width=800
black = (0,0,0)
white = (255,255,255)
win_height=800
blue = (46, 206, 255)
bblue = (171, 228, 245)
vel=10
left = False
right = False
runcount = 0
width = 70
height = 90
import time
import random
pause=False
tc= (200,200,200)

gamewin = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Dakpo Mu Isi")
clock=pygame.time.Clock()
runRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
runLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.png')
niggaimg = pygame.image.load('standing.png')
L = pygame.image.load('edgeL.png')
R = pygame.image.load('edgeR.png')
intbg = pygame.image.load('intbg.png')
abtbg = pygame.image.load('abtbg.png')
woo = pygame.image.load('in.png')



def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamewin.blit(intbg,(0,0))
        gamewin.blit(woo, (150, 300))
        largetext=pygame.font.SysFont('comicsansms',80)
        TextSurf,TextRect=text_objects("FALL ON YOU",largetext)
        TextRect.center=(400,100)
        gamewin.blit(TextSurf,TextRect)
        button("START",550,470,150,50,blue,bblue,"play")
        button("QUIT",550,570,150,50,blue,bblue,"quit")
        button("ABOUT",550,670,150,50,blue,bblue,"about")
        pygame.display.update()
        clock.tick(60)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamewin,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
            elif action=="about":
                about()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamewin,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamewin.blit(textsurf,textrect)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            gamewin.blit(abtbg,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((win_width/2),(win_height/2))
            gamewin.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,blue,bblue,"unpause")
            button("RESTART",350,450,150,50,blue,bblue,"play")
            button("MAIN MENU",550,450,200,50,blue,bblue,"menu")
            pygame.display.update()
            clock.tick(60)
def unpaused():
    global pause
    pause = False

def about():
    about=True
    while about:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamewin.blit(abtbg,(0,0))
        largetext=pygame.font.SysFont('comicsansms.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("This game was built by Nnamani Chijindu Ikenna",smalltext)
        textRect.center=((400),(200))
        TextSurf,TextRect=text_objects("ABOUT",largetext)
        TextRect.center=((400),(100))
        gamewin.blit(TextSurf,TextRect)
        gamewin.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : RUN LEFT",smalltext)
        stextRect.center=((400),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RUN RIGHT" ,smalltext)
        hTextRect.center=((400),(450))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((400),(300))
        gamewin.blit(sTextSurf,sTextRect)
        gamewin.blit(stextSurf,stextRect)
        gamewin.blit(hTextSurf,hTextRect)
        button("BACK",325,550,150,50,blue,bblue,"menu")
        pygame.display.update()
        clock.tick(30)


def obstacle(obs_x, obs_y, obs):

    if obs == 0:
        obs_pic = pygame.image.load("lava.png")
    elif obs == 1:
        obs_pic = pygame.image.load("lava.png")
    elif obs == 2:
        obs_pic = pygame.image.load("lava.png")
    elif obs == 3:
        obs_pic = pygame.image.load("lava.png")
    elif obs == 4:
        obs_pic = pygame.image.load("lava.png")
    elif obs == 5:
        obs_pic = pygame.image.load("lava.png")
    elif obs == 6:
        obs_pic = pygame.image.load("lava.png")

    gamewin.blit(obs_pic, (obs_x, obs_y))

def scoresys(passed,score):
    font = pygame.font.SysFont(None, 25)
    score = font.render("Score" + str(score), True, tc)
    gamewin.blit(score, (4, 70))


def text_objects(text,font):
    textsurface=font.render(text, True, white)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((win_width/2),(win_height/2))
    gamewin.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def died():
    message_display("DEAD")

def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(win_width*0.45)
    y=(win_height*0.8)
    gamewin.blit(bg,(0,0))

    gamewin.blit(niggaimg,(x,y))
    score=font.render("SCORE: 0",True,tc)
    gamewin.blit(score,(0,30))
    button("PAUSE",650,0,150,50,blue,bblue,"pause")
def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("Ready!",largetext)
            TextRect.center=((win_width/2),(win_height/2))
            gamewin.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("Set!",largetext)
            TextRect.center=((win_width/2),(win_height/2))
            gamewin.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((win_width/2),(win_height/2))
            gamewin.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()


def game_loop():
    global pause
    pause=True
    x=(win_width*0.47)
    y=(win_height*0.85)
    vel=0
    width=70
    left=False
    right=False
    global runcount
    runcount = 0
    obs_speed = 9
    obs = 0
    obs_x = random.randrange(100, (win_width-100))
    obs_y = -950
    obs_width = 150
    obs_height = 50
    passed = 0
    level = 0
    score = 0


    hit = False
    while not hit:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    vel = -10
                    left = True
                    right = False
                elif event.key == pygame.K_RIGHT:
                    vel = 10
                    right = True
                    left = False
                else:
                    right = False
                    left = False
                    runcount = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    gamewin.blit(niggaimg, (x, y))
                    vel=0
                    runcount=0
                    right = False
                    left = False

        x+=vel
        gamewin.blit(bg, (0, 0))
        obs_y -= (obs_speed/4)
        obstacle(obs_x, obs_y, obs)
        obs_y += obs_speed
        if runcount + 1 >= 27:
            runcount = 0
        if left:
            gamewin.blit(runLeft[runcount // 3], (x, y))
            runcount += 1
        elif right:
            gamewin.blit(runRight[runcount // 3], (x, y))
            runcount += 1
        else:
            gamewin.blit(niggaimg, (x, y))
            runcount = 0
            vel = 0
        scoresys(passed,score)
        if x>win_width-30 or x<30:
            died()
        gamewin.blit(L, (0, 650))
        gamewin.blit(R, (750, 650))
        if obs_y>win_height:
            obs_y=0-obs_height
            obs_x=random.randrange(100,(win_width-100))
            obs=random.randrange(0,7)
            passed=passed+1
            score=passed*25
            if int(passed)%10==0:
                level=level+1
                obs_speed+2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL"+str(level), largetext)
                textrect.center = ((win_width / 2), (win_height / 2))
                gamewin.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)


        if y < obs_y + obs_height:
            if x > obs_x and x < obs_x + obs_width or x + width > obs_x and x + width < obs_x+obs_width:
                died()
        button("pause",650,0,150,50,blue,bblue,"pause")
        pygame.display.update()

intro_loop()
game_loop()
pygame.quit()
quit()

