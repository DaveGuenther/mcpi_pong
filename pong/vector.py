from mcpi import vec3
import numpy as np

class Vector:
    __world_to_mcpi = vec3.Vec3(-32,66,128)

    def __init__(self, world_vec3, mcpi_vec3):
        self.__world_vec=world_vec3
        self.__mcpi_vec=mcpi_vec3

    @classmethod
    def from_MCWorldXYZ(cls, x,y,z):
        world_vec = vec3.Vec3(x,y,z)
        mcpi_vec=Vector.__world_to_mcpi(world_vec)
        return cls(world_vec, mcpi_vec)

    @classmethod
    def from_mcpiXYZ(cls, x,y,z):
        mcpi_vec = vec3.Vec3(x,y,z)
        world_vec=Vector.__mcpi_to_world(world_vec)
        return cls(world_vec, mcpi_vec)



    def __mcpi_to_world(mcpi_vec):
        world_vec = vec3.Vec3(
            mcpi_vec.x+self.__world_to_mcpi.x,
            mcpi_vec.y+self.__world_to_mcpi.y,
            mcpi_vec.z+self.__world_to_mcpi.z
        )

        return world_vec    

    def __world_to_mcpi(world_vec):
        mcpi_vec = vec3.Vec3(
            mcpi_vec.x-self.__world_to_mcpi.x,
            mcpi_vec.y-self.__world_to_mcpi.y,
            mcpi_vec.z-self.__world_to_mcpi.z
        )
        return mcpi_vec