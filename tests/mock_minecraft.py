from pong.vector import MCVector
from mcpi import vec3


class Minecraft:
    #used only by unittest to create Faux MineCarft instance so we can test server communications in a black box without a running server

    class FauxEntity:
        def __init__(self):
            self.player_pos = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39962))

        def getTilePos(self, player):
            
            return self.player_pos.get_mcpiVec()

    def __init__(self,server_ip,server_port):
        self.entity = Minecraft.FauxEntity()

    @classmethod
    def create(cls, server_ip, server_port):
        return cls(server_ip, server_port)

    def getPlayerEntityIds(self):
        return [0,1]

    def setBlock(self, x,y,z,color):
        print("setBlock: ", x, y, z, " color: ",color)

    class conn:
        class socket:
            def close():
                pass
