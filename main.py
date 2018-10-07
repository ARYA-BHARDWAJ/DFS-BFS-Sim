#This is a pyOpenGL+pygame project targeted to simulate DFS algorithm

#importing stuff
#pygame imports
import pygame
from pygame.locals import *
#opengl imports
from OpenGL.GL import *
from OpenGL.GLU import *
#other imports
import math

#defing functions for basic shapes
def drawPixel(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def drawLine(a, b, c, d):
    glBegin(GL_LINES)
    glVertex2f(a, b)
    glVertex2f(c, d)
    glEnd()

def drawHollowCircle(x, y, r=50):
    lineAmount = 100  # no. of lines used to draw circle
    twoPi = math.pi * 2
    glBegin(GL_LINE_LOOP)
    for i in range(lineAmount):
        glVertex2f(
            x + (r * math.cos(i * twoPi / lineAmount)),
            y + (r * math.sin(i * twoPi / lineAmount))
        )
    glEnd()

def drawFilledCircle(x, y, r=50):
    triangleAmount = 30  # no. of traingles used to draw circle
    twoPi = math.pi * 2
    glBegin(GL_TRIANGLE_FAN)
    for i in range(triangleAmount):
        glVertex2f(
            x + (r * math.cos(i * twoPi / triangleAmount)),
            y + (r * math.sin(i * twoPi / triangleAmount))
        )
    glEnd()

position = [
    (100, 100),
    (200, 100)
]

# main drawing logic
def draw():
    #coding logic here
    for pos in position:
        drawHollowCircle(pos[0], pos[1])


#main function
def main():
    #boiler-plate setup code
    pygame.init()
    display = (800, 600) #the pygame windows resolution
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluOrtho2D(0, 800, 600, 0)

    #the main loop 
    while True:

        #event hadling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if any mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the left button is pressed
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    position.append(pos)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #clear the frame
        draw() #calling the function with drawing logic
        pygame.display.flip() #bring up the updated screen

#calling main()
main()

