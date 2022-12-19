import numpy as np
import random
from .render import PixelArray
from .render import Renderer
from .matrix_tools import MatrixTools
from . import class_mgmt
from .line_segment import LineSegment
from mcpi.minecraft import Minecraft
from . import input_object
from .mcpi_block_structure.blockstructure import BlockStructure
from .vector import MCVector
from .timer import Delay
from .event import EndEvent




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
        self.__headingSegment = LineSegment(self.__cart_pos,self.__last_cart_pos, directional=True)

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
        self.__headingSegment = LineSegment(self.__cart_pos,self.__last_cart_pos, directional=True)

        #print("new pos:",new_pos)

    def getHeadingUnitVec(self):
        return self.__heading_unit_vec

    def getHeadingSegment(self):
        return self.__headingSegment

    def draw(self):
        self.__painter.paintSprite(self.__sprite, self.__cart_pos)
    
    def collide(self, edge, intercept):
        """
        edge:                   LineSegment         This is the edge that the ball (self) has collided with
        intercept:              np.array([x,y])     This is the point that the ball (self) intersects with the edge

        
        This function sets a new heading and current direction for the ball after colliding with an edge.  
        
        """
        edge_screen=edge.getSegment()
        #subtract intercept from both secments
        origin_ball=LineSegment(self.__last_cart_pos-intercept, self.__cart_pos-intercept, directional=True)
        origin_edge=LineSegment(edge_screen.getPoints()[0]-intercept, edge_screen.getPoints()[1]-intercept)

        if edge_screen.getSlope()=='vertical':
            #rotate ball by -90 deg
            ball_vec_end_in_edge_space = MatrixTools.rotateVector(-90, origin_ball.getPoints()[1])
            
            #flip y coord of ball endpoint
            ball_vec_end_in_edge_space[1]=ball_vec_end_in_edge_space[1]*-1

            #rotate ball by 90 deg
            new_ball_end_in_screen_space = MatrixTools.rotateVector(90, ball_vec_end_in_edge_space)

        elif edge_screen.getSlope()==0:
            
            #flip y coord of ball endpoint
            new_ball_end_in_screen_space=origin_ball.getPoints()[1]
            new_ball_end_in_screen_space[1]=new_ball_end_in_screen_space[1]*-1    
            
        else:
            #slope is either positive or negative but not vertical or horizontal
            
            #use a non-zero edge point
            edge_point_to_calc_theta=0
            if (origin_ball.getPoints()[0][0]==0)|(origin_ball.getPoints()[0][1]==0):
                edge_point_to_calc_theta=1
            
            #calculate negative theta form edge point
            neg_theta = -1*(180/math.pi)*math.atan(
                float(origin_edge.getPoints()[edge_point_to_calc_theta][1])/
                float(origin_edge.getPoints()[edge_point_to_calc_theta][0]))

            #Rotate ball by neg_theta
            ball_vec_end_in_edge_space = MatrixTools.rotateVector(neg_theta, origin_ball.getPoints()[1])

            #Flip y coord of ball endpoint
            ball_vec_end_in_edge_space[1]=ball_vec_end_in_edge_space[1]*-1

            #rotate ball by pos_theta
            pos_theta = neg_theta*-1
            new_ball_end_in_screen_space = MatrixTools.rotateVector(pos_theta, ball_vec_end_in_edge_space)             


        #add intercept to ball_vec
        reflected_ball_vec = LineSegment(intercept, new_ball_end_in_screen_space+intercept,directional=True)

        self.__last_cart_pos=intercept
        self.__cart_pos=reflected_ball_vec.getPoints()[1]
        self.__heading_unit_vec= self.__cart_pos-self.__last_cart_pos 
        self.__direction_unit_vec2=MatrixTools.getUnitVector(self.__heading_unit_vec)
        self.__headingSegment = reflected_ball_vec

    def resetBall(self):
        new_direction = np.array([(random.uniform(.5, 1.0)*random.sample([-1,1],1)[0]),(random.uniform(.5, 1.0)*random.sample([-1,1],1)[0])]) # get random numbers from -1 to 1
        self.__direction_unit_vec2=MatrixTools.getUnitVector(new_direction)
        self.__last_cart_pos=np.array([0,0])
        self.__cart_pos=np.array([0,0])
        self.__orthogonal_force=0
        self.__heading_unit_vec= self.__cart_pos-self.__last_cart_pos 
        self.__headingSegment = LineSegment(self.__cart_pos,self.__last_cart_pos, directional=True)

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
    def __init__(self, top_left_coord, bottom_right_coord, normal_facing_out=True):
        """
        top_left_coord:             np.array([x,y])     Cartesian Coordinate of upper left end of rectangle
        bottom_right_coord:         np.array([x,y])     Cartesian Coordinate of lower right end of rectangle
        normal_facing_out:          bool                Boolean value to determine whether to make normals face out or in.  Default=True (this would treat the rect where everything inside is solid)
        """
        self._cart_pos = top_left_coord
        self._getDimensions(top_left_coord, bottom_right_coord)
        self._getCornersFromDimensions()
        self._SetRectangle(normal_facing_out)  

    def _getDimensions(self, top_left_corner, bottom_right_corner):
        self._width = bottom_right_corner[0]-top_left_corner[0]
        self._height = bottom_right_corner[1]-top_left_corner[1]
    
    def _getCornersFromDimensions(self):
        #  A         B
        #   +-------+
        #   |       |
        #   |       |
        #   |       |
        #   +-------+
        #  C         D
        self._A = self._cart_pos
        self._B = np.array([self._cart_pos[0]+self._width,self._cart_pos[1]])
        self._C = np.array([self._cart_pos[0],self._cart_pos[1]+self._height])
        self._D = np.array([self._cart_pos[0]+self._width,self._cart_pos[1]+self._height])

    def _SetRectangle(self, normal_facing_out=True):

        #self.__A = top_left_coord
        #self.__B = np.array([bottom_right_coord[0],top_left_coord[1]])
        #self.__C = np.array([top_left_coord[0],bottom_right_coord[1]])
        #self.__D = bottom_right_coord
        self._normal_invertor = 1 if normal_facing_out else -1
        self._line_segments = [
            Edge([LineSegment(self._A, self._B)],[np.array([0,1])*self._normal_invertor]),
            Edge([LineSegment(self._B, self._D)],[np.array([1,0])*self._normal_invertor]),
            Edge([LineSegment(self._C, self._D)],[np.array([0,-1])*self._normal_invertor]),
            Edge([LineSegment(self._A, self._C)],[np.array([-1,0])*self._normal_invertor])
        ]
                  

  

    def setCartPos(self, cart_pos):
        self._cart_pos=cart_pos # set new top left corner of clipping rect
        self._getCornersFromDimensions() # determine remaining corners
        self._SetRectangle() # construct new rect
        

    def getSegments(self):
        return self._line_segments

    def collide(self):
        pass



