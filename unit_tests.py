import unittest
import numpy as np
from pong.utility import PixelArray

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