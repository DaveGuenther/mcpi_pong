class CartisianPlane:
    
    def __init__(self, screen):
        self.my_screen = screen[0]
        self.screen_width = self.my_screen.getWidth()
        self.screen_height = self.my_screen.getHeight()
    
    def screenToCart(vec):
        """
        Takes a 2d vector with screen coordinates (top left is 0,0 and bottom right is screen_width, screen_height), and converts to cartesian coordinates with origin in the center of the screen.
        
        vec         tuple/2darray       2d vector representing screen coordinates
        
        returns     tuple               2d vector representing caretsian coordinates
        """
        cart_x = (self.screen_width/2)-((self.screen_width-1)/x)
        cart_y = (self.screen_height/2)-((self.screen_height-1)/x)
        return (cart_x, cart_y)

    
    def cartToScreen(x,y):
        """
        Takes a 2d vector with cartesian coordinates (top of visible plane is 1.0, bottom is -1.0, left and right are calculated based on the aspect ratio of the screen_width and screen_height), and converts those coordinates to Screen coordinates (top left is 0,0).
        
        vec         tuple/2darray       2d vector representing cartesian coordinates
        
        returns     tuple               2d vector representing screen coordinates
        """
        screen_x = 1/((-1*x+(self.screen_width/2))/(self.screen_width-1))  # Thanks Raju and Kimbra :)
        screen_y = 1/((-1*y+(self.screen_height/2))/(self.screen_height-1))
        return (screen_x, screen_y)

my_vec = (0,0)
screen_width=16
screen_height=32


cart_x = (screen_width/2)-((screen_width-1)-my_vec[0])
cart_y = (screen_height/2)-((screen_height-1)-my_vec[1])
print (cart_x, cart_y)

screen_x = 1/((-1*my_vec[0]+(screen_width/2))/(screen_width-1))  # Thanks Raju and Kimbra :)
screen_y = 1/((-1*my_vec[1]+(screen_height/2))/(screen_height-1))
print (screen_x, screen_y)