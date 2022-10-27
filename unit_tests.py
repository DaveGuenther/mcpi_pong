import unittest
import numpy as np
import pickle
from pong import utility
from mcpi.minecraft import Minecraft
from pong.render import Color
from pong.render import Screen
from pong.render import PixelArray
from pong.render import Clipper


my_pickle = open( "server.pkl", "rb" )
server_ip, server_port = pickle.load(my_pickle)
my_pickle.close()

mc = Minecraft.create(server_ip,server_port)
top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display

this_screen = Screen([mc],top_left_screen_coord,8,12)
my_clipper = Clipper([this_screen])        
# Create Sprite
my_sprite_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10],
    [11,12,13]
])

this_sprite = PixelArray(my_sprite_array)

# assert val 1
assert_val=np.array([
    [6],
    [10],
    [13]
])

sprite_start_pos=(-2,-1)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)


# assert val 2
assert_val=np.array([
    [4,5,6],
    [7,8,10],
    [11,12,13]
])
sprite_start_pos=(3,-1)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)


# assert val 3
assert_val=np.array([
    []
])
sprite_start_pos=(-5,4)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)



# assert val 4
assert_val=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10],
    [11,12,13]
])
sprite_start_pos=(1,3)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)



# assert val 5
assert_val=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10],
    [11,12,13]
])
sprite_start_pos=(5,3)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)


# assert val 6
assert_val=np.array([
    []
])
sprite_start_pos=(10,3)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)


# assert val 7
assert_val=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10],
    [11,12,13]
])
sprite_start_pos=(0,7)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)


# assert val 8
assert_val=np.array([
    [1,2],
    [4,5],
    [7,8]
])
sprite_start_pos=(6,9)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)



# assert val 9
assert_val=np.array([
    [3]
])
sprite_start_pos=(-2,11)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)


# assert val 10
assert_val=np.array([
    []
])
sprite_start_pos=(3,12)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)


# assert val 11
assert_val=np.array([
    []
])
sprite_start_pos=(2,16)
clipped_sprite, sprite_start_pos = my_clipper.clip_object_with_screen_edges(this_sprite, sprite_start_pos)


data=PixelArray(np.array([[]]))

print("Hello Minecraft!")