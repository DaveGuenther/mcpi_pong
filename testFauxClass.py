from pong.vector import MCVector
from pong import input
from mcpi import vec3

class Minecraft:

    class FauxEntity:
        def __init__(self):
            self.player_pos = MCVector.from_MCWorld_Vec(vec3.Vec3(0,0,0))

        def getTilePos(self, player):
            
            return self.player_pos.get_mcpiVec()
    
        

    def __init__(self):
        self.entity = Minecraft.FauxEntity()

    def getPlayerEntityIds(self):
        return [0,1]

start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 83, 39955))
end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 83, 39962))
mc = Minecraft()
mc.entity.player_pos=MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39955)) # player at start of platform
my_controller = input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord)
my_controller.scanInput()
print(my_controller.getInputValue())
mc.entity.getTilePos(10)
mc.entity.player_pos=MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39962))
mc.entity.getTilePos(10)
print("Awesome")
