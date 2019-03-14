import pygame
import random
import socket
from tkinter import *
def client(E1):
	top.destroy()
	##########################################
	host = E1
	port = 3000
	client_socket = socket.socket()
	client_socket.connect((host, port))
	##########################################

	pygame.init()
	gamedisplay = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Online Pygame")

	clock = pygame.time.Clock()  
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
	y=int(0)
	x_change=0
	ballx_change = 1
	bally_change = ballx_change

	while not crashed:
		gamedisplay.fill((255,255,255))
		gamedisplay.blit(bluebar,(x-100,0))
		gamedisplay.blit(ball,(ballx,bally))
		opponentx = client_socket.recv(1024).decode() 
		if not opponentx:
			break
		gamedisplay.blit(redbar,(int(opponentx),580))
		data=str(x-100)
		client_socket.send(data.encode())

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
		if bally >= 580 and bally <= 600:
			if int(opponentx)<= ballx and ballx <= int(opponentx)+200:
				bally_change = -(bally_change)
				if bally_change<0:
					bally_change -= 1
				else:
					bally_change +=1
			else:
				root = Tk()
				text = Text(root)
				text.insert(INSERT, "You Win !!!!!")
				text.pack()
				root.title("Result")
				root.mainloop()
				print("You Win !!!!")
				break
		if bally <= 20:
			if x-100 <= ballx and x-100+200 > ballx:
				bally_change = -(bally_change)
				if bally_change<0:
					bally_change -= 1
				else:
					bally_change +=1
			else:
				root = Tk()
				text = Text(root)
				text.insert(INSERT, "You Lose !!!!!")
				text.pack()
				root.title("Result")
				root.mainloop()
				print("You Lose !!!!")
				break


		pygame.display.update()
		clock.tick(60)   # 60 fps
	print("Game made by N.C.Mohit , Thanks for playing !! :D")
	pygame.quit()
	client_socket.close()
	quit()
def server():
	print("Game made by N.C.Mohit , Enjoy !!!!!")
	top.destroy()
	###########################################
	host = ''
	port = 3000
	server_socket = socket.socket() 
	server_socket.bind((host, port))
	print("Waiting for client connection . . . ")
	server_socket.listen(2)
	conn, address = server_socket.accept() 
	###########################################

	pygame.init()
	gamedisplay = pygame.display.set_mode((800,600))
	pygame.display.set_caption("OnlinePyGame")

	clock = pygame.time.Clock()  
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
	y=int(580)
	ballx_change = 1
	bally_change = ballx_change

	while not crashed:
		gamedisplay.fill((255,255,255))
		gamedisplay.blit(redbar,(x-100,580))
		gamedisplay.blit(ball,(ballx,bally))
		data = str(x-100)
		conn.send(data.encode())
		opponentx = conn.recv(1024).decode()
		if not opponentx:
			break 
		gamedisplay.blit(bluebar,(int(opponentx),0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		x,y = pygame.mouse.get_pos()
		if x -100< 0 :
			x =100
		elif x-100>600:
			x=700
		ballx+=ballx_change
		bally+=bally_change
		if ballx >= 800:
			ballx_change = -(ballx_change)
			ballx_change -= 1
		elif ballx <= 0:
			ballx_change = -(ballx_change)
			ballx_change += 1
		if bally >= 580 and bally <= 600:
			if x-100<= ballx and ballx <= x-100+200:
				bally_change = -(bally_change)
				if bally_change<0:
					bally_change -= 1
				else:
					bally_change +=1
			else:
				root = Tk()
				text = Text(root)
				text.insert(INSERT, "You Lose !!!!!")
				text.pack()
				root.title("Result")
				root.mainloop()
				print("You Lose !!!!")
				break
		if bally <= 20:
			if int(opponentx) <= ballx and int(opponentx)+200 > ballx: 
				bally_change = -(bally_change)
				if bally_change<0:
					bally_change -= 1
				else:
					bally_change +=1
			else:
				root = Tk()
				text = Text(root)
				text.insert(INSERT, "You Win !!!!!")
				text.pack()
				root.title("Result")
				root.mainloop()
				print("You Win !!!!")
				break

		pygame.display.update()
		clock.tick(60)   # 60 fps
	pygame.quit()
	conn.close()
	quit()
top = Tk()
text = Text(top)
text.insert(INSERT, "What would you like to do ?\n\n\n(To get a server's IPv4 type 'ipconfig' in cmd in the server host PC)")
text.pack()
def run_client():
	global E1
	L1 = Label(top, text="Enter Server's IPv4")
	L1.pack( side = LEFT)
	E1 = Entry(top, bd =5)
	E1.pack(side = RIGHT)
def run_server():
	server()
def join():
	client(E1.get())
B = Button(top, text ="Create Server", command = run_server)
C= Button(top,text="Enter Server",command = run_client)
D = Button(top,text="Join",command = join)

B.pack()
C.pack()
D.pack()
top.title("OnlinePyGame")
top.mainloop()	
