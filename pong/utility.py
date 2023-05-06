from mcpi import vec3
import numpy as np
import pickle
from . import constant
WORLD_TO_MCPI_OFFSET = constant.Constant(pickle.load(open( "offset_vector.pkl", "rb" ) ))
def get_world_coords_from_mcpi_vec(this_vec):
    this_vec.x+=WORLD_TO_MCPI_OFFSET.get().x*-1
    this_vec.y+=WORLD_TO_MCPI_OFFSET.get().y*-1
    this_vec.z+=WORLD_TO_MCPI_OFFSET.get().z*-1
    return vec3.Vec3(x,y,z)    

def get_mcpi_vec_from_world_coords(x, y, z):
    x-=WORLD_TO_MCPI_OFFSET.get().x
    y-=WORLD_TO_MCPI_OFFSET.get().y
    z-=WORLD_TO_MCPI_OFFSET.get().z
    return vec3.Vec3(x,y,z)    

def lerp(start, end, pos):
    return float(float(pos-start)/float(end-start))
