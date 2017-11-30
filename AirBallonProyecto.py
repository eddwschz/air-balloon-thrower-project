from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import OBJLector as lobj
import random
import bezierCurve as bC

name = 'glut'
angulo = 0.0

#PERSPECTIVE
eye = [0.0, 0.0, 300.0]
camera = [0.0, 0.0, 0.0]

#LIGTH
light_ambient = [1.0, 1.0, 1.0, 1.0]
mat_ambient = [0.8, 0.8, 0.8, 1.0]

light_diffuse = [0.0, 1.0, 0.0, 1.0]
light_position = [1.0, 0.0, 0.0, 1.0]
mat_diffuse = [0.8, 0.8, 0.8, 1.0]

#TIMER
timer_secs = 70

#LIST AIRBALLON GL
air_ballon = None
mountain = None

#SCALE BALLON Z
zScale = 0.0
zValueScale = 20.0

#OBJ AIR BALLON
air_ballonOBJ = lobj.OBJLoader("AirBallonsEddie.obj")
mountainOBJ = lobj.OBJLoader("MountainEddie.obj")

#INDEX OF CURVE BEZIER
index_curve = 0
#INDEX OF POINT IN A CURVE BEZIER
index_point_curve = 0

#VARIABLES X Y Z
xV = 0.0
yV = 0.0
zV = 0.0

#CURVES
curvesBezier = []
#print("CURVE A COORDS")
curvesBezier.append(bC.BezierCurve(bC.Vertice(0.0,-0.0,0.0),50.0,50.0,0.0,0.1))
#print("CURVE B COORDS")
curvesBezier.append(bC.BezierCurve(bC.Vertice(curvesBezier[0].controlPoints[8].x,0.0,curvesBezier[0].controlPoints[8].z),0.0,50.0,-400.0,0.1))
#print("CURVE C COORDS")
curvesBezier.append(bC.BezierCurve(bC.Vertice(curvesBezier[1].controlPoints[8].x,0.0,curvesBezier[1].controlPoints[8].z),-50.0,50.0,0.0, 0.1))
#print("CURVE D COORDS")
curvesBezier.append(bC.BezierCurve(bC.Vertice(curvesBezier[2].controlPoints[8].x,0.0,curvesBezier[2].controlPoints[8].z),-50.0,50.0,0.0, 0.1))
#print("CURVE E COORDS")
curvesBezier.append(bC.BezierCurve(bC.Vertice(curvesBezier[3].controlPoints[8].x,0.0,curvesBezier[3].controlPoints[8].z),0.0,50.0,400.0, 0.1)) 
#print("CURVE F COORDS")
curvesBezier.append(bC.BezierCurve(bC.Vertice(curvesBezier[4].controlPoints[8].x,0.0,curvesBezier[4].controlPoints[8].z),50.0,50.0,0.0,0.1))

def listObjects():
    global air_ballonOBJ
    global air_ballon
    air_ballon = glGenLists(1);

    glNewList(air_ballon, GL_COMPILE);
    glBegin(GL_TRIANGLES) 
    for o in air_ballonOBJ.objetos:
        for c in o.caras:
            if o.nombre=="Ballon_Cylinder.002":
                glColor3f(1.0, random.uniform(0,0.031), random.uniform(0,0.29))
            elif o.nombre=="Box_Cube.003":
                glColor3f(random.uniform(0,0.24), random.uniform(0,0.25), random.uniform(0,0.58))
            else:
                glColor3f(0.0, random.uniform(0,0.55), 1.0)
            glVertex3f(c.vertices[0].x,c.vertices[0].y, c.vertices[0].z)
            glVertex3f(c.vertices[1].x,c.vertices[1].y, c.vertices[1].z)
            glVertex3f(c.vertices[2].x,c.vertices[2].y, c.vertices[2].z)
    glEnd()
    glEndList();

    global mountainOBJ
    global mountain
    mountain = glGenLists(1);
    
    glNewList(mountain, GL_COMPILE);
    glBegin(GL_TRIANGLES) 
    for o in mountainOBJ.objetos:
        for c in o.caras:
            #glColor3f(0.184, 0.107, 0.043)
            glColor3f(random.uniform(0,0.55), random.uniform(0,0.28), random.uniform(0,0.19))
            glVertex3f(c.vertices[0].x,c.vertices[0].y, c.vertices[0].z)
            glVertex3f(c.vertices[1].x,c.vertices[1].y, c.vertices[1].z)
            glVertex3f(c.vertices[2].x,c.vertices[2].y, c.vertices[2].z)
    glEnd()
    glEndList();

def airBallon():
    global air_ballon  
    glCallList(air_ballon)

def mountainW():
    global mountain
    glCallList(mountain)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 700)
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
    glutTimerFunc(timer_secs, movement, 0)

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

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye[0], eye[1], eye[2], camera[0],camera[1], camera[2], 0.0, 1.0, 0.0)


    glPushMatrix()
    glTranslatef(xV, yV, zV)
    if index_curve==0 or index_curve==5:
        glScalef(20.0, 20.0, 20.0)
    elif index_curve==2 or index_curve==3:
        glScalef(5.0, 5.0, 5.0)
    elif index_curve==1:
        glScalef(zValueScale, zValueScale, zValueScale)
    elif index_curve==4:
        glScalef(zValueScale, zValueScale, zValueScale)
    airBallon()
    glPopMatrix()


    glPushMatrix()
    glTranslatef(80.0,-400.0,0.0)
    glScalef(80.0, 80.0, 80.0)
    mountainW()
    glPopMatrix()

    glFlush()
    glutSwapBuffers()


def keyboard(key, x, y):
    if ord(key) == 27:
        sys.exit(0)

def movement(value):
    global xV
    global yV
    global zY
    global index_curve
    global index_point_curve
    global curvesBezier
    global zValueScale

    glutTimerFunc(timer_secs, movement, 0)

    if index_point_curve<10:
        index_point_curve=index_point_curve+1
    else:
        index_point_curve=0
        if(index_curve<5):
            index_curve=index_curve+1
        else:
            index_curve=0
    
    xV = curvesBezier[index_curve].curvasPoints[index_point_curve].x
    yV = curvesBezier[index_curve].curvasPoints[index_point_curve].y
    zV = curvesBezier[index_curve].curvasPoints[index_point_curve].z

    if index_curve==1:
        zValueScale=zValueScale-2
    elif index_curve==4:
        zValueScale=zValueScale+2
    #print(str(zValueScale))

    #print("In the curve " + str(index_curve) + " in the point of curve " + str(index_point_curve))
    #print(" X: " + str(xV) + " " + " Y: " + str(yV) + " Z: " + str(zV))


    glutPostRedisplay()


if __name__ == '__main__':
    main()
