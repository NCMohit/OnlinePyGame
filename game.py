import pygame
import random
pygame.init()
gamedisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Test Game")

clock = pygame.time.Clock()  
bar = pygame.image.load('bar.png')
ball = pygame.image.load('ball.png')

ballx=int(1366/2)
bally=int(768/2)
def ball_check(ballx,bally):
	if bally < 0:
		lose = True

crashed = False
x=int(1366/2)
y=int(748)
x_change=0
ballx_change = random.randint(4,7)
bally_change = ballx_change

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:	
                x_change = -5
            elif event.key == pygame.K_RIGHT:
            	x_change = 5
            if event.key == pygame.K_q:
            	pygame.quit()
            	quit()
    x+=x_change
    if x < 0 or x > 1166:
    	x_change=0
    ballx+=ballx_change
    bally+=bally_change
    if ballx >= 1366:
    	ballx_change = -(ballx_change)
    elif ballx <= 0:
    	ballx_change = -(ballx_change)
    if bally >= 748:
    	if x<= ballx and ballx <= x+200:
    		bally_change = -(bally_change)
    if bally <= 0:
   		bally_change = -(bally_change)
   		if ballx_change<0:
   			ballx_change-=1
   		else:
   			ballx_change+=1
    gamedisplay.fill((255,255,255))
    gamedisplay.blit(bar,(x,y))
    gamedisplay.blit(ball,(ballx,bally))



    pygame.display.update()
    clock.tick(60)   # 60 fps
pygame.quit()
quit()	