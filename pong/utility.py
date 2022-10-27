from mcpi import vec3
import numpy as np

def get_world_coords_from_mcpi_vec(this_vec):
    this_vec.x-=32
    this_vec.y+=66
    this_vec.z+=128
    return vec3.Vec3(x,y,z)    

def get_mcpi_vec_from_world_coords(x, y, z):
    x+=32
    y-=66
    z-=128
    return vec3.Vec3(x,y,z)    

