import numpy as np
import abc
from .render import PixelArray


class GameObjectInterface(abc.ABC):
    @abc.abstractclassmethod
    def collide():
        pass

class GameObject(GameObjectInterface):
    """
    This is the base class of a GameObject.
    
    cart_pos:       np.array(float, float)      This is the upper left lixel location of the sprite on the 2D screen.
    sprite:         PixelArray                  This is the 2x2 image of the sprite 
    """
    def __init__(self, cart_pos, sprite):
        self._cart_pos = cart_pos
        self._sprite = sprite

    def getCartPos(self):
        return self._cart_pos

    def getSprite(self):
        return self._sprite

    def setCartPos(self, cart_pos):
        """
        cart_pos:       np.array(float, float)      This is the upper left lixel location of the sprite on the 2D screen.
        """
        self._cart_pos= cart_pos

    def setSprite(self, sprite):
        self._sprite=sprite

    def collide(self):
        """
        Decide what happens when this object collides with something
        """
        pass


class MovableVirtualGameObject(GameObject):
    """
    This is a kind of GameObject that is movable.  It has a speed and direction.  It not controlled by the Player direclty (there is no mineraft controller for the object)
    
    speed:                  float                           This is the speed that an object is currently moving each frame.
    direction:              np.array(float, float)          This is a vector representing the cartesian direction [0,1] is up, [1,0] is right
    lateral_force_vector    float                           Negative value is a 90 deg CCW force, Positive is a 90deg CW force.  0 is no lateral force
    """
    def __init__(self, cart_pos, sprite, speed, direction, lateral_force_vector):
        GameObject.__init__(GameObject, cart_pos, sprite)
        self._speed=speed
        self._direction = direction
        self._lateral_force_vector=lateral_force_vector

    def getSpeed(self):
        return self._speed

    def getDirection(self):
        return self._direction

    def getForceVector(self):
        return self._lateral_force_vector
    
    def setSpeed(speed):
        self._speed=speed

    def setDirection(direction):
        self._direction=direction

    def setForceVector(force_vector):
        self._lateral_force_vector=lateral_force_vector

    def collide(self):
        """
        Decide what happens when this object collides with something
        """
        pass

class MovablePhysicalGameObject(MovableVirtualGameObject):
    """
    This is a kind of GameObject that is movable and directly controlled by some interaction in the MC world.

    PC_Minecraft_Controller:        mcpi_block_structure        This is the actual Minecraft world object that will feed input data to this MovablePCGameObject.

    """
    def __init__(self, cart_pos, sprite, speed, direction, lateral_force_vector, PC_Minecraft_Controller):
        MovableVirtualGameObject.__init__(MovableVirtualGameObject, cart_pos, sprite, speed, direction, lateral_force_vector)
        self._PC_MC_Controller = PC_Minecraft_Controller

    def getInput(self):
        return self._PC_MC_Controller

    def collide(self):
        """
        Decide what happens when this object collides with something
        """
        pass        

