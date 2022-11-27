
from mcpi.minecraft import Minecraft
from mcpi import vec3
from mcpi import block
import pickle
import math
import numpy as np
from pong.render import Screen
from pong import utility
import time
from pong.mcpi_block_structure.blockstructure import BlockStructure

server_ip, server_port = pickle.load(open( "server.pkl", "rb" ) )
mc = Minecraft.create(server_ip,server_port)
print(type(mc))

# These vectors are all in world space
top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display..  Display is facing west
screen_nw_bot_corner = utility.get_mcpi_vec_from_world_coords(39562,74,39957) # Monitor(display) Bottom NW Corner
p1_paddle_nw_bot_corner = utility.get_mcpi_vec_from_world_coords(39522, 78, 39954) # Player 1 paddle
p2_paddle_nw_bot_corner = utility.get_mcpi_vec_from_world_coords(39522, 78, 39968) # player 2 paddle



# paddle storage

my_paddle = BlockStructure(mc)
start_vec = my_paddle.get_mcpi_vec_from_world_coords(39522, 87, 39968)
end_vec = my_paddle.get_mcpi_vec_from_world_coords(39538, 97, 39977)


my_paddle.get_structure(start_vec, end_vec)

my_paddle.write_to_file("p2_paddle.pkl")


my_paddle = BlockStructure(mc)
start_vec = my_paddle.get_mcpi_vec_from_world_coords(39522, 87, 39954)
end_vec = my_paddle.get_mcpi_vec_from_world_coords(39538, 97, 39963)


my_paddle.get_structure(start_vec, end_vec)

my_paddle.write_to_file("p1_paddle.pkl")



#screen storage
my_screen_object = BlockStructure(mc)
start_vec = screen_nw_bot_corner
end_vec = utility.get_mcpi_vec_from_world_coords(39563,107,39974)
my_screen_object.get_structure(start_vec, end_vec)
my_screen_object.write_to_file("my_screen.pkl")

#paddle = BlockStructure(mc)
#paddle.read_from_file(filename="my_paddle.pkl")
#p1_paddle_nw_bot_corner = vec3.Vec3(39522, 78, 39954) # Player 1 paddle
#p1_paddle_nw_bot_corner = paddle.get_mcpi_vec_from_world_vec(p1_paddle_nw_bot_corner)

#paddle.set_structure(p1_paddle_nw_bot_corner)

#screen = BlockStructure(mc)
#screen.read_from_file("screen.pkl")
#screen.set_structure(start_vec)