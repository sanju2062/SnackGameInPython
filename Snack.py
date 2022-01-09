"""-------------------------Snack game----------------------------"""
import random
from pygame.locals import *
import pygame

red = (255, 0, 0)
white = (255, 255, 255)
screenwidth = 544
screenheight = 400
screen = pygame.display.set_mode((screenwidth,screenheight))
game_sprites = {}
game_sound = {}
FPS = 30
game_over = False

sanju = input()
pygame.display.update()

PLAYER = "images//images.png"
def highscore(score):
    with open("HighScore\\highscore.txt","r") as f:
        a = f.read()
    if int(a)< score:
        with open("HighScore\\highscore.txt", "w") as f:
            f.write(f"{score}")

    screen.blit(pygame.font.SysFont(None, 30).render(f"High Score : {a}", True, red), [150,10])

def snackdisplay(image, snk_list):
    for x,y in snk_list:
        screen.blit(image, (x,y))

def iscollide(playerx,playery,snk_list,snk_lnt,head):

    if playery>=screenheight-5 or playerx>=screenwidth-5 or playerx <= -4 or playery<= -4:
        game_sound['hit'].play()
        game_over = True
        # print("12")
        # pygame.quit()
        game_end()
    if (head in snk_list[:-1]) and len(snk_list)>3:
        game_sound['hit'].play()
        game_over = True
        # print("12")
        # pygame.quit()
        game_end()



def welcomescreen():
    """ Display a welcome screen """
    playerx = int(screenwidth/5)
    playery = int((screenheight-game_sprites['player'].get_height())/2)
    messagex = 0
    messagey = 0
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
            elif event.type==KEYDOWN and (event.key==K_SPACE ):
                return
            else:
                # screen.blit(game_sprites['player'], (playerx,playery))
                screen.blit(game_sprites['message'], (0, 0))
                # screen.blit(game_sprites['player'], (playerx,playery))
                screen.blit(pygame.font.SysFont(None,40).render("Press Space to Start",True,red),[150,350])
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def maingame():
    playervelx = 0
    playervely = 0
    snk_lnt = 1
    foodx = random.randint(10, screenwidth - 10)
    foody = random.randint(10, screenheight - 10)
    global score
    score = 0
    snk_list = []

    playerx = int(screenwidth / 5)
    playery = int((screenheight - game_sprites['player'].get_height()) / 2)
    while not game_over:
        if game_over==True:
            print("game over")
            game_end()
        else:
            for event in pygame.event.get():
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.quit()
                if event.type==KEYDOWN and event.key==K_UP:
                    playervelx = 0
                    playervely = -5
                if event.type==KEYDOWN and event.key == K_DOWN:
                    playervelx = 0
                    playervely = 5
                if event.type==KEYDOWN and event.key == K_RIGHT:
                    playervelx = 5
                    playervely = 0
                if event.type==KEYDOWN and event.key == K_LEFT:
                    playervelx = -5
                    playervely = 0
            if abs(playerx - foodx) < 6 and abs(playery - foody) < 6:
                score += 1
                foodx = random.randint(10, screenwidth - 10)
                foody = random.randint(10, screenheight - 10)
                # print("score :", score)
                snk_lnt+=4
                game_sound['point'].play()

            if len(snk_list)>snk_lnt:
                del snk_list[0]

        playerx += playervelx
        playery += playervely

        screen.blit(game_sprites['background'], (0, 0))
        snackdisplay(game_sprites['player'], snk_list)
        screen.blit(pygame.font.SysFont(None, 30).render(f"Score : {score}", True, red), [10,10])
        pygame.draw.rect(screen , red ,[ foodx, foody, 11,11])
        head=[]
        head.append(playerx)
        head.append(playery)
        snk_list.append(head)
        iscollide(playerx, playery, snk_list, snk_lnt, head)
        highscore(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)
def game_end():
    # print("sanju")
    # snk_lnt=1
    # snk_list=[]
    # head=[]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT :
                pygame.quit()
            if event.type==KEYDOWN and event.key==K_SPACE:
                maingame()

        screen.fill(white)
        screen.blit(pygame.font.SysFont(None, 30).render("Game Over!", True, red),[120, 180])
        screen.blit(pygame.font.SysFont(None, 30).render(f"Your Score :{score}", True, red),[120, 200])
        screen.blit(pygame.font.SysFont(None, 30).render("Press space to Play again", True, red),[120, 220])
        pygame.display.update()
        FPSCLOCK.tick(FPS)
if __name__ == '__main__':
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    pygame.display.set_caption("Snack Game by sanju")
    game_sound["point"] = pygame.mixer.Sound(r"audio\point.wav")
    game_sound["hit"] = pygame.mixer.Sound(r"audio\hit.wav")

    game_sprites['player']=pygame.image.load(PLAYER).convert_alpha()
    game_sprites['message']=pygame.image.load('images//images (2).jpeg').convert_alpha()
    game_sprites['background']=pygame.image.load('images//background.png').convert_alpha()
    welcomescreen()
    maingame()
    # game_end()
