from mcpi import vec3
import numpy as np

def get_world_coords_from_mcpi_vec(this_vec):
    this_vec.x-=32
    this_vec.y+=66
    this_vec.z+=128
    return vec3.Vec3(x,y,z)    

def get_mcpi_vec_from_world_coords(x, y, z):
    x+=32
    y-=66
    z-=128
    return vec3.Vec3(x,y,z)    

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

    def __init__(self, rows, columns):
        self.data = np.zeros((columns,rows),dtype=int)
    
    def getPoint(self, x, y):
        """
        Goes to x,y location in PixelArray and gets element there.  Returns that element
        """
        return self.data[y][x]

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
