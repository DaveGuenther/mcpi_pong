import unittest
from pong import utility
from pong.vector import MCVector
from mcpi import vec3
from pong import input

#used to create Faux MineCarft instance so we can test server communications in a black box without a running server
class Minecraft:

    class FauxEntity:
        def __init__(self):
            self.player_pos = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39962))

        def getTilePos(self, player):
            
            return self.player_pos.get_mcpiVec()
    
        

    def __init__(self):
        self.entity = Minecraft.FauxEntity()

    def getPlayerEntityIds(self):
        return [0,1]

# test cases
class TestInput(unittest.TestCase):
    def testInputSingleBlock(self):
        """
        Tests for TactileInput or RangeInput instances of a single block.  Passes if instance is created     
        start_block(x,y,z)
        end_block(x,y,z)           
        """

        pass

    def testInputBlockLineX(self):

        """
        Tests for TactileInput or RangeInput instances of a line of blocks along the x axis. Passes if instance is created
        start_block(x1,y,z)
        end_block(x2,y,z)
        """
        pass    

    def testInputBlockLineZ(self):

        """
        Tests for TactileInput or RangeInput instances of a line of blocks along the z axis. Passes if instance is created
        start_block(x,y,z1)
        end_block(x,y,z2)
        """
        pass

    def testInputPlaneXZ(self):

        """
        Tests for TactileInput or RangeInput instances of a plane of blocks along the XZ plane. Passes if instance fails to be create
        start_block(x1,y,z1)
        end_block(x2,y,z2)
        """
        pass    

    def testInputBlockLineY(self):

        """
        Tests for TactileInput or RangeInput instances of a line of blocks along the Y axis. Passes if instance fails to be create
        start_block(x,y1,z)
        end_block(x,y2,z)
        """
        pass  

    def testInputCuboid(self):

        """
        Tests for TactileInput or RangeInput instances of a cuboid of blocks. Passes if instance fails to be create
        start_block(x1,y1,z1)
        end_block(x1,y2,z2)
        """
        pass  

    def testRangeInputInstance(self):

        player_id = 0  #just need some integer here
        start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))
        end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39962))

        mc = Minecraft()
        mc.entity.player_pos=MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39955)) # player at start of platform
        my_controller = input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord)
        my_controller.scanInput()
        lerp_val=my_controller.getInputValue()
        self.assertAlmostEqual(lerp_val, 0.0)

        mc.entity.player_pos=MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39962)) # player at end of platform
        my_controller.scanInput()
        lerp_val=my_controller.getInputValue()
        self.assertAlmostEqual(lerp_val, 1.0)

        mc.entity.player_pos=MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39958)) # player somewhere near middle of controller
        my_controller.scanInput()
        lerp_val=my_controller.getInputValue()
        self.assertAlmostEqual(lerp_val, 0.42857142)
                
        pass


if __name__ == '__main__':
    unittest.main()