import pygame, sys
from pygame.locals import *

MainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("64 KB")

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen_size = [1024,512]
Player_status = [0,0,0]
scene = "menu"
surf = pygame.Surface((256,128))

ex = 0
ey = 0

with open("Data.txt", "r", encoding="utf-8")as file:
    Data_t = file.readlines()
    scale = int(Data_t[4])
    lvl = int(Data_t[3])
    screen_size[0] = int(Data_t[0])
    screen_size[1] = int(Data_t[1])

temizlik = pygame.image.load("Sprites/n.png")
temizlik = pygame.transform.scale(temizlik,screen_size)

if int(Data_t[2]) == 1:
    screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)
    ex = (screen_size[0]) /2
    ey = (screen_size[1]) /2
else:
    screen = pygame.display.set_mode(monitor_size,pygame.FULLSCREEN)
    ex = (monitor_size[0]) /2
    ey = (monitor_size[1]) /2

kapak = pygame.image.load("kapak.png")
pygame.display.set_icon(kapak)


Player = pygame.image.load("Sprites/Player/Player.png")
Player = pygame.transform.scale(Player,(scale*16,scale*16))
Player_2 = pygame.transform.flip(Player, True, False)
Player_Run_delay = 100
P_Animnum = 0
time = pygame.time.get_ticks()
prect = Player.get_rect()

font = pygame.font.SysFont("None", 32)

Player_Run_1 = pygame.image.load("Sprites/Player/Player_Run_1.png")
Player_Run_2 = pygame.image.load("Sprites/Player/Player_Run_2.png")
Player_Run_3 = pygame.image.load("Sprites/Player/Player_Run_3.png")
Player_Run_4 = pygame.image.load("Sprites/Player/Player_Run_4.png")
Player_Run_1 = pygame.transform.scale(Player_Run_1,(scale*16,scale*16))
Player_Run_2 = pygame.transform.scale(Player_Run_2,(scale*16,scale*16))
Player_Run_3 = pygame.transform.scale(Player_Run_3,(scale*16,scale*16))
Player_Run_4 = pygame.transform.scale(Player_Run_4,(scale*16,scale*16))
Player_Run_list = [Player_Run_1,Player_Run_2,Player_Run_3,Player_Run_4]
Player_Run_1 = pygame.transform.flip(Player_Run_1,True,False)
Player_Run_2 = pygame.transform.flip(Player_Run_2,True,False)
Player_Run_3 = pygame.transform.flip(Player_Run_3,True,False)
Player_Run_4 = pygame.transform.flip(Player_Run_4,True,False)
Player_Run_2_list = [Player_Run_1,Player_Run_2,Player_Run_3,Player_Run_4]
Player_Jump = pygame.image.load("Sprites/Player/Player_Jump.png")
Player_Jump = pygame.transform.scale(Player_Jump,(scale*16,scale*16))
Player_Jump_2 = pygame.transform.flip(Player_Jump,True,False)

space = 0

mp_0_0 = pygame.image.load("sprites/map/basamak.png")
mp_0_0 = pygame.transform.scale(mp_0_0,(scale*16,scale*16))
mp_0_1 = pygame.transform.flip(mp_0_0,1,0)
mp_0_2 = pygame.transform.flip(mp_0_1,1,1)
mp_0_3 = pygame.transform.flip(mp_0_2,1,0)

mp_1 = pygame.image.load("sprites/map/duvar_1.png")
mp_1 = pygame.transform.scale(mp_1,(scale*16,scale*16))

mp_2_0 = pygame.image.load("sprites/map/duvar_2.png")
mp_2_0 = pygame.transform.scale(mp_2_0,(scale*16,scale*16))
mp_2_1 = pygame.transform.flip(mp_2_0,1,0)
mp_2_2 = pygame.transform.rotate(mp_2_1,90)
mp_2_3 = pygame.transform.flip(mp_2_2,0,1)

mp_3_0 = pygame.image.load("sprites/map/duvar_3.png")
mp_3_0 = pygame.transform.scale(mp_3_0,(scale*16,scale*16))
mp_3_1 = pygame.transform.rotate(mp_3_0,90)

mp_4_0 = pygame.image.load("sprites/map/duvar_4.png")
mp_4_0 = pygame.transform.scale(mp_4_0,(scale*16,scale*16))
mp_4_1 = pygame.transform.flip(mp_4_0,1,0)
mp_4_2 = pygame.transform.flip(mp_4_1,1,1)
mp_4_3 = pygame.transform.flip(mp_4_2,1,0)

