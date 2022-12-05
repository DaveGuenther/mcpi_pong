import abc
import numpy as np
class Collidable(abc.ABC):
    def __init__(self):
        pass
    
    @abc.abstractclassmethod 
    def collide(self):
        pass

    pass

    def setBoundingBox(self, this_int):
        self._bounding_box=this_int

class Renderable(abc.ABC):
    def __init__(self):
        pass

    def setPos(self, this_int):
        self._pos=this_int

    def setSprite(self, this_int):
        self._sprite=this_int

class Ball(Collidable, Renderable):
    def __init__(self):
        self.setBoundingBox(10)
        self.setPos(3)
        self.setSprite(7)
        self.__speed=10.0
        self.__ortho_force=0
        self.__color=1
        self.__direction=np.array([1,0])

    def collide(self):
        self.__direction*=-1

        

    def toString(self):
        print('Position:',self._pos)
        print('Sprite:',self._sprite)
        print('Bounding Box:',self._bounding_box)
        print('Speed:',self.__speed)
        print('ortho val:',self.__ortho_force)
        print('Color:',self.__color)
        print('Direction:',self.__direction)

class Edge(Collidable, Renderable):
    def __init__(self):
        self.__edge_specific_data=5.0
        self.setPos(6)
        self.setSprite(9)
        self.setBoundingBox(15)
        pass

    def collide(self):
        print('Doing Nothing.  Edge stays where it is')

    def toString(self):
        print('Position:',self._pos)
        print('Sprite:',self._sprite)
        print('Bounding Box:',self._bounding_box)
        print('Edge Date:',self.__edge_specific_data)



my_edge=Edge()
my_ball=Ball()

my_ball.toString()
my_ball.collide()
my_ball.toString()

my_edge.collide()
my_edge.toString()