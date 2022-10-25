import unittest
import numpy as np
import pickle
from pong import utility
from mcpi.minecraft import Minecraft
from pong.render import Color
from pong.render import Screen
from pong.render import PixelArray

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


print("Hello Minecraft!")