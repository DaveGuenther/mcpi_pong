from . import input
from mcpi.minecraft import Minecraft
from .vector import MCVector
from ..mcpi_block_structure.blockstructure import BlockStructure

class Controller:
    def __init__(self, mc:[Minecraft], mc_blockstructure:BlockStructure, block_structure_start_pos:MCVector, input_object:input.InputInterface):
        """
        Associates a blockstructure with an InputInterface object
        mc_block_structure              blockstructure          This is a blockstructure object created from the minecraft world.
        block_structure_start_pos       MCVector                MCVector representation of an x,y,z coordinate of one corner of the cuboid to place in the MC world.  This vector must be at the base of the structure on the NW corner.  If you stand at the corner of the structure and look away from it, and find that you are facing just between north and west, you're on the right corner.
        input_object                    InputInterface          This is an abstract class, referencing either concrete class TactileInput or RangeInput.  It is the 1d input set of blocks that will be used to capture input from the MC World

        """
        self.__block_structure = mc_blockstructure
        self.__block_structure_start_pos = block_structure_start_pos
        self.__inputOjbect = input_object
        self.__block_structure.set_structure(self.__block_structure_start_pos.get_mcpiVec())
        

    def scanInput(self):
        return self.__inputOjbect.scanInput()
        
        

    def getInputValue(self):
        return self.__inputOjbect.getInputValue()