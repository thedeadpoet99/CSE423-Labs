from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_studentID():
    glPointSize(10)
    glBegin(GL_LINES)
    #for 2
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(50,200)
    glVertex2f(70, 200)

    glVertex2f(50, 200)
    glVertex2f(50, 220)

    glVertex2f(50, 220)
    glVertex2f(70,220)

    glVertex2f(70,220)
    glVertex2f(70,240)

    glVertex2f(70, 240)
    glVertex2f(50, 240)

    #for 1
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(90, 200)
    glVertex2f(90, 240)


    # for 3
    glColor3f(1.0, 0.5, 0.0)

    glVertex2f(110, 200)
    glVertex2f(130, 200)

    glVertex2f(130, 200)
    glVertex2f(130, 220)

    glVertex2f(130, 220)
    glVertex2f(110, 220)

    glVertex2f(130, 220)
    glVertex2f(130, 240)

    glVertex2f(130,240)
    glVertex2f(110,240)


    # for 0
    glColor3f(1.0, 0.0, 0.5)
    glVertex2f(150,240)
    glVertex2f(170, 240)

    glVertex2f(150, 240)
    glVertex2f(150, 200)

    glVertex2f(150, 200)
    glVertex2f(170, 200)

    glVertex2f(170, 200)
    glVertex2f(170, 240)

    # for 1
    glColor3f(0.5, 1.0, 0.5)

    glVertex2f(190, 200)
    glVertex2f(190, 240)

    # for 5
    glColor3f(0.5, 0.5, 0.0)

    glVertex2f(210, 200)
    glVertex2f(230, 200)

    glVertex2f(230, 200)
    glVertex2f(230, 220)

    glVertex2f(230, 220)
    glVertex2f(210, 220)

    glVertex2f(210,220)
    glVertex2f(210,240)

    glVertex2f(210,240)
    glVertex2f(230,240)

    # for 8
    glColor3f(2.0, 0.5, 1.0)

    glVertex2f(250,200)
    glVertex2f(270,200)

    glVertex2f(250,200)
    glVertex2f(250, 220)

    glVertex2f(250, 220)
    glVertex2f(250, 240)

    glVertex2f(250,220)
    glVertex2f(270,220)

    glVertex2f(270,200)
    glVertex2f(270,220)

    glVertex2f(270,220)
    glVertex2f(270,240)

    glVertex2f(250,240)
    glVertex2f(270,240)

    # for 0
    glColor3f(1.0, 1.0, 0.5)

    glVertex2f(290,200)
    glVertex2f(310, 200)

    glVertex2f(290, 200)
    glVertex2f(290, 220)

    glVertex2f(310, 200)
    glVertex2f(310, 220)

    glVertex2f(290,220)
    glVertex2f(290,240)

    glVertex2f(310,220)
    glVertex2f(310,240)

    glVertex2f(290,240)
    glVertex2f(310,240)


    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_studentID()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"21301580") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
