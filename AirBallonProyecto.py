from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import OBJLector as lobj
import random

name = 'glut'
angulo = 0.0
eye = [0.0, 0.0, 300.0]
camera = [0.0, 0.0, 0.0]

light_ambient = [0.0, 0.0, 0.0, 1.0]
mat_ambient = [0.8, 0.8, 0.8, 1.0]

light_diffuse = [0.0, 1.0, 0.0, 1.0]
light_position = [1.0, 0.0, 0.0, 1.0]
mat_diffuse = [0.8, 0.8, 0.8, 1.0]

timer_secs = 100
air_ballon = None
angle = 0.0

air_ballonOBJ = lobj.OBJLoader("AirBallonsEddie.obj")

def listObjects():
    global air_ballonOBJ
    global air_ballon
    air_ballon = glGenLists(1);

    glNewList(air_ballon, GL_COMPILE);
    glBegin(GL_TRIANGLES) 
    for o in air_ballonOBJ.objetos:
        for c in o.caras:
            glColor3f(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
            glVertex3f(c.vertices[0].x,c.vertices[0].y, c.vertices[0].z)
            glVertex3f(c.vertices[1].x,c.vertices[1].y, c.vertices[1].z)
            glVertex3f(c.vertices[2].x,c.vertices[2].y, c.vertices[2].z)
    glEnd()
    glEndList();


def airBallon():
    global air_ballon  
    glCallList(air_ballon)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Air Balloon Thrower")

    glShadeModel(GL_FLAT)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_FRONT)

    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)

    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(timer_secs, movimiento, 0)

    listObjects()
	
    glutMainLoop()


def reshape(w, h):
    #	ar = (w*1.0) / h
    glViewport(0, 0,  w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-w, w, -h, h, 1.0, 1000.0)
#	glFrustum(-ar, ar, -ar, ar, 1.0, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    #	reshape(300, 300)
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye[0], eye[1], eye[2], camera[0],camera[1], camera[2], 0.0, 1.0, 0.0)
    
    
    
    glPushMatrix()

    

    

    glPopMatrix()
    glRotatef(angle, 0.0, 1.0, 0.0)
    glTranslatef(200.0, 0.0, 0.0)
    glScalef(20.0, 20.0, 20.0)
    airBallon()
    

    glFlush()
    glutSwapBuffers()


def keyboard(key, x, y):
    if ord(key) == 27:
        sys.exit(0)

def movimiento(value):

    global angle 
    
    glutTimerFunc(timer_secs, movimiento, 0)
    angle= angle + (10.0 if angle < 360.0 else -360.0)
    glutPostRedisplay()

if __name__ == '__main__':
    main()
