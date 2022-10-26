import unittest
import numpy as np
import pickle
from pong import utility
from mcpi.minecraft import Minecraft
from pong.render import Color
from pong.render import Screen
from pong.render import PixelArray
from pong.render import Clipper

data = PixelArray.fromDimensions(3, 4)
other_data = np.array(
    [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
)
more_other_data= np.array(
    [
        [0,0,0],
        [0,2,0],
        [0,0,0]
    ]
)


print(other_data-more_other_data)
a=Color.get(0)

b=(35,15)
assert a==b,f"not equal"


reg= np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [0,0,0]
    ]
)
x = np.array([[1,2,3]])
flip = reg.T

index = np.array([True, True, False])

new_index = np.tile(index,(4,1))
print(new_index)

a = PixelArray(reg,True)
print(a.toString())
b = a.filter(np.array([False, True, True, False]), 0)
print(b.toString())

c= PixelArray(np.array([[0,1,2,3]]),True)
print(c.toString())
d = c.filter([True, True, True, False],1)
print(d.toString())

index = np.append(index,True)
print(index)

my_pickle = open( "server.pkl", "rb" )
server_ip, server_port = pickle.load(my_pickle)
my_pickle.close()

mc = Minecraft.create(server_ip,server_port)
top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
my_screen = Screen([mc],top_left_screen_coord, 16, 32)

my_clipper = Clipper([my_screen])
        
# Create Sprite
my_sprite_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10]
])

this_sprite = PixelArray(my_sprite_array)

# Create top_left assert val
top_left_assert=np.array([
    [5,6],
    [8,10]
])

screen_edge=(0,0)
screen_edge_normal_vec=(1,0) # left
sprite_start_pos=(-1,-1)
clipped_sprite, sprite_start_pos = my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

screen_edge=(0,0)
screen_edge_normal_vec=(0,1) # top
clipped_sprite, sprite_start_pos = my_clipper.clip_sprite_with_single_edge(clipped_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)


# Create Sprite
my_sprite_array=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10]
])

this_sprite = PixelArray(my_sprite_array)

top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
this_screen = Screen([mc],top_left_screen_coord,4,5)
my_clipper = Clipper([this_screen])
#self.assertIs(my_clipper.my_screen, this_screen, f"Screen objects do not occupy same memory address")

# Create top_left assert val
bot_right_assert=np.array([
    [1,2],
    [4,5]
])

screen_edge=(this_screen.getWidth(),0)
screen_edge_normal_vec=(-1,0) # right
sprite_start_pos=(3,4)
clipped_sprite, sprite_start_pos  = my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

screen_edge=(0,this_screen.getHeight())
screen_edge_normal_vec=(0,-1) # bottom
clipped_sprite, sprite_start_pos  = my_clipper.clip_sprite_with_single_edge(clipped_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)




print("Hello Minecraft!")