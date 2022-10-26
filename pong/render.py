from mcpi.minecraft import Minecraft
from mcpi import vec3
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

    def __init__(self, mc:[Minecraft], start_pos:vec3.Vec3, width, height):
        """
        mc:             [mcpi.minecraft.Minecraft]  This is an mcpi object wrapped into an array so that it can be mutable (the same mcpi object declared in your program is the same one used in this class, not a copy).
        start_pos:      vec3.Vec3                   This represents the x,y,z coordinates of the top left corner of the screen
        width:          int                         Width in pixels of the screen
        height:         int                         Height in pixels of the screen
        """
        self.__start_position = start_pos
        self.__width=width
        self.__height=height
        self.__front_virtual_page=PixelArray.fromDimensions(self.__width,self.__height)
        self.__back_virtual_page = PixelArray.fromDimensions(self.__width,self.__height)
        self.mc_connection = mc[0]
        self.__clipper=Clipper([self]) 
        

    def fill(self, color):
        """
        This function fills the back virtual page with whatever color is provided.

        color:      tuple   This is a value provided from Color.get() function to render a specific color of wool, or nothing at all.
        """
        for x in range(self.width):
            for y in range(self.height):
                self.__back_virtual_page.setPoint(x, y, color)        
        
    def flipVirtualPage(self):
        """
        This function will take whatever is on the back virtual page and flip it to the front, drawing the pixels on the front page to the as blocks in the minecraft world.
        This is the only function that directly sets blocks in the minecraft world 2D screen in the pong library
        """

        # swap front/back pages
        temp_page = self._back_virtual_page
        self.__back_virtual_page = self._front_virtual_page
        self.__front_virtual_page=temp_page

        #draw front page
        for x in range(self.__width):
            for y in range(self.__height):
                this_color = Color.get(self.__front_virtual_page.getPoint(x, y))
                if this_color!=(0,0): # skip if pixel is transparent
                    self.mc_connection.setBlock(
                        self.__start_position.x,
                        self.__start_position.y-y,
                        self.__start_position.z+x,
                        this_color)

    def drawObject(self, sprite, sprite_start_pos):
        """
        This function draws a sprite to the back virtual page.

        sprite:             PixelArray      This can be any size pixel array (including 1x1)
        sprite_start_pos:   tuple           this is the 2d x,y location on the screen that represents the upper left hand corner of the sprite
        """
        clipped_object = self.__clipper.clip_object_with_screen_edges(sprite, sprite_start_pos)
        #draw front page
        for x in range(clipped_object.getWidth()):
            for y in range(clipped_object.getHeight()):
                this_color = Color.get(clipped_object.getPoint(x,y))
                if this_color!=(0,0): # skip if pixel is transparent
                    self.__back_virtual_page.setPoint(x, y, this_color)
        
        
class Clipper:
    
    def __init__(self,my_screen:[Screen]):
        self.my_screen=my_screen[0]

    def clip_sprite_with_single_edge(self,this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec):
        """
        sprite:                 PixelArray    This is a 2d array of pixels to render
        sprite_start_pos:       tuple         this is the 2d x,y location on the screen that represents the upper left hand corner of the sprite
        screen_edge:            tuple         this is a 2d coordinate of a point that exists on the edge
        screen_edge_normal_vec: tuple         this is a 2d coordinate that represents the unit vector of the normal of the edge line  (e.g. (1,0)
        
        returns a new PixelArray that has been reshaped after clipped with edge
        """
        if screen_edge_normal_vec[1]!=0: #clipping sprite with either bottom or top edge of screen
            elements_not_clipped=np.array([])
            for y in range(this_sprite.getHeight()):
                row = screen_edge[1]+screen_edge_normal_vec[1]*(sprite_start_pos[1]+y) #determines if the row of the sprite falls inside or outside clipped edge
                
                elements_not_clipped = np.append(elements_not_clipped, True) if row>=0 else np.append(elements_not_clipped,False)
            if np.all((elements_not_clipped==True)):
                return this_sprite # nothing was clipped
            else:
                return this_sprite.filter(elements_not_clipped,0)   
                    
        elif screen_edge_normal_vec[0]!=0: # clipping sprite with either left or right edge of screen
            elements_not_clipped=np.array([])
            for x in range(this_sprite.getWidth()):
                column = screen_edge[0]+screen_edge_normal_vec[0]*(sprite_start_pos[0]+x) #determines if the column of the sprite falls inside or outside clipped edge
                elements_not_clipped = np.append(elements_not_clipped, True) if column>=0 else np.append(elements_not_clipped,False)

            if np.all((elements_not_clipped==True)):
                return this_sprite # nothing was clipped
            else:
                return this_sprite.filter(elements_not_clipped,1) 
        
    
    def clip_object_with_screen_edges(self, sprite, sprite_start_pos):
        """
        This function will take a sprite and clipt it with all 4 screen edges, returning at the end a new clipped sprite that will be drawn against the screen.
        """
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
        
        #clip sprite with each edge
        clipped_sprite=sprite.copy()
        for point, normal in zip(edge_points, edge_normals):
            clipped_sprite = self.clip_sprite_with_single_edge(clipped_sprite, point, normal)
        
        return clipped_sprite
            

