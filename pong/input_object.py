from mcpi.minecraft import Minecraft
from mcpi import vec3
from .vector import MCVector
from .utility import lerp
import numpy as np
import abc



class MCVectorError(RuntimeError):
    pass

class InputScanner():
    """
    Input in pong works in two steps.  First InputScanner will query player locations once each gameloop and store them.  Then InputParserInterace will
    query InputScanner to test player positions with blocks.
    """
    def __init__(self, MC:[Minecraft]):
        self.__player_info={}
        self.__player_ids=[]
        self.__mc_connection = MC[0]

    def getMC_Player_Pos_By_ID(self, player_id):
            temp_tile=self.__mc_connection.entity.getTilePos(player_id)
            tilepos = MCVector.from_mcpi_Vec(
                vec3.Vec3(temp_tile.x, temp_tile.y-1, temp_tile.z))
            return tilepos


    def scanMC_Player_Positions(self):
        try:
            self.__player_ids = self.__mc_connection.getPlayerEntityIds()
        except Exception as e: # happens if there are no players on the server
            self.__player_ids =[]
            self.__player_info={}

        for player in self.__player_ids:
            try:
                tilepos=self.getMC_Player_Pos_By_ID(player)
                self.__player_info.update({player:tilepos})
            except Exception as e:
                print ('Player joined/left unexpectedly.  Skipping this query')
                pass



    def getScannedPlayerIDs(self):
        return self.__player_ids

    def getScannedPlayerPositions(self):
        return self.__player_info


class InputParserInterface(abc.ABC):
    def __init__(self, MC:[Minecraft], scanner:[InputScanner], start_coord:MCVector, end_coord:MCVector):
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
        self._scanner = scanner[0]
        self._constructVirtualPadFromEndBlocks()
        self._concreteInit()
    
    @abc.abstractclassmethod
    def _concreteInit(self):
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
        self._axis = axis
        self._length = abs(blockrange)+1
        #create array of vec3.Vec3 coordinates
        self._block_array = np.empty(self._length, dtype=object)
        for offset,i in zip(range(0,blockrange+increment,increment),range(0,abs(blockrange)+1,1)):
            self._block_array[i]=MCVector.from_MCWorld_Vec(vec3.Vec3(start_block.x+(offset*axis.x), start_block.y+(offset*axis.y), start_block.z+(offset*axis.z)))

    def reset(self):
        self._concreteInit()

    @abc.abstractclassmethod
    def getInputValue(self):
        """
        Get current state of the input controller (from private data)
        """
        pass

    @abc.abstractclassmethod
    def readInputScanner(self):
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


class TactileInputParser(InputParserInterface):
    
    def _concreteInit(self):
        self.__player=False
        self.__player_is_registered=False
        pass

    def readInputScanner(self):
        self.__pressed=False

        # check where each player on the server is standing
        if self.__player_is_registered==True: # only query position of registered player
                player = self.__player
                try: 
                    tilepos = self._scanner.getMC_Player_Pos_By_ID(player)
                except Exception as e:
                    tilepos=self._start_block

                # look through each block in array and see if player is standing on one of them
                for block in self._block_array:
                    if block.isEqual(tilepos):
                        self.__pressed=True
                        break
        else: # query positions of ALL players on the server to see if anyone is standing on this block
            for player in self._scanner.getScannedPlayerIDs():
                #temp_tile=self._MC.entity.getTilePos(player)
                try:
                    tilepos = self._scanner.getScannedPlayerPositions()[player]
                except:
                    tilepos=self._start_block
                
                # look through each block in array and see if player is standing on one of them
                for block in self._block_array:
                    if block.isEqual(tilepos):
                        self.__pressed=True
                        self.__player = player
                        break

    def assignPlayer(self, player=None):
        """
        This function will look at the player currently standing on this tactile block and register future inputs from that user
        player:      int     id of player in the MC server
        
        If this function is not called, then readInputScanner will always read all player positions on the server (slow)
        """
        if player is not None:
            self.__player=player
        self.__player_is_registered=True 

    def getAssignedPlayer(self):
        return self.__player

    def getInputValue(self):
        return self.__pressed

class RangeInputParser(InputParserInterface):

    def _concreteInit(self):
        self.__range_input_val=.5
        self.__last_range_input_val=.5
        self.__player=False
        self.__player_is_registered=False

    def readInputScanner(self):
        #self.__pressed=False

        self.__last_range_input_val=self.__range_input_val

        if self.__player_is_registered==True: # player has been registered..  only query that player's position
            player = self.__player
            tilepos = self._scanner.getMC_Player_Pos_By_ID(player)
            
            # look through each block in array and see if player is standing on one of them
            for block in self._block_array:
                if block.isEqual(tilepos):

                    #take dot product with self._axis of start, end, and tilepos blocks in order to get floats that we can lerp into an input range between 0-1
                    block_pos=(tilepos.get_MCWorld_Vec().x*self._axis.x)+(tilepos.get_MCWorld_Vec().y*self._axis.y)+(tilepos.get_MCWorld_Vec().z*self._axis.z)
                    block_start=(self._start_block.get_MCWorld_Vec().x*self._axis.x)+(self._start_block.get_MCWorld_Vec().y*self._axis.y)+(self._start_block.get_MCWorld_Vec().z*self._axis.z)
                    block_end=(self._end_block.get_MCWorld_Vec().x*self._axis.x)+(self._end_block.get_MCWorld_Vec().y*self._axis.y)+(self._end_block.get_MCWorld_Vec().z*self._axis.z)

                    self.__range_input_val = lerp(start=block_start, end=block_end, pos=block_pos)

                    break
        else: # player has not been registered.  Query ALL player positions on the server
            # check where each player on the server is standing
            for player in self._scanner.getScannedPlayerIDs():
                
                
                tilepos = self._scanner.getScannedPlayerPositions()[player]
                
                # look through each block in array and see if player is standing on one of them
                for block in self._block_array:
                    if block.isEqual(tilepos):

                        #take dot product with self._axis of start, end, and tilepos blocks in order to get floats that we can lerp into an input range between 0-1
                        block_pos=(tilepos.get_MCWorld_Vec().x*self._axis.x)+(tilepos.get_MCWorld_Vec().y*self._axis.y)+(tilepos.get_MCWorld_Vec().z*self._axis.z)
                        block_start=(self._start_block.get_MCWorld_Vec().x*self._axis.x)+(self._start_block.get_MCWorld_Vec().y*self._axis.y)+(self._start_block.get_MCWorld_Vec().z*self._axis.z)
                        block_end=(self._end_block.get_MCWorld_Vec().x*self._axis.x)+(self._end_block.get_MCWorld_Vec().y*self._axis.y)+(self._end_block.get_MCWorld_Vec().z*self._axis.z)

                        self.__range_input_val = lerp(start=block_start, end=block_end, pos=block_pos)

                        break

    def assignPlayer(self, player=None):
        """
        This function will look at the player currently standing on this tactile block and register future inputs from that user
        player:      int     id of player in the MC server
        
        If this function is not called, then readInputScanner will always read all player positions on the server (slow)
        """
        if player is not None:
            self.__player=player
        self.__player_is_registered=True 

    def getAssignedPlayer(self):
        return self.__player

    def getInputValue(self):
        return self.__range_input_val

    def getLastInputValue(self):
        return self.__last_range_input_val




