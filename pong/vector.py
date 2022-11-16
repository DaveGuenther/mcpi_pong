from mcpi import vec3
import numpy as np
import constant

class Vector:
    world_to_mcpi_offset = constant.Constant(vec3.Vec3(-32,66,128))

    def __init__(self, world_vec3, mcpi_vec3):
        self.__world_vec=world_vec3
        self.__mcpi_vec=mcpi_vec3

    @classmethod
    def from_MCWorld_XYZ(cls, x,y,z):
        world_vec = vec3.Vec3(x,y,z)
        mcpi_vec=Vector.__world_to_mcpi(Vector,world_vec)
        return cls(world_vec, mcpi_vec)

    @classmethod
    def from_mcpi_XYZ(cls, x,y,z):
        mcpi_vec = vec3.Vec3(x,y,z)
        world_vec=Vector.__mcpi_to_world(Vector,mcpi_vec)
        return cls(world_vec, mcpi_vec)

    @classmethod
    def from_MCWorld_Vec(cls, world_vec):
        mcpi_vec=Vector.__world_to_mcpi(Vector,world_vec)
        return cls(world_vec, mcpi_vec)

    @classmethod
    def from_mcpi_Vec(cls, mcpi_vec):
        world_vec=Vector.__mcpi_to_world(Vector,mcpi_vec)
        return cls(world_vec, mcpi_vec)

    def __mcpi_to_world(self, mcpi_vec):
        world_vec = vec3.Vec3(
            mcpi_vec.x+Vector.world_to_mcpi_offset.get().x,
            mcpi_vec.y+Vector.world_to_mcpi_offset.get().y,
            mcpi_vec.z+Vector.world_to_mcpi_offset.get().z
        )

        return world_vec    

    def __world_to_mcpi(self, world_vec):
        mcpi_vec = vec3.Vec3(
            world_vec.x-Vector.world_to_mcpi_offset.get().x,
            world_vec.y-Vector.world_to_mcpi_offset.get().y,
            world_vec.z-Vector.world_to_mcpi_offset.get().z
        )
        return mcpi_vec
    
    def set_MCWorld_XYZ(self, x,y,z):
        self.__world_vec = vec3.Vec3(x,y,z)
        self.__mcpi_vec=Vector.__world_to_mcpi(self.__world_vec)

    def set_mcpi_XYZ(self, x,y,z):
        self.__mcpi_vec = vec3.Vec3(x,y,z)
        self.__world_vec=Vector.__mcpi_to_world(self.__mcpi_vec)

    def set_MCWorld_XYZ(self, world_vec):
        self.__mcpi_vec=Vector.__world_to_mcpi(world_vec)
        self.__world_to_mcpi=world_vec

    def set_mcpi_Vec(self, mcpi_vec):
        self.__world_vec=Vector.__mcpi_to_world(mcpi_vec)
        self.__mcpi_vec=mcpi_vec

    def get_mcpiVec(self):
        return self.__mcpi_vec

    def get_MCWorld_Vec(self):
        return self.__world_vec



print(Vector.world_to_mcpi_offset)
my_world_vec = Vector.from_mcpi_XYZ(1,1,1)
my_mcpi_vec = Vector.from_MCWorld_XYZ(
    my_world_vec.get_MCWorld_Vec().x, 
    my_world_vec.get_MCWorld_Vec().y, 
    my_world_vec.get_MCWorld_Vec().z)
my_vec = vec3.Vec3(1,1,1)
my_world_vec2 = Vector.from_mcpi_Vec(my_vec)
my_mcpi_vec2 = Vector.from_MCWorld_Vec(
    vec3.Vec3(
        my_world_vec.get_MCWorld_Vec().x, 
        my_world_vec.get_MCWorld_Vec().y, 
        my_world_vec.get_MCWorld_Vec().z))
print("All Done")