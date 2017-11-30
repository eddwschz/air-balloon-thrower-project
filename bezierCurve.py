from OpenGL.GL import *
import math
import numpy as np

class Vertice():
    def __init__(self, xValue, yValue, zValue):
        self.x=xValue
        self.y=yValue
        self.z=zValue

class BezierCurve():
    def __init__(self, vAct, xInc, yInc, zInc, dtV):
        self.vA = vAct
        self.xI = xInc
        self.yI = yInc
        self.zI = zInc
        self.controlPoints=[]
        self.curvasPoints=[]
        self.dt = dtV
        self.calculateCurveControlPoints()
        self.calculateCurve()

    def calculateCurveControlPoints(self):
        #5 CONTROL POINTS FOR A CURVE
        #print("CONTROL POINTS FOR A CURVE")
        self.controlPoints.append(self.vA)
        #print("P1:" + " X: "+ str(self.controlPoints[0].x) + " Y: "+ str(self.controlPoints[0].y) + " Z: "+ str(self.controlPoints[0].z))
        self.controlPoints.append(Vertice(self.controlPoints[0].x+self.xI, self.controlPoints[0].y-self.yI , self.controlPoints[0].z+self.zI))
        #print("P2:" + " X: "+ str(self.controlPoints[1].x) + " Y: "+ str(self.controlPoints[1].y) + " Z: "+ str(self.controlPoints[1].z))
        self.controlPoints.append(Vertice(self.controlPoints[1].x+self.xI, self.controlPoints[1].y-self.yI , self.controlPoints[1].z+self.zI))
        #print("P3:" + " X: "+ str(self.controlPoints[2].x) + " Y: "+ str(self.controlPoints[2].y) + " Z: "+ str(self.controlPoints[2].z))
        self.controlPoints.append(Vertice(self.controlPoints[2].x+self.xI, self.controlPoints[2].y-self.yI , self.controlPoints[2].z+self.zI))
        #print("P4:" + " X: "+ str(self.controlPoints[3].x) + " Y: "+ str(self.controlPoints[3].y) + " Z: "+ str(self.controlPoints[3].z))
        self.controlPoints.append(Vertice(self.controlPoints[3].x+self.xI, self.controlPoints[3].y-self.yI , self.controlPoints[3].z+self.zI))
        #print("P5:" + " X: "+ str(self.controlPoints[4].x) + " Y: "+ str(self.controlPoints[4].y) + " Z: "+ str(self.controlPoints[4].z))
        self.controlPoints.append(Vertice(self.controlPoints[4].x+self.xI, self.controlPoints[4].y+self.yI , self.controlPoints[4].z+self.zI))
        #print("P6:" + " X: "+ str(self.controlPoints[5].x) + " Y: "+ str(self.controlPoints[5].y) + " Z: "+ str(self.controlPoints[5].z))
        self.controlPoints.append(Vertice(self.controlPoints[5].x+self.xI, self.controlPoints[5].y+self.yI , self.controlPoints[5].z+self.zI))
        #print("P7:" + " X: "+ str(self.controlPoints[6].x) + " Y: "+ str(self.controlPoints[6].y) + " Z: "+ str(self.controlPoints[6].z))
        self.controlPoints.append(Vertice(self.controlPoints[6].x+self.xI, self.controlPoints[6].y+self.yI , self.controlPoints[6].z+self.zI))
        #print("P8:" + " X: "+ str(self.controlPoints[7].x) + " Y: "+ str(self.controlPoints[7].y) + " Z: "+ str(self.controlPoints[7].z))
        self.controlPoints.append(Vertice(self.controlPoints[7].x+self.xI, self.controlPoints[7].y+self.yI , self.controlPoints[7].z+self.zI))
        #print("P9:" + " X: "+ str(self.controlPoints[8].x) + " Y: "+ str(self.controlPoints[8].y) + " Z: "+ str(self.controlPoints[8].z))

    def calculateCurve(self):
        j=0
        for i in range(int(1/self.dt)+1):
            #print("     EN DT= " + str(self.dt*i))
            self.pointsOnCurveBezier(self.dt*j)
            j=j+1

    def pointsOnCurveBezier(self,t):
        rX = ((1-t)**3)*self.controlPoints[0].x + 3*t*((1-t)**2)*self.controlPoints[2].x + 3*(t**2)*(1-t)*self.controlPoints[4].x + (t**3)*self.controlPoints[8].x
        rY = ((1-t)**3)*self.controlPoints[0].y + 3*t*((1-t)**2)*self.controlPoints[2].y + 3*(t**2)*(1-t)*self.controlPoints[4].y + (t**3)*self.controlPoints[8].y
        rZ = ((1-t)**3)*self.controlPoints[0].z + 3*t*((1-t)**2)*self.controlPoints[2].z + 3*(t**2)*(1-t)*self.controlPoints[4].z + (t**3)*self.controlPoints[8].z
        #print("     X: " + str(rX) + " Y: " + str(rY) + " Z: " + str(rZ))
        self.curvasPoints.append(Vertice(rX,rY,rZ))

    

    



