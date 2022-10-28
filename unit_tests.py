import unittest
import numpy as np
import pickle
from pong import utility
from mcpi.minecraft import Minecraft
from pong.render import Color
from pong.render import Screen
from pong.render import PixelArray
from pong.render import Clipper
from pong.render import Painter


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
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)


# assert val 2
assert_val=np.array([
    [4,5,6],
    [7,8,10],
    [11,12,13]
])
sprite_start_pos=(3,-1)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)


# assert val 3
assert_val=np.array([
    []
])
sprite_start_pos=(-5,4)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)



# assert val 4
assert_val=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10],
    [11,12,13]
])
sprite_start_pos=(1,3)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)



# assert val 5
assert_val=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10],
    [11,12,13]
])
sprite_start_pos=(5,3)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)


# assert val 6
assert_val=np.array([
    []
])
sprite_start_pos=(10,3)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)


# assert val 7
assert_val=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,10],
    [11,12,13]
])
sprite_start_pos=(0,7)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)


# assert val 8
assert_val=np.array([
    [1,2],
    [4,5],
    [7,8]
])
sprite_start_pos=(6,9)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)



# assert val 9
assert_val=np.array([
    [3]
])
sprite_start_pos=(-2,11)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)


# assert val 10
assert_val=np.array([
    []
])
sprite_start_pos=(3,12)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)


# assert val 11
assert_val=np.array([
    []
])
sprite_start_pos=(2,16)
clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)


data=PixelArray(np.array([[]]))


data = PixelArray(np.array(
    [
        [1,0,5],
        [0,2,3],
        [0,4,0]
    ]
))


this=data.getPoint(0,2)
this=data.getPoint(2,1)
this=data.getPoint(0,0)
data.setPoint(0,0,7)
data.setPoint(0,1,9)
this=data.getPoint(0,0)
this=data.getPoint(0,1)



my_file= open( "server.pkl", "rb" ) 
server_ip, server_port = pickle.load(my_file)
my_file.close()
mc = Minecraft.create(server_ip,server_port)
top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
my_screen = Screen([mc],top_left_screen_coord,8,12)        


sprite=PixelArray(np.array(
    [
        [3,4,5],
        [6,7,8],
        [9,10,11],
        [12,13,14]
    ]
))

sprite_start_pos=(2,1)

assert_val=np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 4, 5, 0, 0, 0],
        [0, 0, 6, 7, 8, 0, 0, 0],
        [0, 0, 0,10,11, 0, 0, 0],
        [0, 0,12,13,14, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
)
my_screen.drawObject(sprite,sprite_start_pos)
data = my_screen.getBackVirtualPage()



my_big_screen = Screen([mc], top_left_screen_coord,8,16)


this_sprite = PixelArray(
    np.array([
        [1,2,3],
        [4,5,6],
        [7,8,10],
        [11,12,13]        
    ])
)
sprite_start_pos=(1,3)

clipped_sprite, clipped_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite,sprite_start_pos)
my_big_screen.fill(2)
my_big_screen.flipVirtualPage()
my_big_screen.fill(1)
my_big_screen.flipVirtualPage()
my_big_screen.drawObject(clipped_sprite, clipped_start_pos)

my_painter = Painter([my_big_screen])


print("Hello Minecraft!")