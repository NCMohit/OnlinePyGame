import pygame
pygame.init()
gamedisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Online Pygame")

clock = pygame.time.Clock()  
background = pygame.image.load('tennis.jpg')
redbar = pygame.image.load('redbar.png')
bluebar = pygame.image.load('bluebar.png')
ball = pygame.image.load('ball.png')
	#pygame.mixer.music.load('resources/music2.mp3')
	#pygame.mixer.music.play(-1, 0.0)
	#pygame.mixer.music.set_volume(0.25)

ballx=int(800/2)
bally=int(600/2)

crashed = False
x=int(800/2)+100
opponentx=int(800/2)+100
y=int(0)
x_change=0
level = 1
ballx_change = int(level)
bally_change = ballx_change

while not crashed:
	gamedisplay.fill((255,255,255))
	gamedisplay.blit(background,(0,0))
	gamedisplay.blit(bluebar,(x-100,0))
	gamedisplay.blit(ball,(ballx,bally))
	gamedisplay.blit(redbar,(int(opponentx),580))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				quit()
	x,y = pygame.mouse.get_pos()
	if x -100< 0 :
		x=100
	elif x-100>600:
		x=700
	ballx+=ballx_change
	bally+=bally_change
	if ballx >= 800:
		ballx_change = -(ballx_change)
		ballx_change -= 1
	elif ballx <= 0:
		ballx_change = -(ballx_change)
		ballx_change +=1
	if ballx < opponentx+100 and opponentx>200:
		if ballx_change<0:
			opponentx_change = ballx_change-3
		else:
			opponentx_change = -(ballx_change+3)
	elif ballx > opponentx+200 and opponentx<600:
		if ballx_change<0:
			opponentx_change = -(ballx_change-3)
		else:
			opponentx_change = ballx_change+3
	opponentx+=opponentx_change
	if bally >= 560 and bally <= 600:
		if int(opponentx)<= ballx and ballx <= int(opponentx)+200:
			bally_change = -(bally_change)
			if bally_change<0:
				bally_change -= 1
			else:
				bally_change +=1
		else:
			print("You Win !!")
			break
	if bally <= 20:
		if x-100 <= ballx and x-100+200 > ballx:
			bally_change = -(bally_change)
			if bally_change<0:
				bally_change -= 1
			else:
				bally_change +=1
		else:
			print("You Lose !!!!")
			break


	pygame.display.update()
	clock.tick(60)   # 60 fps
print("Game made by N.C.Mohit , Thanks for playing !! :D")
quit()


