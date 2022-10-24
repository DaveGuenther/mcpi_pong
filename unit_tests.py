import unittest
import numpy as np
from pong.utility import PixelArray
from pong.render import Color

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