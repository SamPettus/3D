import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies1 = ( #Vertices for a cube
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1),
)
verticies3 = (
	(1, 1, 1), #0
	(-1, 1, 1), #1
	(-1, 1, -1), #2 
	(1, 1, -1), #3 
	(1, -1, 1), #4
	(-1, -1, 1), #5 
	(-1, -1, -1),#6 
	(1, -1, -1), #7
	(0, 2, 0) # 8
)
verticies2 = ( #Vertices for a square pyramid
	(0,1,0),
	(1,0,1),
	(-1,0,1),
	(-1,0,-1),
	(1,0,-1),
)
edges3 = (
	(0,1),
	(0,3),
	(0,4),
	(0,8),
	(1,8),
	(1,2),
	(1,5),
	(2,8),
	(2,3),
	(2,6),
	(3,8),
	(3,7),
	(4,5),
	(5,6),
	(6,7),
	(7,4),



)
edges2 = (#Edge for a square pyramid
	(0,1),
	(0,2),
	(0,3),
	(0,4),
	(1,2),
	(2,3),
	(3,4),
	(4,1),
)
edges1 = (#Edge for a cube
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7),
)
surfaces = ( #Surface for a cube
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2),
	(4,0,3,6),
)
surfaces2 = (
	(1,2,3,4),
	(0,1,2),
	(1,2,0),
	(0,3,4),
	(3,4,0),
	(0,4,1),
	(1,4,0)
)
colors = ( #colors
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,0,0),
	(1,1,1),
	(0,1,1),
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,0,0),
	(1,1,1),
	(0,1,1),
)
def House():
	glBegin(GL_LINES)
	for edge in edges3:
		for vertex in edge:
			glColor3fv((1,1,1))
			glVertex3fv(verticies3[vertex])
	glEnd()
def Pyramid():
	glBegin(GL_QUADS)
	for surface in surfaces2:
		x = 0
		for vertex in surface:
			x+=1
			glColor3fv(colors[x])
			glVertex3fv(verticies2[vertex])
	glEnd()
	glBegin(GL_LINES)
	for edge in edges2:
		for vertex in edge:
			glVertex3fv(verticies2[vertex])
	glEnd()
def Cube():
	glBegin(GL_QUADS)
	for surface in surfaces:
		x= 0;
		
		for vertex in surface:
			x+=1
			glColor3fv(colors[x])
			glVertex3fv(verticies1[vertex])
	glEnd()
	glBegin(GL_LINES)
	for edge in edges1:#Connects the vertices with the edges
		for vertex in edge:
			glVertex3fv(verticies1[vertex])
	glEnd()
def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0,0.0,-15)#Changes our field of view
	glRotatef(0, 0, 0, 0)
	vel = 1
	autopilot = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					glTranslatef(0,0,1)
				if event.button == 5:
					glTranslatef(0,0,-1)
		inkey = pygame.key.get_pressed()
		if(inkey[pygame.K_1]): #Changes the vel of the spin
			vel = 1
		if(inkey[pygame.K_2]):
			vel= 2
		if(inkey[pygame.K_3]):
			vel =3
		if(inkey[pygame.K_4]):
			vel = 4
		if(inkey[pygame.K_5]):
			vel = 5
		if(inkey[pygame.K_6]):
			vel = 6
		if(inkey[pygame.K_7]):
			vel = 7
		if(inkey[pygame.K_8]):
			vel = 8
		if(inkey[pygame.K_9]):
			vel = 9
		if(inkey[pygame.K_0]):
			autopilot = True
		if(inkey[pygame.K_LEFT]):
			glTranslatef(-.5,0,0)
		if(inkey[pygame.K_RIGHT]):
			glTranslatef(.5,0,0)
		if(inkey[pygame.K_UP]):
			glTranslatef(0,.5,0)
		if(inkey[pygame.K_DOWN]):
			glTranslatef(0,-.5,0)
		if(autopilot):			#changes the rotatition
			glRotatef(vel,1,-1,1)
		if(inkey[pygame.K_w]):
			glRotatef(vel,1,0,0)
			autopilot = False
		if(inkey[pygame.K_s]):
			glRotatef(vel,-1,0,0)
			autopilot = False
		if(inkey[pygame.K_d]):
			glRotatef(vel,0,1,0)
			autopilot = False
		if(inkey[pygame.K_a]):
			glRotatef(vel,0,-1,0)
			autopilot = False
		#glRotatef(1,1,1,1)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		House()
		pygame.display.flip()
		pygame.time.wait(10)

main()
