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
	y=int(0)
	x_change=0
	level = client_socket.recv(1024).decode()
	ballx_change = int(level)
	bally_change = ballx_change

	while not crashed:
		gamedisplay.fill((255,255,255))
		gamedisplay.blit(background,(0,0))
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
		if bally >= 560 and bally <= 600:
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

def server(level):
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
	y=int(580)
	ballx_change = int(level)
	bally_change = ballx_change
	data = level
	conn.send(data.encode())

	while not crashed:
		gamedisplay.fill((255,255,255))
		gamedisplay.blit(background,(0,0))
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
		if bally >= 560 and bally <= 600:
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

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

clientrunned = 0
serverrunned = 0

def run_client():
	global clientrunned
	global serverrunned
	if clientrunned == 0 and serverrunned == 0:
		global E1
		global top
		ei = Label(top, text = "Enter Ip address please \n\n\n\n\n\n\n\n")
		ei.pack()
		L1 = Label(top, text="Enter Server's IPv4")
		L1.pack()
		E1 = Entry(top, bd =5)
		E1.pack()
		D = Button(top,text="Join",command = join)
		D.pack()
		F = Button(top,text="Cancel",command = cleanup)
		F.pack()
		clientrunned = 1

def runserver():
	global blah
	global E2
	blah.destroy()
	server(E2.get())

def run_server():
	global blah
	global E2
	if E2.get()=='':
		root = Tk()
		text = Text(root)
		text.insert(INSERT,"You did not enter Hardness")
		text.pack()
		root.mainloop()
	elif E2.get() in ['1','2','3','4','5']:
		blah = Tk()
		text = Text(blah)
		text.insert(INSERT, "Your Ip is : ")
		text.insert(INSERT,ip)
		text.pack()
		button = Button(blah, text="OK",command = runserver)
		button.pack()
		blah.mainloop()
	else:
		blah = Tk()
		text = Text(blah)
		text.insert(INSERT, " PLease type the correct number")
		text.pack()
		blah.mainloop()



def hard():
	global serverrunned
	global clientrunned
	if serverrunned == 0 and clientrunned == 0:
		global E2
		global top
		eh = Label(top, text = "Enter level of hardness and after that create server please \n\n\n\n\n\n\n\n")
		eh.pack()
		L2 = Label(top,text=" Enter Level of Hardness  ( 1 to 5 ) ")
		L2.pack()
		E2 = Entry(top, bd = 5)
		E2.pack()
		B = Button(top, text ="Create Server", command = run_server)
		B.pack()
		F = Button(top,text="Cancel",command = cleanup)
		F.pack()
		serverrunned = 1

def join():
	global E1
	client(E1.get())

def cleanup():
	global serverrunned
	global clientrunned
	serverrunned = 0
	clientrunned = 0
	global top
	top.destroy()
	mainloop()
	
def mainloop():
	global top
	top = Tk()
	B1 = Label(top, text = "\n\n\n    What would you like to do ?    \n\n\n    (To get a server's IPv4 type 'ipconfig' in cmd in the server host PC)    \n\n\n    Please enter hardness before creating a server    \n\n") 
	B1.pack()
	guide = Label(top, text = "Guidelines:\n1.Control your bar using Mouse\n2.Don't let the ball go behind you\n\n")
	guide.pack()
	C = Button(top,text="Enter Ip address and join server",command = run_client)
	E = Button(top,text="Enter hardness and create server",command = hard)
	C.pack(side = LEFT)
	E.pack(side = RIGHT)

	top.title("OnlinePyGame")
	top.mainloop()

mainloop()
