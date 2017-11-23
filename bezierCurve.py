from OpenGL.GL import *
import math
import numpy as np

class Vertice():
    def __init__(self, xValue, yValue):
        self.x=xValue
        self.y=yValue

class ControlPoints():
    def __init__(self, vA):
        self.puntosControl = self.calculatePC(vA)
    
    def calculatePC(self,vI):
        puntosControl=[]
        d=10
        puntosControl.append(vI)
        puntosControl.append(Vertice(vI.x+d*2,vI.y+d))
        puntosControl.append(Vertice(vI.x+d*4,vI.y))
        puntosControl.append(Vertice(vI.x+d*6,vI.y-d))
        return puntosControl

class BezierCurve():
    def __init__(self, pC, dtV):
        self.puntosControl=pC
        self.curva =[]
        self.dt = dtV
        self.calculateCurve()

    def calculateCurve(self):
        j=0
        for i in range(int(1/self.dt)+1):
            print("En dt= " + str(self.dt*i))
            self.pointsOnCurveBezier(self.dt*j)
            j=j+1

    def pointsOnCurveBezier(self,t):
        rX = ((1-t)**3)*self.puntosControl[0].x + 3*t*((1-t)**2)*self.puntosControl[1].x + 3*(t**2)*(1-t)*self.puntosControl[2].x + (t**3)*self.puntosControl[3].x
        rY = ((1-t)**3)*self.puntosControl[0].y + 3*t*((1-t)**2)*self.puntosControl[1].y + 3*(t**2)*(1-t)*self.puntosControl[2].y + (t**3)*self.puntosControl[3].y
        print("x: " + str(rX) + " " + "y: " + str(rY))
        result = Vertice(rX,rY)
        self.curva.append(result)

    

    



