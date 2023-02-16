import pygame,sys,os,random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("parkur oyunu")
screen_size = [1024,512]
screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE,32)
scale = 4

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

mp_6_ls = [mp_6_1,mp_6_2]
mp_6_nm = 0
mp_list = [0,mp_0_0,mp_0_1,mp_0_2,mp_0_3,mp_1,mp_2_0,mp_2_1,mp_2_2,mp_2_3,mp_3_0,mp_3_1,mp_4_0,mp_4_1,mp_4_2,mp_4_3,mp_5_0,mp_5_1,mp_5_2,mp_5_3,mp_6_ls[mp_6_nm]]
time = pygame.time.get_ticks()

fps = 360

scrsz = [int(screen_size[0]//(scale*16)),int(screen_size[1]//(scale*16))]
x,y = 0,0

lvl_1_map = [[14, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 15], [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11], [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11], [11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 9], [11, 0, 0, 1, 6, 10, 10, 10, 7, 0, 6, 7, 0, 0, 0, 0], [11, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8], [11, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11], [12, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 13]]
msmxy = [0,0]
blck = 1

ctrli = 0
sc = 0

mrect = pygame.Rect(0,0,1,1)

while True:
    screen.fill((0,0,0))
    mx,my = pygame.mouse.get_pos()
    mrect.x,mrect.y = mx,my



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            screen_size = [screen.get_width(),screen.get_height()]
            scrsz = [int(screen_size[0]//(scale*16)),int(screen_size[1]//(scale*16))]
        if event.type == MOUSEBUTTONDOWN:
            if sc == 0:
                if event.button == 1:
                    lvl_1_map[msmxy[1]][msmxy[0]] = blck
                elif event.button == 3:
                    lvl_1_map[msmxy[1]][msmxy[0]] = 0
                elif event.button == 2:
                    blck += 1
                    if blck > len(mp_list)-1:
                        blck = 0
            else:
                if event.button == 1:
                    pass
            if ctrli == 1:
                if event.button == 4:
                    if scale < 16:
                        scale += 1
                        #relomap()
                elif event.button == 5:
                    if scale > 1:
                        scale -= 1
                        #relomap()
            else:
                if event.button == 4:
                    blck+=1
                    if blck > len(mp_list)-1:
                        blck = 1
                elif event.button == 5:
                    blck-=1
                    if blck == 0:
                        blck = len(mp_list)-1
        if event.type == KEYDOWN:
            if event.key == pygame.K_p:
                print(lvl_1_map)
            if event.key == pygame.K_LCTRL:
                ctrli = 1
            if event.key == pygame.K_f:
                screen = pygame.display.set_mode(screen_size,pygame.FULLSCREEN)
        if event.type == KEYUP:
            if event.key == pygame.K_LCTRL:
                ctrli = 0

    mpbltsr = [15,7]
    mpbltxy = [15*scale*16,7*scale*16]
    while mpbltsr[1]>=0:
        while mpbltsr[0]>=0:
            if lvl_1_map[mpbltsr[1]][mpbltsr[0]] != 0:
                screen.blit(pygame.transform.scale(mp_list[lvl_1_map[mpbltsr[1]][mpbltsr[0]]],(16*scale,16*scale)),mpbltxy)
            mpbltsr[0] -=1
            mpbltxy[0] -= scale*16
        if mpbltsr[0] == -1:
            mpbltsr[1] -=1
            mpbltsr[0] = 15
            mpbltxy[0] = 15*scale*16
            mpbltxy[1] -= scale*16

    msmxy = [mx//(scale*16),my//(scale*16)]
    msp = pygame.Surface((scale*16,scale*16),pygame.SRCALPHA)
    msp.blit(pygame.transform.scale(mp_list[blck],(scale*16,scale*16)),(0,0))
    msp.set_alpha(96)
    screen.blit(msp,(msmxy[0]*scale*16,msmxy[1]*scale*16))
    pygame.draw.rect(screen,(255,255,255),(msmxy[0]*scale*16,msmxy[1]*scale*16,16*scale,16*scale),1)

    pygame.draw.rect(screen,(255,255,255),(0,0,256*scale,128*scale),2)
    if mx > 256*scale or my > 128*scale:
        sc = 1
    else:
        sc = 0
    clock.tick(fps)
    pygame.display.update()