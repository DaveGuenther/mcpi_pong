from .render import Renderer

class Engine():

    
    def __init__(self,mc:[Minecraft],start_screen_pos, width:int, height:int, type='screen'):
        self.__width=width
        self.__height=height
        self.__mc=mc[0]
        self.__renderer=Renderer(mc,start_screen_pos,width,heigth)

    