class Controller(Rectangle):
    """
    Associates a blockstructure and screen sprite with an InputInterface object
    mc_block_structure              blockstructure          This is a blockstructure object created from the minecraft world.
    block_structure_start_pos       MCVector                MCVector representation of an x,y,z coordinate of one corner of the cuboid to place in the MC world.  This vector must be at the base of the structure on the NW corner.  If you stand at the corner of the structure and look away from it, and find that you are facing just between north and west, you're on the right corner.
    input_object                    InputInterface          This is an abstract class, referencing either concrete class TactileInput or Rangeinput_object  It is the 1d input set of blocks that will be used to capture input from the MC World

    """
    def __init__(
        self, mc:[Minecraft], input_scanner:[input_object.InputScanner], painter:[Renderer], #subsystems as pointers
        mc_blockstructure:BlockStructure, block_structure_start_pos:MCVector, #MC World Structure for Controller
        joystick_start_block, joystick_end_block, ready_button_block, #MC World block Coords to define virtual input
        controller_sprite:PixelArray, sprite_screen_pos, player_number:int):

        self.__block_structure = mc_blockstructure
        self.__block_structure_start_pos = block_structure_start_pos
        self.__controller_state='unloaded' # one of ['unloaded','loaded','dropin,'ingame','endgame']
        # controller states:
        # 'unloaded' - this is when the game hasn't started yet and controller is waiting for player to step on ready block
        # 'loaded' - game hasn't started, but player is standing on ready block (likely waiting for other player to get on block)
        # 'dropin' - both players are on their ready blocks and the dropIn() is called and drop in timer is started.  This removes the ready block and players fall through to range input pad
        # 'ingame' - once drop in timer is concluded, ready block is replaced and players are on range pads.  range input is now queried

        self.__player_num = player_number
        self.__joystick_input = input_object.RangeInputParser(mc,input_scanner,start_coord=joystick_start_block, end_coord=joystick_end_block)
        self.__ready_button = input_object.TactileInputParser(mc,input_scanner,start_coord=ready_button_block, end_coord=ready_button_block)
        self.__sprite = controller_sprite
        self.__sprite_screen_pos = sprite_screen_pos
        self.__painter = painter[0]
        self.__half_screen_width = int(self.__painter.getScreenWidth()/2)
        self.__rect = Rectangle(sprite_screen_pos+np.array([-.5,0]),np.array([sprite_screen_pos[0]+controller_sprite.getWidth()+.5,sprite_screen_pos[1]-controller_sprite.getHeight()]))
        self.__ready_button_block = ready_button_block
        self.__mc = mc[0]

    def getPlayerNum(self):
        return self.__player_num

    def dropIn(self):
        self.__ready_button.assignPlayer()
        self.__drop_in_timer = Delay(2000)
        self.__drop_in_timer.start()
        self.__joystick_input.assignPlayer(self.__ready_button.getAssignedPlayer())
        self.__mc.setBlock(self.__ready_button_block.get_mcpiVec().x,self.__ready_button_block.get_mcpiVec().y,self.__ready_button_block.get_mcpiVec().z,0)
        self.__controller_state='dropin'

    def readScannerInput(self):

        if self.__controller_state in ['unloaded','loaded']:
            self.__ready_button.readInputScanner()
            if self.__ready_button.getInputValue()==True:
                self.__controller_state='loaded'
            else:
                self.__controller_state='unloaded'

        if self.__controller_state=='dropin':
            if self.__drop_in_timer.getState()==False:
                self.__mc.setBlock(self.__ready_button_block.get_mcpiVec().x,self.__ready_button_block.get_mcpiVec().y,self.__ready_button_block.get_mcpiVec().z,35,7)
                self.__controller_state='ingame'
            
        if self.__controller_state=='ingame':
            self.__joystick_input.readInputScanner()

    def getControllerState(self):
        return self.__controller_state

    def updatePos(self):
        """
        This measures the width o the paddle against the width of the screen and ensures that there is a linear formula such that joystick input value:0 places the paddle at the left edge of the screen and joystick input value 1 places the paddle at the right side of the screen.
        
        We only move the x value (sprite_screen_pos[0] because the ship moves left and right only.)
        """
        self.__sprite_screen_pos[0] = (
            (self.__painter.getScreenWidth()-self.__sprite.getWidth())*
            self.__joystick_input.getInputValue()-self.__half_screen_width
        )
        self.__rect.setCartPos(self.__sprite_screen_pos+np.array([-.5,0]))


    def getDrawData(self):
        print("P1:",self.__joystick_input.getInputValue(), p1_pos[0]," b:",self.__ready_button.getInputValue())


    def draw(self):
        self.__painter.paintSprite(self.__sprite, self.__sprite_screen_pos)

    def getColliderRect(self):
        return self.__rect
    
    def resetController(self):
        """
        This function is called when the game has concluded and is resetting for new players..
        """
        self.__controller_state='unloaded'

class PlayerRectangle(Rectangle):
    def __init__(self, top_left_coord, bottom_right_coord, controller:[Controller], end_game_event:[EndEvent], normal_facing_out=True):
        """
        top_left_coord:             np.array([x,y])     Cartesian Coordinate of upper left end of rectangle
        bottom_right_coord:         np.array([x,y])     Cartesian Coordinate of lower right end of rectangle
        normal_facing_out:          bool                Boolean value to determine whether to make normals face out or in.  Default=True (this would treat the rect where everything inside is solid)
        """
        self._cart_pos = top_left_coord
        self._getDimensions(top_left_coord, bottom_right_coord)
        self._getCornersFromDimensions()
        self._SetRectangle(normal_facing_out)   
        self.__player = controller[0].getPlayerNum()
        self.__end_event = end_game_event

    def collide(self):
        self.__end_event.setWinningPlayer(self.__player)