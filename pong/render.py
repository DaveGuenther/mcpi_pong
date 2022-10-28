from mcpi.minecraft import Minecraft
from mcpi import vec3
import numpy as np

      
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
    Manages the Screen that we will draw on.  Pixels must all fall within the x,y coordinates of the defined screen space.
    The screen has two virtual pages to help optimize drawing.  A back page and a front page.  When moving
    from the current state to new state, we only adjust the pixels that have changed and nother else.  This way we limit the number of drawn blocks in Minecraft
    
    The term "Active" page, refers to the page that is active for drawing on.  This is the Back Page at all times.  The Front Page, while shown to the user is not available for drawing
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
        

    def fill(self, color:int):
        """
        This function fills the back virtual page with whatever color is provided.

        color:      int   This is a encoded color value from Color class.  It represents a specific color of wool, or nothing at all.
        """
        for x in range(self.getWidth()):
            for y in range(self.getHeight()):
                self.__back_virtual_page.setPoint(x, y, color)        
        
    def removeUnchangedBlocksFromRedraw(self):
        """
        This method should be called just before calling flipVirtualPage.  It does a pixel-for-pixel comparison of the back page and front page.  For each position that hasn't changed its Color value, the screen puts in its place on the back page a Color value of 9 (transparent).  This eliminates redrawing of pixels.
        """
        for x in range(self.getWidth()):
            for y in range(self.getHeight()):
                if self.__front_virtual_page.getPoint(x,y)==self.__back_virtual_page.getPoint(x, y):
                    self.__back_virtual_page.setPoint(x, y, 9) # Set pixel to transparent

    def flipVirtualPage(self):
        """
        This function will take whatever is on the back virtual page and flip it to the front, drawing the pixels on the front page to the as blocks in the minecraft world.
        This is the only function that directly sets blocks in the minecraft world 2D screen in the pong library
        """

        # swap front/back pages
        temp_page = self.__back_virtual_page
        self.__back_virtual_page = self.__front_virtual_page
        self.__front_virtual_page=temp_page

        #draw front page
        for x in range(self.getWidth()):
            for y in range(self.getHeight()):
                this_color = Color.get(self.__front_virtual_page.getPoint(x, y))
                #if this_color!=(0,0): # skip if pixel is transparent
                #    self.mc_connection.setBlock(
                #        self.__start_position.x,
                #        self.__start_position.y-y,
                #        self.__start_position.z+x,
                #        this_color)

    def drawObject(self, clipped_sprite, sprite_start_pos):
        """
        This function draws a sprite to the back virtual page.

        sprite:             PixelArray      This can be any size pixel array (including 1x1)
        sprite_start_pos:   tuple           this is the 2d x,y location on the screen that represents the upper left hand corner of the sprite
        """
        #clipped_object = self.__clipper.clipObjectWithScreenEdges(sprite, sprite_start_pos)
        #draw on back (active) page
        for x in range(clipped_sprite.getWidth()):
            for y in range(clipped_sprite.getHeight()):
                this_encoded_color = clipped_sprite.getPoint(x,y)
                this_decoded_color = Color.get(this_encoded_color)
                self.__back_virtual_page.setPoint(x+sprite_start_pos[0], y+sprite_start_pos[1], this_encoded_color)
    
    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getBackVirtualPage(self):
        return self.__back_virtual_page

    def getFrontVirtualPage(self):
        return self.__front_virtual_page   
        