mp_5_0 = pygame.image.load("sprites/map/duvar_5.png")
mp_5_0 = pygame.transform.scale(mp_5_0,(scale*16,scale*16))
mp_5_1 = pygame.transform.flip(mp_5_0,1,0)
mp_5_2 = pygame.transform.flip(mp_5_0,1,1)
mp_5_3 = pygame.transform.flip(mp_5_0,0,1)

mp_6_1 = pygame.image.load("sprites/map/sandık_1.png")
mp_6_1 = pygame.transform.scale(mp_6_1,(scale*16,scale*16))
mp_6_2 = pygame.image.load("sprites/map/sandık_2.png")
mp_6_2 = pygame.transform.scale(mp_6_2,(scale*16,scale*16))

mp_7_1 = pygame.image.load("sprites/map/hedef.png")
mp_7_1 = pygame.transform.scale(mp_7_1,(scale*16,scale*16))

mp_6_ls = [mp_6_1,mp_6_2]
mp_6_nm = 0
mp_list = [0,mp_0_0,mp_0_1,mp_0_2,mp_0_3,mp_1,mp_2_0,mp_2_1,mp_2_2,mp_2_3,mp_3_0,mp_3_1,mp_4_0,mp_4_1,mp_4_2,mp_4_3,mp_5_0,mp_5_1,mp_5_2,mp_5_3,mp_6_ls[mp_6_nm],mp_7_1]

lvl_1_map = [[14, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15], [11, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11], [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11], [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 9], [11, 0, 0, 1, 6, 10, 10, 10, 7, 0, 6, 7, 0, 0, 0, 21], [11, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8], [11, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11], [12, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 13]]
msmxy = [0,0]
blck = 1

mpbl = []

