import numpy as np
from matrix_tools import MatrixTools


class CoordinateTools:
    
    def __init__(self, screen):
        self.my_screen = screen[0]
        self.half_screen_width = float(self.my_screen.getWidth()/2)
        self.half_screen_height = float(self.my_screen.getHeight()/2)
        self.aspect_ratio = float(self.my_screen.getWidth()/self.my_screen.getHeight())

    def screenToCart(vec):
        """
        Takes a 2d vector with screen coordinates (top left is 0,0 and bottom right is screen_width, screen_height), and converts to cartesian coordinates with origin in the center of the screen.
        
        vec         tuple/2darray       2d vector representing screen coordinates
        
        returns     tuple               2d vector representing caretsian coordinates
        """
        cart_coords=np.array(
            [
                [float(1/self.aspect_ratio),0],
                [0,1]
            ]
        )

        offset = np.array([self.half_screen_width/self.aspect_ratio,self.half_screen_height])
        screen_coords = np.matmul(cart_coords,vec)+offset

        #cart_x=(vec[0]-(self.width/2))/(self.screen_width/self.screen_height)
        #cart_y=(vec[1]-(self.height/2))
        return (cart_x, cart_y)

    
    def cartToScreen(vec):
        """
        Takes a 2d vector with cartesian coordinates (top of visible plane is 1.0, bottom is -1.0, left and right are calculated based on the aspect ratio of the screen_width and screen_height), and converts those coordinates to Screen coordinates (top left is 0,0).
        
        vec         tuple/2darray       2d vector representing cartesian coordinates
        
        returns     tuple               2d vector representing screen coordinates
        """
        screen_coords = np.array(
            [
                [self.aspect_ratio, 0],
                [0,1]
            ]
        )
        offset = np.array([self.half_screen_width, self.half_screen_height])
        cart_coords = np.matmul(screen_coords,vec)+offset
        #screen_x=(self.width/2)+(vec[0]*(self.screen_width/self.screen_height))
        #screen_y=(screen.height/2)+vec[1]
        return (screen_x, screen_y)
