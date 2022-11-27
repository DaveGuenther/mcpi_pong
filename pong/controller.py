from . import input
from .render import Renderer
from .render import PixelArray
from mcpi.minecraft import Minecraft
from .vector import MCVector
from .mcpi_block_structure.blockstructure import BlockStructure

class Controller:
    """
    Associates a blockstructure and screen sprite with an InputInterface object
    mc_block_structure              blockstructure          This is a blockstructure object created from the minecraft world.
    block_structure_start_pos       MCVector                MCVector representation of an x,y,z coordinate of one corner of the cuboid to place in the MC world.  This vector must be at the base of the structure on the NW corner.  If you stand at the corner of the structure and look away from it, and find that you are facing just between north and west, you're on the right corner.
    input_object                    InputInterface          This is an abstract class, referencing either concrete class TactileInput or RangeInput.  It is the 1d input set of blocks that will be used to capture input from the MC World

    """
    def __init__(
        self, mc:[Minecraft], input_scanner:[input.InputScanner], painter:[Renderer], #subsystems as pointers
        mc_blockstructure:BlockStructure, block_structure_start_pos:MCVector, #MC World Structure for Controller
        joystick_start_block, joystick_end_block, ready_button_block, #MC World block Coords to define virtual input
        controller_sprite:PixelArray, sprite_screen_pos):

        self.__block_structure = mc_blockstructure
        self.__block_structure_start_pos = block_structure_start_pos
        self.__controller_state='unloaded' # one of ['unloaded','loaded','ingame','endgame']
        self.__joystick_input = input.RangeInputParser(mc,input_scanner,start_coord=joystick_start_block, end_coord=joystick_end_block)
        self.__ready_button = input.TactileInputParser(mc,input_scanner,start_coord=ready_button_block, end_coord=ready_button_block)
        self.__sprite = controller_sprite
        self.__sprite_screen_pos = sprite_screen_pos
        self.__painter = painter[0]
        self.__half_screen_width = int(self.__painter.getScreenWidth()/2)

    def readScannerInput(self):
        if self.__controller_state=='unloaded':
            self.__ready_button.readInputScanner()
            if self.__ready_button.getInputValue()==True:
                self.__controller_state=='loaded'
        self.__joystick_input.readInputScanner()

    def updatePos(self):
        """
        This measures the width o the paddle against the width of the screen and ensures that there is a linear formula such that joystick input value:0 places the paddle at the left edge of the screen and joystick input value 1 places the paddle at the right side of the screen.
        
        We only move the x value (sprite_screen_pos[0] because the ship moves left and right only.)
        """
        self.__sprite_screen_pos[0] = (
            (self.__painter.getScreenWidth()-self.__sprite.getWidth())*
            self.__joystick_input.getInputValue()-self.__half_screen_width
        )

    def getDrawData(self):
        print("P1:",self.__joystick_input.getInputValue(), p1_pos[0]," b:",self.__ready_button.getInputValue())


    def draw(self):
        self.__painter.paintSprite(self.__sprite, self.__sprite_screen_pos)