while True:
    screen.fill((255,255,255))
    key = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            screen_size = [screen.get_width(),screen.get_height()]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LSHIFT:
                if Player_status[0] == 0:
                    prect.x += 64*scale
                else:
                    prect.x -= 64*scale
            if event.key == K_SPACE:
                space = 1
            else:
                space = 0
    
    if scene == "menu":
        screen.fill((30,30,70))
        text = font.render("64 KB",True,(255,255,255))
        screen.blit(text,(screen_size[0]//2-text.get_width()//2,0))
        text = font.render("PRESS SPACE TO PLAY",True,(255,255,255))
        screen.blit(text,(screen_size[0]//2-text.get_width()//2,screen_size[1]-text.get_height()))
        if space == 1:
            scene = "game"
            if lvl == 1:
                mpbltsr = [15,7]
                mpbltxy = [15*scale*16,7*scale*16]
                while mpbltsr[1]>=0:
                    while mpbltsr[0]>=0:
                        if lvl_1_map[mpbltsr[1]][mpbltsr[0]] == -1:
                            prect.x = mpbltxy[0]
                            prect.y = mpbltxy[1]
                        mpbltsr[0] -=1
                        mpbltxy[0] -= scale*16
                    if mpbltsr[0] == -1:
                        mpbltsr[1] -=1
                        mpbltsr[0] = 15
                        mpbltxy[0] = 15*scale*16
                        mpbltxy[1] -= scale*16
    
    elif scene == "game":
        surf.fill((0,0,0))
        if lvl == 1:
            mpbltsr = [15,7]
            mpbltxy = [15*scale*16,7*scale*16]
            mpbl = []
            while mpbltsr[1]>=0:
                while mpbltsr[0]>=0:
                    if lvl_1_map[mpbltsr[1]][mpbltsr[0]] != 0 and lvl_1_map[mpbltsr[1]][mpbltsr[0]] != -1:
                        surf.blit(mp_list[lvl_1_map[mpbltsr[1]][mpbltsr[0]]],mpbltxy)
                        #print(mpbltxy)
                        mpbl.append([mpbltxy[0],mpbltxy[1]])
                    mpbltsr[0] -=1
                    mpbltxy[0] -= scale*16
                if mpbltsr[0] == -1:
                    mpbltsr[1] -=1
                    mpbltsr[0] = 15
                    mpbltxy[0] = 15*scale*16
                    mpbltxy[1] -= scale*16
            if key[pygame.K_d]:
                Player_status[0] = 0
                Player_status[1] = 1
            if key[pygame.K_w]:
                
                if Player_status[2] != 1:
                    Player_status[2] = 1
            if key[pygame.K_a]:

                Player_status[0] = 1
                Player_status[1] = 1
            if key[pygame.K_a] + key[pygame.K_d] == 0:
                Player_status[1] = 0
            if key[pygame.K_w] == 0:
                Player_status[2] = 0
            if Player_status[1] == 1:
                if pygame.time.get_ticks() - time > Player_Run_delay:
                    P_Animnum += 1
                    if P_Animnum > 3:
                        P_Animnum = 0
                    time = pygame.time.get_ticks()
            if Player_status[0] == 1 and Player_status[1] == 1:
                if pygame.time.get_ticks() - time > Player_Run_delay:
                    P_Animnum += 1
                    if P_Animnum > 3:
                        P_Animnum = 0
                    time = pygame.time.get_ticks()
            if Player_status[2] == 1:
                #prect.y += scale*2
                pass
            sira = len(mpbl)
            sira -=1
            if key[pygame.K_e]:
                lvl = 2
            if key[pygame.K_w]:
                prect.y -= 2
            if key[pygame.K_s]:
                pass
            if key[pygame.K_a]:
                prect.x -= 2
            if key[pygame.K_d]:
                prect.x += 2
            prect.y += 2
            if prect.y+32 > 128:
                prect.y -= 4
            if prect.x < 16:
                prect.x += 4
            if prect.y == 96:
                if prect.x > 256-32:
                    prect.x -= 4
            if prect.x == 16:
                if prect.y > 84:
                    prect.y-= 4
            if prect.x > 16 and prect.x <20:
                if prect.y > 80:
                    prect.y-= 4
            if prect.x > 20 and prect.x <24:
                if prect.y > 76:
                    prect.y-= 4
            if prect.x > 24 and prect.x <28:
                if prect.y > 72:
                    prect.y-= 4
            if prect.x > 28 and prect.x <32:
                if prect.y > 68:
                    prect.y-= 4
            if prect.x > 32 and prect.x <36:
                if prect.y > 64:
                    prect.y-= 4
            if prect.x > 36 and prect.x <40:
                if prect.y > 60:
                    prect.y-= 4
            if prect.x > 40 and prect.x <44:
                if prect.y > 56:
                    prect.y-= 4
            if prect.x > 44 and prect.x <48:
                if prect.y > 52:
                    prect.y-= 4
            if prect.x > 48 and prect.x <52:
                if prect.y > 48:
                    prect.y-= 4
            if prect.x > 52 and prect.x <56:
                if prect.y > 44:
                    prect.y-= 4
            if prect.x > 56 and prect.x <60:
                if prect.y > 40:
                    prect.y-= 4
            if prect.x > 60 and prect.x <64:
                if prect.y > 36:
                    prect.y-= 4
            if prect.x > 64 and prect.x <68:
                if prect.y > 32:
                    prect.y-= 4
            print(prect.x,prect.y)
            if Player_status[0] == 0:
                if Player_status[1] + Player_status[2] == 0:
                    surf.blit(Player,prect)
                if Player_status[1] == 1 and Player_status[2] == 0:
                    surf.blit(Player_Run_list[P_Animnum],prect)
                if Player_status[2] == 1:
                    surf.blit(Player_Jump,prect)
            else:
                if Player_status[1] + Player_status[2] == 0: 
                    surf.blit(Player_2,prect)
                if Player_status[1] == 1 and Player_status[2] == 0:
                    surf.blit(Player_Run_2_list[P_Animnum],prect)
                if Player_status[2] == 1:
                    surf.blit(Player_Jump_2,prect)
            screen.blit(pygame.transform.scale(surf,screen_size),(0,0))
        if lvl == 2:
            screen.fill((30,30,70))
            text = font.render("OYUN BİTTİ",True,(255,255,255))
            screen.blit(text,(screen_size[0]//2-text.get_width()//2,0))
            text = font.render("OYNADIĞINIZ İÇİN TEŞEKKÜRLER",True,(255,255,255))
            screen.blit(text,(screen_size[0]//2-text.get_width()//2,screen_size[1]//2-text.get_height()//2))
            text = font.render("OYUNA YENİ BÖLÜMLER EKLERSEM DİSCORD'DAN HABER VERİRM",True,(255,255,255))
            screen.blit(text,(screen_size[0]//2-text.get_width()//2,screen_size[1]-text.get_height()))
            if space == 1:
                scene = "game"
                if lvl == 1:
                    mpbltsr = [15,7]
                    mpbltxy = [15*scale*16,7*scale*16]
                    while mpbltsr[1]>=0:
                        while mpbltsr[0]>=0:
                            if lvl_1_map[mpbltsr[1]][mpbltsr[0]] == -1:
                                prect.x = mpbltxy[0]
                                prect.y = mpbltxy[1]
                            mpbltsr[0] -=1
                            mpbltxy[0] -= scale*16
                        if mpbltsr[0] == -1:
                            mpbltsr[1] -=1
                            mpbltsr[0] = 15
                            mpbltxy[0] = 15*scale*16
                            mpbltxy[1] -= scale*16
    MainClock.tick(60)
    pygame.display.update()