class PixelArray:
    """
    This class creates an manages a raster of pixels.  Each pixel spot holds an encoded color as shown below:

    0=black wool
    1=green wool
    2=blue wool
    3=red wool
    4=white wool  
    5=Magenta wool
    6=Brown wool
    7=Purple wool
    8=Cyan wool
    9=Transparent/do not draw
    10=Grey wool
    11=Pink wool
    12=Lime wool
    13=Yellow wool
    14=Light Blue wool
    15=Orange wool
    16=Light Grey wool
    """


    def __init__(self, my_array, transpose=True):
        """
        Creates a new PixelArray from an existing array

        my_array:   (numpy.ndarray)     1D or 2D array representing the pixelspace
        transpose:  (boolean)           True if my_array is indexed with [row][col] (it needs to be flipped)
                                        False if my_array is indexed with [col][row] (it gets copied as is)
        """
        if transpose:
            self.data=np.swapaxes(my_array,0,1)
        else:
            self.data=my_array
        
    @classmethod
    def fromDimensions(cls, rows, columns):
        data = np.zeros((columns,rows),dtype=int)
        return cls(data, False)
    
    
    def getPoint(self, x, y):
        """
        Goes to x,y location in PixelArray and gets color there.  Returns that color
        """
        return self.data[y][x]

    def filter(self, indices, axis:int):
        """
        This function will return a new PixelArray that is filtered with specific rows or columns based on an array of boolean values for each row/column

        indices:    (np.array)  1D array with boolean values for each element in the axis.  True will keep the row, False will drop it
        axis:       (int)       This indicates the axis by which to apply the indices boolean array.  value must be either 0 or 1.  0=Rows, 1=columns.
        
        returns a new PixelArray filtered based on boolean element-wise index
        """
        if np.all((indices==True)):
            return self
        else:
            if axis==0: # indexing rows
                this_arr_index =np.tile(indices,(self.getHeight(),1))
                this_arr=self.data[this_arr_index]
                this_arr = this_arr.reshape(self.getHeight(),int(len(this_arr)/self.getHeight()))
                if this_arr.ndim==1: this_arr=np.array([this_arr])
                return PixelArray(my_array=this_arr,transpose=False)
            elif axis==1: # indexing columns
                this_arr_index = np.tile(indices,(self.getWidth(),1)).T
                this_arr=self.data[this_arr_index]
                this_arr = this_arr.reshape(int(len(this_arr)/self.getWidth()),self.getWidth())
                if this_arr.ndim==1: this_arr=np.array([this_arr])
                return PixelArray(my_array=this_arr,transpose=False)
            

    def getWidth(self):
        """
        returns the width of the PixelArray
        """
        return self.data.shape[1]

    def getHeight(self):
        """
        returns the height of the PixelArray
        """
        return self.data.shape[0]

    def setPoint(self, x, y, value):
        """
        Goes to x,y location in array and sets element to value.  Value should be an integer from 0-16
        """
        self.data[y][x]=int(value)

    def fillArray(self, color_code):
        self.data.fill(color_code)

    def toString(self):
        print(self.data.T)