class Clipper:
    
    def __init__(self,my_screen:[Screen]):
        self.my_screen=my_screen[0]

    def clipSpriteWithSingleEdge(self,this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec):
        """
        sprite:                 PixelArray    This is a 2d array of pixels to render
        sprite_start_pos:       tuple         this is the 2d x,y location on the screen that represents the upper left hand corner of the sprite
        screen_edge:            tuple         this is a 2d coordinate of a point that exists on the edge
        screen_edge_normal_vec: tuple         this is a 2d coordinate that represents the unit vector of the normal of the edge line  (e.g. (1,0)
        
        returns a tuple (PixelArray, tuple): 
            - The PixelArray represents the clipped sprite with the screen edge
            - The tuple is an adjusted sprite_start_pos coordinate (it's only adjusted if the top or left of the sprite were clipped)
        """
        new_sprite_start_pos=sprite_start_pos
        if (screen_edge_normal_vec[1]!=0)&(this_sprite.getSize()>0): #clipping rows of sprite with either bottom or top edge of screen
            elements_not_clipped=np.array([], dtype=bool)
            for y in range(this_sprite.getHeight()):
                row = screen_edge[1]+screen_edge_normal_vec[1]*(sprite_start_pos[1]+y) #determines if the row of the sprite falls inside or outside clipped edge
                
                elements_not_clipped = np.append(elements_not_clipped, True) if row>=0 else np.append(elements_not_clipped,False)
            
            #offset start coordinate of sprite if clipping with plane requires it
            amount_to_offset = len(elements_not_clipped)-elements_not_clipped.sum()
            if (
                (amount_to_offset>0)&
                (amount_to_offset!=this_sprite.getHeight())&
                (elements_not_clipped[0]==False)):
                new_sprite_start_pos = (
                    new_sprite_start_pos[0],
                    new_sprite_start_pos[1]-(-1*screen_edge_normal_vec[1]*(amount_to_offset))
                )
            elif (amount_to_offset==this_sprite.getHeight()): #all columns are clipped and nothing should be shown
                new_sprite_start_pos = (
                    new_sprite_start_pos[1],
                    0
                )

            if np.all((elements_not_clipped==True)):
                return (this_sprite, sprite_start_pos) # nothing was clipped
            else:
                return (this_sprite.filter(elements_not_clipped,0), new_sprite_start_pos)   # clipping rows
                    
        elif (screen_edge_normal_vec[0]!=0)&(this_sprite.getSize()>0): # clipping columns of sprite with either left or right edge of screen
            elements_not_clipped=np.array([], dtype=bool)
            for x in range(this_sprite.getWidth()):
                column = screen_edge[0]+screen_edge_normal_vec[0]*(sprite_start_pos[0]+x) #determines if the column of the sprite falls inside or outside clipped edge
                elements_not_clipped = np.append(elements_not_clipped, True) if column>=0 else np.append(elements_not_clipped,False)

            amount_to_offset = len(elements_not_clipped)-elements_not_clipped.sum()
            if (
                (amount_to_offset>0)&
                (amount_to_offset!=this_sprite.getWidth())&
                (elements_not_clipped[0]==False)
                ):
                new_sprite_start_pos = (
                    new_sprite_start_pos[0]-(-1*screen_edge_normal_vec[0]*(amount_to_offset)),
                    new_sprite_start_pos[1]
                )
            elif (amount_to_offset==this_sprite.getWidth()): #all columns are clipped and nothing should be shown
                new_sprite_start_pos = (
                    0,
                    new_sprite_start_pos[1]
                )


            if np.all((elements_not_clipped==True)):
                return (this_sprite, sprite_start_pos) # nothing was clipped
            else:
                return (this_sprite.filter(elements_not_clipped,1), new_sprite_start_pos) # clipping columns
        else:
            return (this_sprite, (0,0))
    
    def clipObjectWithScreenEdges(self, sprite, sprite_start_pos):
        """
        This function will take a sprite and start position of the sprite on the vitrual page and clip it with all 4 screen edges, returning at the end a new clipped sprite and start position that will be drawn against the screen.
        sprite:             PixelArray      sprite to be clipped with the screen edges
        sprite_start_pos:   tuple           this is a coordinate representing the top left corner of the sprite

        returns a tuple (PixelArray, tuple)
            - The PixelArray represents the clipped sprite with the screen edge
            - The tuple is an adjusted sprite_start_pos coordinate (it's only adjusted if the top or left of the sprite were clipped)        
        """
        edge_points = [
            (0,self.my_screen.getHeight()-1),     # bottom
            (0,0),                                  # left
            (0,0),                                  # top
            (self.my_screen.getWidth()-1,0)       # right
        ]
        
        edge_normals = [
            (0,-1),                             # bottom
            (1,0),                              # left
            (0,1),                              # top
            (-1,0)                              # right
        ]
        
        #clip sprite with each edge
        clipped_sprite=sprite
        for point, normal in zip(edge_points, edge_normals):
            clipped_sprite, sprite_start_pos = self.clipSpriteWithSingleEdge(clipped_sprite, sprite_start_pos, point, normal)
        
        return (clipped_sprite, sprite_start_pos)
            

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
        if (transpose)&(my_array.ndim>1):
            self.__data=np.swapaxes(my_array,0,1)
        else:
            self.__data=my_array
        
    @classmethod
    def fromDimensions(cls, rows, columns):
        data = np.zeros((columns,rows),dtype=int)
        return cls(data, True)
    
    
    def getPoint(self, x, y):
        """
        Goes to x,y location in PixelArray and gets color there.  Returns that color
        """
        return self.__data[x][y]

    def filter(self, indices, axis:int):
        """
        This function will return a new PixelArray that is filtered with specific rows or columns based on an array of boolean values for each row/column

        indices:    (np.array)  1D array with boolean values for each element in the axis.  True will keep the row, False will drop it
        axis:       (int)       This indicates the axis by which to apply the indices boolean array.  value must be either 0 or 1.  0=Rows, 1=columns.
        
        returns a new PixelArray filtered based on boolean element-wise index
        """
        if np.all((indices==True)): # none of sprite is clipped
            return self
        elif np.all((indices==False)): # whole sprite is clipped
            empty_array=np.array([])
            return PixelArray(my_array=empty_array,transpose=False)
        else: # some part of sprite is clipped
            if axis==0: # indexing rows
                this_arr_index =np.tile(indices,(self.getWidth(),1))
                this_arr=self.__data[this_arr_index]
                this_arr = this_arr.reshape(self.getWidth(),int(len(this_arr)/self.getWidth()))
                if this_arr.ndim==1: this_arr=np.array([this_arr])
                return PixelArray(my_array=this_arr,transpose=False)
            elif axis==1: # indexing columns
                this_arr_index = np.tile(indices,(self.getHeight(),1)).T
                this_arr=self.__data[this_arr_index]
                this_arr = this_arr.reshape(int(len(this_arr)/self.getHeight()),self.getHeight())
                if this_arr.ndim==1: this_arr=np.array([this_arr])
                return PixelArray(my_array=this_arr,transpose=False)
            

    def getWidth(self):
        """
        returns the width of the PixelArray
        """
        if self.__data.size>0:
            return self.__data.shape[0]
        else:
            return 0


    def getHeight(self):
        """
        returns the height of the PixelArray
        """
        if self.__data.size>0:
            return self.__data.shape[1]
        else:
            return 0


    def getSize(self):
        return self.__data.size

    def setPoint(self, x:int, y:int, value:int):
        """
        Goes to x,y location in array and sets element to value.  Value should be an integer from 0-16
        """
        self.__data[x][y]=int(value)

    def fillArray(self, color_code):
        self.__data.fill(color_code)

    def getData(self):
        return self.__data

    def toString(self):
        print(self.__data.T)

class Painter:
    """
    This class accepts a Screen object, creates a Clipper object, and then manages the application of sprites through the clipper onto the screen.
    """

    def __init__(self,my_screen:[Screen]):
        self.__my_screen=my_screen[0]
        self.__clipper=Clipper(self.__my_screen) 
    
    def paintSprite(self, my_sprite, sprite_pos):
        """
        This method takes a sprite object, passes it through the Clipper class and then finally applies it to the Screen's active virtual page
        my_sprite:          PixelArray      This is the sprite object to paint
        sprite_pos:         tuple           This is the top left coordinate of the sprite object in Screen space
        
        """
        
        my_clipped_sprite, clipped_sprite_pos = self.__clipper.clipObjectWithScreenEdges(my_sprite, sprite_pos)
        
