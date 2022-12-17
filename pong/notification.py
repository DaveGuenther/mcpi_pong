import numpy as np
from .render import PixelArray

class Notification:

    __data={
        'p1_waiting':PixelArray(np.array(
            [
                [9,2,2,2,9],
                [2,9,9,9,2],
                [9,9,9,9,2],
                [9,9,9,9,2],
                [9,9,9,2,9],
                [9,9,2,9,9],
                [9,9,2,9,9],
                [9,9,9,9,9],
                [9,9,2,9,9]
            ])),
        'p2_waiting':PixelArray(np.array(
            [
                [ 9,15,15,15, 9],
                [15, 9, 9, 9,15],
                [ 9, 9, 9, 9,15],
                [ 9, 9, 9, 9,15],
                [ 9, 9, 9,15, 9],
                [ 9, 9,15, 9, 9],
                [ 9, 9,15, 9, 9],
                [ 9, 9, 9, 9, 9],
                [ 9, 9,15, 9, 9]
            ])),
        'p1_loaded':PixelArray(np.array(
            [
                [ 9, 9, 2, 9, 9],
                [ 9, 2, 2, 2, 9],
                [ 9, 2, 2, 2, 9],
                [ 9, 9, 2, 9, 9],
                [ 9, 2, 2, 2, 9],
                [ 2, 9, 2, 9, 2],
                [ 2, 9, 2, 9, 2],
                [ 9, 9, 2, 9, 9],
                [ 9, 2, 9, 2, 9],
                [ 2, 2, 9, 2, 2]
            ])),
        'p2_loaded':PixelArray(np.array(
            [
                [ 9, 9,15, 9, 9],
                [ 9,15,15,15, 9],
                [ 9,15,15,15, 9],
                [ 9, 9,15, 9, 9],
                [ 9,15,15,15, 9],
                [15, 9,15, 9,15],
                [15, 9,15, 9,15],
                [ 9, 9,15, 9, 9],
                [ 9,15, 9,15, 9],
                [15,15, 9,15,15]
            ]))
        }
       
    def __init__(self, painter, x:float, y:float, bitmap='p1_waiting'):
        self.__painter = painter[0]
        self.__cart_x = x
        self.__cart_y = y
        self.__bitmap = self.__data[bitmap]


    def put_char(character, x=4, y=10, transparent=False):
        """
        
        :param character: (single character string)  This is the character that will be printed on the screen
        :param x: (int) This is the x position on the display for the top left corner of the character
        :param y: (int) this is the y position on the display for the top left corner of the character
        
        """
        #:param center(x, y):  (tuple) This is the screen coordinates of the center of the character to be displayed
        #:param scale=1: (float) 1 is unity scale.  <1 is smaller and >1 is bigger
        #:param rot: (float) degrees to rotate CCW
    
        
        char_array = self.data[character]
        
        