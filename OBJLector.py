from OpenGL.GL import *
import math
import numpy as np

class Vertice():
    def __init__(self, xValue, yValue, zValue):
        self.x=xValue
        self.y=yValue
        self.z=zValue

    def matrixCoords(self):
        return np.array([self.x,self.y,self.z])

class Cara():
    def __init__(self, vS):
        self.vertices=vS
        self.eqNormalC()
    
    def eqNormalC(self):
        self.eqNormal = []
        [A,B,C] = np.cross(self.vertices[1].matrixCoords() - self.vertices[0].matrixCoords(), self.vertices[2].matrixCoords() - self.vertices[0].matrixCoords())
        v = self.vertices[0]
        D = -((A*v.x) + (B*v.y) +(C*v.z))
        self.eqNormal = (A,B,C,D)

class Objeto():
    def __init__(self, cS, name):
        self.caras=cS
        self.nombre = name

    def translate(self, tX, tY, tZ):
        for c in self.caras:
            for v in c.vertices:
                v.x= v.x + tX
                v.y= v.y + tY
                v.y= v.z + tZ
        
        for c in self.caras:
            c.eqNormalC()

    def scale(self, sX, sY, sZ):
        for c in self.caras:
            for v in c.vertices:
                v.x= v.x * sX
                v.y= v.y * sY
                v.y= v.z * sZ
        
        for c in self.caras:
            c.eqNormalC()

    def rotation(self, angle, rX, rY, rZ):
        rd=np.radians(angle)
        cos=np.cos(rd)
        sen=np.sin(rd)

        for c in self.caras:
            for v in c.vertices:
                if rX > 0.0:
                    v.y = cos*v.y + sen*v.z
                    v.z = cos*v.z - sen*v.y
                
                elif rY>0.0:
                    v.x = cos*v.x + sen*v.z
                    v.z = cos*v.x - sen*v.z
                
                elif rZ>0.0:
                    v.x = cos*v.x + sen*v.y
                    v.y = cos*v.y - sen*v.x
                
        for c in self.caras:
            c.eqNormalC()

class OBJLoader():
    def __init__(self, filename):
        self.archivo = open(filename, 'r')
        self.objetos = []
        self.load()
        
    def load(self):
        caras=[]
        vertices=[]  
        nombre = ""    
        bandObj = False
        codigo = self.archivo.read()
        lineas = codigo.splitlines()
        for l in lineas:
            elements = l.split()
            if elements:
                if elements[0]=='o':
                    if bandObj:
                        self.objetos.append(Objeto(caras,nombre))
                        caras=[]
                        bandObj=False
                    else:
                        bandObj = True

                elif elements[0]=='v':
                    vertices.append(Vertice(float(elements[1]),float(elements[2]),float(elements[3])))

                elif elements[0]=='f':
                    verticesF=[]
                    for e in elements:
                        if(e!='f'):
                            vNumber = int(e.split("//")[0])-1
                            verticesF.append(vertices[vNumber])
                    caras.append(Cara(verticesF))