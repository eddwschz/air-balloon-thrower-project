from OBJLector import *
from OpenGL.GL import *

class airBallon():
    def __init__(self):
        self.obj = OBJLoader("AirBallonsEddie.obj")
		self.objetos = self.obj.objectos

    def genGList(self):
        for o in self.objetos:
            o.generateglList()