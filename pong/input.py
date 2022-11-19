from mcpi.minecraft import Minecraft
from mcpi import vec3
from .vector import MCVector
import numpy as np
import abc


class MCVectorError(RuntimeError):
    pass

class InputInterface(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self, MC:[Minecraft], start_coord:MCVector, end_coord:MCVector):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        MC:                     [mcpi.Minecraft]    The mcpi connection instance (mutable)
        start_coord:            MCWorldVec          Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec          End coordinate (MC World Coordinate) for input block range
        """
        pass

    def _constructVirtualPadFromEndBlocks(self):
        """
        Pads can be defined with arbitrary dimensions.  While we hope they exist as a single slick or a line of blocks, we will define them as planes with two corner blocks (start_block_ and end_block).  This function will build an np.array of MCVectors that contains all the blocks in the virtual pad, which is an xy plane.
        """
        #determine direction of block vector, number of blocks in block vector, using MCworldcoords
        start_block = self._start_block.get_MCWorld_Vec()
        end_block = self._end_block.get_MCWorld_Vec()
        unit_vec = vec3.Vec3(end_block.x-start_block.x,end_block.y-start_block.y, end_block.z-start_block.z)
        blockrange=0
        increment=1
        axis=vec3.Vec3(0,0,0)
        if ((unit_vec.x==0)&(unit_vec.y==0)):
            blockrange=unit_vec.z
            increment=1 if blockrange>=0 else -1
            axis.z = 1 # z axis
        elif ((unit_vec.z==0)&(unit_vec.y==0)):
            blockrange=unit_vec.x
            increment=-1 if blockrange<0 else 1
            axis.x = 1 #x axis
        else:
            raise MCVectorError('Failed to initialize a virtual controller surface from start and end coordiates.  Start and end vector y values must match.  Similarly one other axis in both vectors must match.')

        #create array of vec3.Vec3 coordinates
        self._block_array = np.empty(abs(blockrange)+1, dtype=object)
        for offset,i in zip(range(0,blockrange+increment,increment),range(0,abs(blockrange)+1,1)):
            self._block_array[i]=MCVector.from_MCWorld_Vec(vec3.Vec3(start_block.x+(offset*axis.x), start_block.y+(offset*axis.y), start_block.z+(offset*axis.z)))

    @abc.abstractclassmethod
    def getInputValue(self):
        """
        Get current state of the input controller (from private data)
        """
        pass

    def scanInput(self):
        """
        Get input data by querying MC and stores the input value (accessible by getInvputValue())
        """
        pass


    def setBlockRange(self, start_coord:MCVector, end_coord:MCVector):
        """
        This takes a start and end MC World Coordinate (can be the same coordinate for tactile button) and stores input block range as start and end coordinates of input
        
        start_coord:            MCWorldVec      Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec      End coordinate (MC World Coordinate) for input block range
        """
        self._start_block=start_coord
        self._end_block=end_coord
        self._constructVirtualPadFromEndBlocks()

    def getBlockRange(self):
        """nparray of MCVectors is returned in a list -->  [nparray([MCVector, MCVector, ... , MCVector])]"""
        return self._block_array


class TactileInput(InputInterface):

    def __init__(self, MC:[Minecraft], start_coord:MCVector, end_coord:MCVector):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input

        MC:                     [mcpi.Minecraft]    The mcpi connection instance (mutable)
        start_coord:            MCVector      Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCVector      End coordinate (MC World Coordinate) for input block range
        """
        #convert World to mcpi Vecs
        self._start_block = start_coord
        self._end_block = end_coord      
        assert self._end_block.get_MCWorld_Vec().y==self._end_block.get_MCWorld_Vec().y, f"virtual input pad must be defined on a flat plane where start and end y block coordinates are the same"
        self._MC = MC[0]
        self._pressed=False
        self._constructVirtualPadFromEndBlocks()

    def scanInput(self):
        player_ids = Minecraft(self._MC).getPlayerEntityIds()
        for player in player_ids:
            tilepos = MCVector.from_MCWorld_Vec(Minecraft(self._MC).entity.getTilePos(player_id))
            
        pass

    def getInputValue():
        pass





