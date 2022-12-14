import numpy as np
from .render import PixelArray
from .render import Renderer
from .matrix_tools import MatrixTools
from . import class_mgmt
from .line_segment import LineSegment

from mcpi.minecraft import Minecraft
from . import input
from .mcpi_block_structure.blockstructure import BlockStructure
from .vector import MCVector



class GameObject():
    """
    This is the base class of a GameObject.  It will further define 
    
    cart_pos:       np.array(float, float)      This is the upper left lixel location of the sprite on the 2D screen.
    sprite:         PixelArray                  This is the 2x2 image of the sprite 
    """
    def __init__(self):
        raise RuntimeError("Cannot Instantiate GameObject directly!  Instead use one one of the subclasses")


    def getCartPos(self):
        return self.__cart_pos

    def getSprite(self):
        return self.__sprite

    def setCartPos(self, cart_pos):
        """
        cart_pos:       np.array(float, float)      This is the upper left lixel location of the sprite on the 2D screen.
        """
        self.__cart_pos= cart_pos

    def setSprite(self, sprite):
        self.__sprite=sprite
   
    def collide(self):
        """
        Decide what happens when this object collides with something
        """
        pass


class Ball(GameObject):

    def __init__(self, painter:[Renderer], cart_pos=np.array([0,0]), direction=np.array([0,1]), speed=1,orthogonal_force=0, color=4):
        """
        GameObject.Ball is defined as a point in space with a current speed, direction, and orthogonal force.

        painter:            Renderer            Renderer instance
        cart_pos:           np.array([x,y])     array representing a 2d cartesian coordinate 
        direction:          np.array([x,y])     array representing the 2D vector of the heading of the ball determined by the difference between the current point and previous point
        speed:              float               speed of the ball, default=1.0
        orthogonal_force:   float               amount of lateral force to apply to direction.  <0 is 90deg CCW force, >0 is 90deg CW force
        color:              int                 color number as defined in pong.renderer.Color class
        """
        self.__cart_pos=cart_pos
        self.__sprite=PixelArray.fromDimensions(1,1)
        self.__sprite.fillArray(color)
        self.__direction_unit_vec2=MatrixTools.getUnitVector(direction)
        self.__speed_scalar=speed
        self.__orthogonal_force=orthogonal_force # scalar float:  <0 is 90deg CCW force, >0 is 90deg CW force
        self.__painter = painter[0]
        self.__last_cart_pos = self.__cart_pos
        self.__heading_unit_vec= self.__cart_pos-self.__last_cart_pos 
        self.__headingSegment = LineSegment(self.__cart_pos,self.__last_cart_pos)

    def updatePos(self):
        #print("start pos:",self.__cart_pos)
        #print("dir: ",self.__direction_unit_vec2)
        # get new direction after figuring in orthogonal force
        if self.__orthogonal_force!=0:
            orthogonal_force_unit_vec = MatrixTools.getOrthogonalForceUnitVector(self.__direction_unit_vec2, self.__orthogonal_force)
            new_dir = self.__direction_unit_vec2+orthogonal_force_unit_vec
            self.__direction_unit_vec2 = MatrixTools.getUnitVector(new_dir)
        
        #get new position by applying speed to new direction vector
        new_pos = self.__cart_pos+(self.__direction_unit_vec2*self.__speed_scalar)
        self.__last_cart_pos=self.__cart_pos
        self.__cart_pos=new_pos
        self.__heading_unit_vec= self.__cart_pos-self.__last_cart_pos 
        self.__headingSegment = LineSegment(self.__cart_pos,self.__last_cart_pos)

        #print("new pos:",new_pos)

    def getHeadingUnitVec(self):
        return self.__heading_unit_vec

    def getHeadingSegment(self):
        return self.__headingSegment

    def draw(self):
        self.__painter.paintSprite(self.__sprite, self.__cart_pos)
    
    def collide(self, edge):
        print('Ball Collided with edge!')

class Edge():
    def __init__(self, segment:[LineSegment], normal_vec):
        self.__segment = segment[0]
        self.__normal = normal_vec[0]
    
    def getSegment(self):
        return self.__segment

    def getNormal(self):
        return self.__normal
    

