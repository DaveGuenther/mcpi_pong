
import numpy as np
import pickle
from pong.render import PixelArray

p1_waiting = PixelArray(np.array(
    [
        [9,2,2,2,9],
        [2,9,9,9,2],
        [9,9,9,9,2],
        [9,9,9,9,2],
        [9,9,9,2,9],
        [9,9,2,9,9],
        [9,9,2,9,9],
        [9,9,9,9,9],
        [9,9,2,9,9]
    ]
))

pickle.dump(p1_waiting,open( 'p1_waiting.pkl', "wb" ))

p2_waiting = PixelArray(np.array(
    [
        [ 9,15,15,15, 9],
        [15, 9, 9, 9,15],
        [ 9, 9, 9, 9,15],
        [ 9, 9, 9, 9,15],
        [ 9, 9, 9,15, 9],
        [ 9, 9,15, 9, 9],
        [ 9, 9,15, 9, 9],
        [ 9, 9, 9, 9, 9],
        [ 9, 9,15, 9, 9]
    ]
))
pickle.dump(p2_waiting,open( 'p2_waiting.pkl', "wb" ))


p1_loaded = PixelArray(np.array(
    [
        [ 9, 9, 2, 9, 9],
        [ 9, 2, 2, 2, 9],
        [ 9, 2, 2, 2, 9],
        [ 9, 9, 2, 9, 9],
        [ 9, 2, 2, 2, 9],
        [ 2, 9, 2, 9, 2],
        [ 2, 9, 2, 9, 2],
        [ 9, 9, 2, 9, 9],
        [ 9, 2, 9, 2, 9],
        [ 2, 2, 9, 2, 2]
    ]
))

pickle.dump(p1_loaded,open( 'p1_loaded.pkl', "wb" ))

p2_loaded = PixelArray(np.array(
    [
        [ 9, 9,15, 9, 9],
        [ 9,15,15,15, 9],
        [ 9,15,15,15, 9],
        [ 9, 9,15, 9, 9],
        [ 9,15,15,15, 9],
        [15, 9,15, 9,15],
        [15, 9,15, 9,15],
        [ 9, 9,15, 9, 9],
        [ 9,15, 9,15, 9],
        [15,15, 9,15,15]
    ]
))

pickle.dump(p2_loaded,open( 'p2_loaded.pkl', "wb" ))

