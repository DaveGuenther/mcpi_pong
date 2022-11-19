from mcpi.minecraft import Minecraft
from mcpi import vec3
from .vector import MCVector
import numpy as np
import abc

class InputInterface(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self,MC,start_coord, end_coord):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        MC:                     [mcpi.Minecraft]    The mcpi connection instance (mutable)
        start_coord:            MCWorldVec          Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec          End coordinate (MC World Coordinate) for input block range
        """
        pass

    @abc.abstractclassmethod
    def _constructVirtualPadFromEndBlocks(self):
        """
        Pads can be defined with arbitrary dimensions.  While we hope they exist as a single slick or a line of blocks, we will define them as planes with two corner blocks (start_block_ and end_block).  This function will build an np.array of MCVectors that contains all the blocks in the virtual pad, which is an xy plane.
        """
        pass

    @abc.abstractclassmethod
    def getPressed(self):
        """
        Get current state of the input controller (from private data)
        """
        pass

    @abc.abstractclassmethod
    def scanInput(self):
        """
        Get input data by querying MC
        """
        pass

    @abc.abstractclassmethod
    def getBlockRange(self):
        pass

    @abc.abstractclassmethod
    def setBlockRange(start_coord, end_coord):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        start_coord:            MCWorldVec      Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec      End coordinate (MC World Coordinate) for input block range
        """
        pass

    def _vec_swap(self, vec_1, vec_2):
        temp=vec_1
        vec_1=vec_2
        vec_2=temp
        return (vec_1, vec_2)

    @abc.abstractclassmethod
    def getBlockRange(self):
        pass


class TactileInput(InputInterface):

    def __init__(self, MC:[Minecraft], start_coord:MCVector, end_coord:MCVector):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input

        MC:                     [mcpi.Minecraft]    The mcpi connection instance (mutable)
        start_coord:            MCVector      Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCVector      End coordinate (MC World Coordinate) for input block range
        """
        #convert World to mcpi Vecs
        self._start_block = start_coord.get_MCWorld_Vec()
        self._end_block = end_coord.get_MCWorld_Vec()        
        assert self._end_block.y==self._end_block.y, f"virtual input pad must be defined on a flat plane where start and end y block coordinates are the same"
        self._MC = MC[0]
        self._pressed=False
        self._constructVirtualPadFromEndBlocks()

    def _constructVirtualPadFromEndBlocks(self):
        """
        Pads can be defined with arbitrary dimensions.  While we hope they exist as a single slick or a line of blocks, we will define them as planes with two corner blocks (start_block_ and end_block).  This function will build an np.array of MCVectors that contains all the blocks in the virtual pad, which is an xy plane.
        """
        #re-order blocks so that start block is less or equal to end block
        if self._end_block.x<self._start_block.x: 
            self._start_block, self._end_block=self._vec_swap(self._start_block, self._end_block)
        if self._end_block.z<self._start_block.z:
            self._start_block, self._end_block=self._vec_swap(self._start_block, self._end_block)


        x_range = self._end_block.x - self._start_block.x+1
        z_range = self._end_block.z-self._start_block.z+1
        self._block_array = np.empty((x_range,z_range), dtype=object)
        for x in range(x_range):
            for z in range(z_range):
                self._block_array[x][z]=vec3.Vec3(self._start_block.x+x, self._start_block.y, self._start_block.z+z)



    def getPressed(self):
        """
        
        """
        pass

    def scanInput(self):
        player_ids = Minecraft(self._MC).getPlayerEntityIds()
        for player in player_ids:
            tilepos = MCVector.from_MCWorld_Vec(Minecraft(self._MC).entity.getTilePos(player_id))
            
        pass

    def getBlockRange(self):
        pass

    def setBlockRange(self, start_coord, end_coord):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        start_coord:            MCWorldVec      Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec      End coordinate (MC World Coordinate) for input block range
        """
        pass

    def getBlockRange(self):
        pass


