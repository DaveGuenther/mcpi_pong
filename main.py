from mcpi.minecraft import Minecraft
from mcpi import vec3
from mcpi import block
from mcpi_block_structure.blockstructure import BlockStructure
import pickle
import math
import numpy as np
from pong.render import Screen
from pong import utility
import time

server_ip, server_port = pickle.load(open( "server.pkl", "rb" ) )
mc = Minecraft.create(server_ip,server_port)
print(type(mc))

# These vectors are all in world space
top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display..  Display is facing west
screen_nw_bot_corner = utility.get_mcpi_vec_from_world_coords(39562,74,39957) # Monitor(display) Bottom NW Corner
p1_paddle_nw_bot_corner = utility.get_mcpi_vec_from_world_coords(39522, 78, 39954) # Player 1 paddle
p2_paddle_nw_bot_corner = utility.get_mcpi_vec_from_world_coords(39522, 78, 39968) # player 2 paddle


paddle1 = BlockStructure(mc)
paddle1.read_from_file("assets/paddle.pkl")
paddle1.set_structure(p1_paddle_nw_bot_corner)

paddle2 = BlockStructure(mc)
paddle2.read_from_file("assets/paddle.pkl")
paddle2.set_structure(p2_paddle_nw_bot_corner)

screen_obj = BlockStructure(mc)
screen_obj.read_from_file("assets/screen.pkl")
screen_obj.set_structure(screen_nw_bot_corner)

my_screen = Screen([mc], top_left_screen_coord,16,32)
