import numpy as np
from .render import PixelArray
from .timer import SquareWave

class Notification:

    __data={
        'p1_waiting':PixelArray(np.array(
            [
                [0,2,2,2,0],
                [2,0,0,0,2],
                [0,0,0,0,2],
                [0,0,0,2,0],
                [0,0,2,0,0],
                [0,0,0,0,0],
                [0,0,2,0,0]
            ])),
        'p2_waiting':PixelArray(np.array(
            [
                [ 0,15,15,15, 0],
                [15, 0, 0, 0,15],
                [ 0, 0, 0, 0,15],
                [ 0, 0, 0,15, 0],
                [ 0, 0,15, 0, 0],
                [ 0, 0, 0, 0, 0],
                [ 0, 0,15, 0, 0]
            ])),
        'p1_loaded':PixelArray(np.array(
            [
                [ 0, 2, 2, 2, 0],
                [ 0, 2, 2, 2, 0],
                [ 0, 0, 2, 0, 0],
                [ 0, 2, 2, 2, 0],
                [ 2, 0, 2, 0, 2],
                [ 2, 0, 2, 0, 2],
                [ 0, 0, 2, 0, 0],
                [ 0, 2, 0, 2, 0],
                [ 2, 2, 0, 2, 2]
            ])),
        'p2_loaded':PixelArray(np.array(
            [
                [ 0,15,15,15, 0],
                [ 0,15,15,15, 0],
                [ 0, 0,15, 0, 0],
                [ 0,15,15,15, 0],
                [15, 0,15, 0,15],
                [15, 0,15, 0,15],
                [ 0, 0,15, 0, 0],
                [ 0,15, 0,15, 0],
                [15,15, 0,15,15]
            ])),
        'P':PixelArray(np.array(
            [
                [ 4, 4, 4, 0],
                [ 4, 0, 0, 4],
                [ 4, 0, 0, 4],
                [ 4, 4, 4, 0],
                [ 4, 0, 0, 0],
                [ 4, 0, 0, 0],
                [ 4, 0, 0, 0]

            ])),
        '1':PixelArray(np.array(
            [
                [ 0, 4, 0],
                [ 4, 4, 0],
                [ 0, 4, 0],
                [ 0, 4, 0],
                [ 0, 4, 0],
                [ 0, 4, 0],
                [ 4, 4, 4]
            ])),
        '2':PixelArray(np.array(
            [
                [ 0, 4, 4, 4, 0],
                [ 4, 0, 0, 0, 4],
                [ 0, 0, 0, 0, 4],
                [ 0, 0, 4, 4, 0],
                [ 0, 4, 0, 0, 0],
                [ 4, 0, 0, 0, 0],
                [ 4, 4, 4, 4, 4]
            ])),
        '3':PixelArray(np.array(
            [
                [ 0, 4, 4, 4, 0],
                [ 4, 0, 0, 0, 4],
                [ 0, 0, 0, 0, 4],
                [ 0, 0, 4, 4, 0],
                [ 0, 0, 0, 0, 4],
                [ 4, 0, 0, 0, 4],
                [ 0, 4, 4, 4, 0]
            ])),
        'WIN':PixelArray(np.array(
            [
                [ 4, 0, 0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 4],
                [ 4, 0, 0, 0, 4, 0, 4, 0, 4, 4, 0, 0, 4],
                [ 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4, 0, 4],
                [ 0, 4, 0, 4, 0, 0, 4, 0, 4, 0, 4, 0, 4],
                [ 0, 4, 0, 4, 0, 0, 4, 0, 4, 0, 0, 4, 4]
            ])),
        'python':PixelArray(np.array(
            [
                [ 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0],
                [ 0, 0, 0, 2, 0, 2, 2, 2, 0, 0, 0],
                [ 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0],
                [ 0, 0, 0, 0, 0, 0, 2, 2,13,13, 0],
                [ 0, 2, 2, 2, 2, 2, 2, 2,13,13,13],
                [ 2, 2, 2, 2, 2, 2, 2,13,13,13,13],
                [ 2, 2, 2, 2,13,13,13,13,13,13,13],
                [ 2, 2, 2,13,13,13,13,13,13,13, 0],
                [ 0, 2, 2,13,13, 0, 0, 0, 0, 0, 0],
                [ 0, 0, 0,13,13,13,13,13, 0, 0, 0],
                [ 0, 0, 0,13,13,13, 0,13, 0, 0, 0],
                [ 0, 0, 0, 0,13,13,13, 0, 0, 0, 0]
            ]))
        }
       
    def __init__(self, painter, cart_pos, bitmap='p1_waiting', flashing=False, period=1000):
        """
        painter:        [Renderer]          Renderer instance.  This is placed in a list as a pointer
        cart_pos:       np.array([x,y])     Cartesian point to the top left of the sprite
        bitmap:         string              dictionary lookup of preloaded sprite to use
        flashing:       bool                True if the bitmap needs to flash on the screen, False if it should just be displayed
        period:         int                 Period in ms for flashing bitmaps
        """
        self.__painter = painter[0]
        self.__cart_pos = cart_pos
        self.__bitmap = self.__data[bitmap]
        self.__bitmap_off = PixelArray.fromDimensions(self.__bitmap.getWidth(), self.__bitmap.getHeight())
        self.__flashing = flashing
        if flashing:
            self.__timer = SquareWave(period)


    def removeImage(self):
        self.__painter.paintSprite(self.__bitmap_off, self.__cart_pos)


    def draw(self):
        if self.__flashing:
            # show/hide graphic based on timer state
            self.__timer.update()
            if self.__timer.getState()==True:
                # draw the sprite
                self.__painter.paintSprite(self.__bitmap, self.__cart_pos)
            else:
                # remove the sprite
                self.removeImage()
        else:
            # image is static
            self.__painter.paintSprite(self.__bitmap, self.__cart_pos)
        