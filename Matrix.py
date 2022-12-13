import numpy as np
from pong.matrix_tools import MatrixTools
from pong.coordinate_tools import CoordinateTools
from mcpi.minecraft import Minecraft
from pong.render import Screen
from pong import utility
import pickle

my_file= open( "server.pkl", "rb" ) 
server_ip, server_port = pickle.load(my_file)
my_file.close()
mc = Minecraft.create(server_ip,server_port)
top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display

my_vec = np.array([1,1])
print(my_vec)
my_vec_length = MatrixTools.getVectorLength(my_vec)
my_vec = MatrixTools.getUnitVector(my_vec)
my_vec = MatrixTools.rotateVector(-90.0, my_vec)
my_vec = my_vec*my_vec_length
print(my_vec)

my_vec = np.array([0,1])
my_force_vec = MatrixTools.getOrthogonalForceVector(my_vec, 1)
my_vec = my_vec+my_force_vec
my_vec = MatrixTools.getUnitVector(my_vec)
print(my_vec)

#my_vec_length = getVectorLength(my_vec)

my_vec = MatrixTools.rotateVector(-90.0, my_vec)
my_vec = my_vec*my_vec_length
print(my_vec)

my_screen = Screen([mc],top_left_screen_coord,16,32)
my_coord_tools=CoordinateTools([my_screen])
new_coords = my_coord_tools.cartToScreen(np.array([4,-2]))
print(new_coords)
new_coords = my_coord_tools.screenToCart(np.array([10,14]))
print(new_coords)


from pong.render import PixelArray
import pong.game_object as GO

my_sprite = PixelArray(np.array(
    [
        [1,0,5],
        [0,2,3],
        [0,4,0]
    ]
))
my_PC_Minecraft_Controller=None
my_base_object = GO.GameObject(np.array([0,1]), my_sprite)
my_VirtualObject = GO.MovableVirtualGameObject(np.array([0,1]), my_sprite, 10, np.array([1,0]), 1)
my_InputGameObject = GO.MovablePhysicalGameObject(np.array([0,1]), my_sprite, 10, np.array([1,0]), 1, my_PC_Minecraft_Controller)
print(my_InputGameObject.getCartPos())
print(my_InputGameObject.getDirection())
print(my_InputGameObject.getForceVector())
print(my_InputGameObject.getSpeed())
print(my_InputGameObject.getSprite().toString())
print(my_InputGameObject.getInput())