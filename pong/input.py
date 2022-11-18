from mcpi.minecraft import Minecraft
from mcpi import vec3
from .vector import MCVector
import abc

class InputInterface(abc.ABC):
    @abc.abstractclassmethod
    def __init__(MC,start_coord, end_coord):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        MC:                     [mcpi.Minecraft]    The mcpi connection instance (mutable)
        start_coord:            MCWorldVec          Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec          End coordinate (MC World Coordinate) for input block range
        """
        pass

    @abc.abstractclassmethod
    def _constructVirtualPadFromEndBlocks():
        """
        Pads can be defined with arbitrary dimensions.  While we hope they exist as a single slick or a line of blocks, we will define them as planes with two corner blocks (start_block_ and end_block).  This function will build an np.array of MCVectors that contains all the blocks in the virtual pad, which is an xy plane.
        """
        pass

    @abc.abstractclassmethod
    def getPressed():
        """
        Get current state of the input controller (from private data)
        """
        pass

    @abc.abstractclassmethod
    def scanInput():
        """
        Get input data by querying MC
        """
        pass

    @abc.abstractclassmethod
    def getBlockRange():
        pass

    @abc.abstractclassmethod
    def setBlockRange(start_coord, end_coord):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        start_coord:            MCWorldVec      Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec      End coordinate (MC World Coordinate) for input block range
        """
        pass

    def _vec_swap(vec_1, vec_2):
        temp=vec_1
        vec_1=self.vec_2
        vec_2=temp
        return (vec1, vec2)

    @abc.abstractclassmethod
    def getBlockRange():
        pass


class TactileInput(InputInterface):

    def __init__(MC:[Minecraft], start_coord:MCVector, end_coord:MCVector):
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

    def _constructVirtualPadFromEndBlocks():
        """
        Pads can be defined with arbitrary dimensions.  While we hope they exist as a single slick or a line of blocks, we will define them as planes with two corner blocks (start_block_ and end_block).  This function will build an np.array of MCVectors that contains all the blocks in the virtual pad, which is an xy plane.
        """
        #re-order blocks so that start block is less or equal to end block
        if self._end_block.x<self._start_block.x: 
            self._start_block, self._end_block=self._vec_swap(self._start_block, self._end_block)
        if self._end_block.y<self._start_block.y:
            self._start_block, self._end_block=self._vec_swap(self._start_block, self._end_block)

        x_range = self._end_block.x - self._start_block.x+1
        y_range = self._end_block.y-self._start_block.y+1



    def getPressed():
        """
        
        """
        pass

    def scanInput():
        player_ids = Minecraft(self._MC).getPlayerEntityIds()
        for player in player_ids:
            tilepos = MCVector.from_MCWorld_Vec(Minecraft(self._MC).entity.getTilePos(player_id))
            
        pass

    def getBlockRange():
        pass

    def setBlockRange(start_coord, end_coord):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        start_coord:            MCWorldVec      Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec      End coordinate (MC World Coordinate) for input block range
        """
        pass

    def getBlockRange():
        pass


