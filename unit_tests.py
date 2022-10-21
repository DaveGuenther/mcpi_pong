import unittest
import numpy as np
from pong.utility import PixelArray
from pong.render import Color

data = PixelArray(3, 4)
other_data = np.array(
    [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
)
print(data.data)
print(data.data==other_data)
a=Color.get(0)

b=(35,15)
assert a==b,f"not equal"

