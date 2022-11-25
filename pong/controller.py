from . import input
from ..mcpi_block_structure import blockstructure

class Controller:
    def __init__(self, mc_blockstructure:blockstructure, block_structure_start_pos:MCVector, input_object:input.InputInterface):
        """
        Associates a blockstructure with an InputInterface object
        mc_block_structure              blockstructure          This is a blockstructure object created from the minecraft world.
        block_structure_start_pos       MCVector                MCVector representation of an x,y,z coordinate of one corner of the cuboid to place in the MC world.  This vector must be at the base of the structure on the NW corner.  If you stand at the corner of the structure and look away from it, and find that you are facing just between north and west, you're on the right corner.
        
        """