class Rectangle(GameObject):
    """
    GameObject.Rectangle defines a collection of four edges and their normals.
    """
    def _SetRectangle(self, top_left_coord, bottom_right_coord, normal_facing_out=True):
        #  A         B
        #   +-------+
        #   |       |
        #   |       |
        #   |       |
        #   +-------+
        #  C         D

        A = top_left_coord
        B = np.array([bottom_right_coord[0],top_left_coord[1]])
        C = np.array([top_left_coord[0],bottom_right_coord[1]])
        D = bottom_right_coord
        normal_invertor = 1 if normal_facing_out else -1
        self.__line_segments = [
            Edge([LineSegment(A, B)],[np.array([0,1])*normal_invertor]),
            Edge([LineSegment(B, D)],[np.array([1,0])*normal_invertor]),
            Edge([LineSegment(C, D)],[np.array([0,-1])*normal_invertor]),
            Edge([LineSegment(A, C)],[np.array([-1,0])*normal_invertor])
        ]
                  

    def __init__(self, top_left_coord, bottom_right_coord, normal_facing_out=True):
        """
        top_left_coord:             np.array([x,y])     Cartesian Coordinate of upper left end of rectangle
        bottom_right_coord:         np.array([x,y])     Cartesian Coordinate of lower right end of rectangle
        normal_facing_out:          bool                Boolean value to determine whether to make normals face out or in.  Default=True (this would treat the rect where everything inside is solid)
        """
        self._SetRectangle(top_left_coord, bottom_right_coord, normal_facing_out)

    def getSegments(self):
        return self.__line_segments


class Controller(Rectangle):
    """
    Associates a blockstructure and screen sprite with an InputInterface object
    mc_block_structure              blockstructure          This is a blockstructure object created from the minecraft world.
    block_structure_start_pos       MCVector                MCVector representation of an x,y,z coordinate of one corner of the cuboid to place in the MC world.  This vector must be at the base of the structure on the NW corner.  If you stand at the corner of the structure and look away from it, and find that you are facing just between north and west, you're on the right corner.
    input_object                    InputInterface          This is an abstract class, referencing either concrete class TactileInput or RangeInput.  It is the 1d input set of blocks that will be used to capture input from the MC World

    """
    def __init__(
        self, mc:[Minecraft], input_scanner:[input.InputScanner], painter:[Renderer], #subsystems as pointers
        mc_blockstructure:BlockStructure, block_structure_start_pos:MCVector, #MC World Structure for Controller
        joystick_start_block, joystick_end_block, ready_button_block, #MC World block Coords to define virtual input
        controller_sprite:PixelArray, sprite_screen_pos):

        self.__block_structure = mc_blockstructure
        self.__block_structure_start_pos = block_structure_start_pos
        self.__controller_state='unloaded' # one of ['unloaded','loaded','ingame','endgame']
        self.__joystick_input = input.RangeInputParser(mc,input_scanner,start_coord=joystick_start_block, end_coord=joystick_end_block)
        self.__ready_button = input.TactileInputParser(mc,input_scanner,start_coord=ready_button_block, end_coord=ready_button_block)
        self.__sprite = controller_sprite
        self.__sprite_screen_pos = sprite_screen_pos
        self.__painter = painter[0]
        self.__half_screen_width = int(self.__painter.getScreenWidth()/2)
        self.__rect = Rectangle(sprite_screen_pos,np.array([sprite_screen_pos[0]+controller_sprite.getWidth(),sprite_screen_pos[1]-controller_sprite.getHeight()]))


    def readScannerInput(self):
        if self.__controller_state=='unloaded':
            self.__ready_button.readInputScanner()
            if self.__ready_button.getInputValue()==True:
                self.__controller_state=='loaded'
        self.__joystick_input.readInputScanner()

    def updatePos(self):
        """
        This measures the width o the paddle against the width of the screen and ensures that there is a linear formula such that joystick input value:0 places the paddle at the left edge of the screen and joystick input value 1 places the paddle at the right side of the screen.
        
        We only move the x value (sprite_screen_pos[0] because the ship moves left and right only.)
        """
        self.__sprite_screen_pos[0] = (
            (self.__painter.getScreenWidth()-self.__sprite.getWidth())*
            self.__joystick_input.getInputValue()-self.__half_screen_width
        )

    def getDrawData(self):
        print("P1:",self.__joystick_input.getInputValue(), p1_pos[0]," b:",self.__ready_button.getInputValue())


    def draw(self):
        self.__painter.paintSprite(self.__sprite, self.__sprite_screen_pos)

    def getColliderRect(self):
        return self.__rect
