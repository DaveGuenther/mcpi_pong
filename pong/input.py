from mcpi.minecraft import Minecraft
from mcpi import vec3
from pong.vector import MCVector
import abc

class InputInterface(abc.ABC):
    @abc.abstractclassmethod
    def __init__(start_coord, end_coord):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        start_coord:            MCWorldVec      Start coordinate (MC World Coordinate) for input block range
        end_coord:              MCWorldVec      End coordinate (MC World Coordinate) for input block range
        """
        pass

    @abc.abstractclassmethod
    def getPressed():
        pass

    @abc.abstractclassmethod
    def scanInput():
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

    @abc.abstractclassmethod
    def getBlockRange():
        pass


class TactileInput(InputInterface):

    def __init__(start_coord, end_coord):
        """
        This takes a start and end MC World Coordinate (can be the same coordinage for tactile button) and stores input block range as start and end coordinates of input
        
        start_coord:            Vector      Start coordinate (MC World Coordinate) for input block range
        end_coord:              Vector      End coordinate (MC World Coordinate) for input block range
        """
        #convert World to mcpi Vecs
        self._start_block = start_coord
        self._end_block = end_coord
        self._pressed=False

    def getPressed():
        pass

    def scanInput():
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