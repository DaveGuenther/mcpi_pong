from mcpi.minecraft import Minecraft
from mcpi import vec3
from pong.utility import PixelArray
import numpy as np


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
    |    16    |   WOOL_LIGHT_GREY |       (35,8)       |
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

    __pixel_color=[
        (35,15), #0=black wool
        (35,13), #1=green wool
        (35,11), #2=blue wool
        (35,14), #3=red wool
        (35,0),  #4=white wool  
        (35,2),  #5=Magenta wool
        (35,12), #6=Brown wool
        (35,10), #7=Purple wool
        (35,9),  #8=Cyan wool
        (0,0),   #9=Transparent/do not draw
        (35,7),  #10=Grey wool
        (35,6),  #11=Pink wool
        (35,5),  #12=Lime wool
        (35,4),  #13=Yellow wool
        (35,3),  #14=Light Blue wool
        (35,1),  #15=Orange wool
        (35,8)   #16=Light Grey wool
    ]
    
    def get(color_num):
        """
        This function returns the mcpi wool block color (block_id, data) associated with the integer ID for that color.
        param color_num: (int) This is the integer identifier that will correspond to a tuple for an mcpi block type.
        
        """
        return Color.__pixel_color[color_num]
        
class Screen:
    """
    Manages the Screen that we will draw on.  We can place pixels anywhere, but it will only draw on the screen dimensions that we have provided.
    The screen has three virtual pages to help optimize drawing.  A current state, a new state, and a changes array to identify any pixel changes.  When moving
    from the current state to new state, we only adjust the pixels that have changed and nother else.  This way we limit the number of drawn blocks in Minecraft
    """

    changes = np.array([])

    def __init__(self, mc:Minecraft, start_pos:vec3.Vec3, width, height):
        self.start_position = start_pos
        self.width=width
        self.height=height
        self.current_screen_array=PixelArray(self.width,self.height)
        self.new_screen_array = PixelArray(self.width,self.height)
        self.mc_connection = mc
        self._clipper=Clipper(self)
        cls

    def cls(self):
        color=0
        for x in range(self.width):
            for y in range(self.height):
                self.mc_connection.setBlock(self.start_position.x,self.start_position.y-y,self.start_position.z+x,Color.pixel_color[color[0]], self.pixel_color[color[1]])        
        

    def draw(self):
        print('Drawing')
        
class Clipper:
    
    def __init__(self,my_screen:Screen):
        self.my_screen=my_screen

    def clip_object_with_edge(self,sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec):
        """
        sprite:                 (PixelArray)    This is a 2d array of pixels to render
        sprite_start_pos:       (tuple)         this is the 2d x,y location on the screen that represents the upper left hand corner of the sprite
        screen_edge:            (tuple)         this is a 2d coordinate of a point that exists on the edge
        screen_edge_normal_vec: (tuple)         this is a 2d coordinate that represents the unit vector of the normal of the edge line  (e.g. (1,0)
        
        returns a new PixelArray that has been reshaped after clipped with edge
        """
        if normal_vec[1]!=0: #clipping sprite with either bottom or top edge of screen
            rows_not_clipped=np.array([])
            for y in range(sprite.getHeight()):
                row = screen_edge[1]+screen_edge_normal[1]*(sprite_start_pos[1]+y)
                np.append(True) if row>=0 else np.append(False)
            if np.all((rows_not_clipped==True)):
                return sprite # nothing was clipped
            else:
                pass    
                    
        elif normal_vec[0]!=0: # clipping sprite with either left or right edge of screen
            for x in range(sprite.getWidth()):
                column = screen_edge[0]+screen_edge_normal[0]*(sprite_start_pos[0]+x)

        
    
    def clip_object_with_screen(self, sprite):
        edge_points = [
            (0,self.pixel_array.getHeight()-1),     # bottom
            (0,0),                                  # left
            (0,0),                                  # top
            (self.pixel_array.getWidth()-1,0)       # right
        ]
        
        edge_normals = [
            (0,-1),                             # bottom
            (1,0),                              # left
            (0,1),                              # top
            (-1,0)                              # right
        ]
        
        for point, normal in zip(edge_points, edge_normals):
            self.clip_object_with_edge(sprite, point, normal)
            

        #clip with bottom edge
        bottom_edge = (0,0)
        left_normal = (1,0)
        
        #clip with left edge

        left_edge = (0,0)
        left_normal = (1,0)
        
        #clip with top edge
        
        #clip with right edge
