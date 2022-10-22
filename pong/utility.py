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
        Goes to x,y location in PixelArray and gets element there.  Returns that element
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