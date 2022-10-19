from mcpi.minecraft import Minecraft
import numpy as np

class Clipper:
    
    def clip_object_with_edge(sprite, edge, normal_vec):
        """
        sprite: (2d np.array)  This is a 2d array of pixels to render
        edge: (tuple) this is a 2d coordinate of a point that exists on the edge
        normal_vec: (tuple) this is a 2d coordinate that represents the unit vector of the normal of the edge line  (e.g. (1,0)
        """
    
    def clip_object_with_screen:
        #clip with bottom edge
        left_edge = 
        #clip with left edge
        
        #clip with top edge
        
        #clip with right edge

class Renderable:
    def __init__(self, this_array, x, y):
        self.x = x
        self.y= y
        
class Color:
    """
    The Color class uses a Wool block (id=35), to represent the colors of the pixels.  According to the reference: 
    +----------+-------------------+--------------------+
    | Block ID |      Color Name   |    mcpi Block ID   |
    +----------+-------------------+--------------------+
    |    4     |   WOOL_WHITE      |       (35,0)       |
    |    15    |   WOOL_ORANGE     |       (35,1)       |
    |    5     |   WOOL_MAGENTA    |       (35,2)       |
    |    14    |   WOOL_LIGHT_BLUE |       (35,3)       |
    |    13    |   WOOL_YELLOW     |       (35,4)       |
    |    12    |   WOOL_LIME       |       (35,5)       |
    |    11    |   WOOL_PINK       |       (35,6)       |
    |    10    |   WOOL_GREY       |       (35,7)       |
    |    9     |   WOOL_LIGHT_GREY |       (35,8)       |
    |    8     |   WOOL_CYAN       |       (35,9)       |
    |    7     |   WOOL_PURPLE     |       (35,10)      |
    |    2     |   WOOL_BLUE       |       (35,11)      |
    |    6     |   WOOL_BROWN      |       (35,12)      |
    |    1     |   WOOL_GREEN      |       (35,13)      |
    |    3     |   WOOL_RED        |       (35,14)      |
    |    0     |   WOOL_BLACK      |       (35,15)      |
    |    9     |       N/A         |        N/A         |   (Use this for transparent -- skip drawing)   
    +----------+-------------------+--------------------+
    """
    __pixel_color=
    [
        (35,15), #0=black wool
        (35,13), #1=green wool
        (35,11), #2=blue wool
        (35,14), #3=red wool
        (35,0),  #4=white wool  (9=transparent alpha/skip drawing)
        (35,2),  #5=Magenta wool
        (35,12), #6=Brown Wool
        (35,
    ] 
    
    get(color_num):
        """
        This function returns the mcpi wool block color (block_id, data) associated with the integer ID for that color.
        param color_num: (int) This is the integer identifier that will correspond to a tuple for an mcpi block type.
        
        """
        
class Screen:
    width=16
    height=32

    current_screen_array = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #use pixel_color ids at each postion (0=black)
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    
    new_screen_array = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #0=black 1=red 2=blue 3=green
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    
    changes = np.array([])
    
    def cls(self):
        color=0
        for x in range(self.width):
            for y in range(self.height):
                self.mc_connection.setBlock(self.start_position.x,self.start_position.y-y,self.start_position.z+x,Color.pixel_color[color[0]], self.pixel_color[color[1]])        
        
    def __init__(self, mc, start_pos):
        self.start_position = start_pos
        self.mc_connection = mc
        self.height, self.width = self.current_screen_array.shape
        cls
    
    def draw(self):
        print('Drawing')
        