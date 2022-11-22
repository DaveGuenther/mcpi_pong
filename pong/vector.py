from mcpi import vec3
import numpy as np
from . import constant

class MCVector:
    WORLD_TO_MCPI_OFFSET = constant.Constant(vec3.Vec3(-32,66,128))

    def __init__(self, world_vec3, mcpi_vec3):
        self.__world_vec=world_vec3
        self.__mcpi_vec=mcpi_vec3

    @classmethod
    def from_MCWorld_XYZ(cls, x,y,z):
        world_vec = vec3.Vec3(x,y,z)
        mcpi_vec=MCVector.__world_to_mcpi(MCVector,world_vec)
        return cls(world_vec, mcpi_vec)

    @classmethod
    def from_mcpi_XYZ(cls, x,y,z):
        mcpi_vec = vec3.Vec3(x,y,z)
        world_vec=MCVector.__mcpi_to_world(MCVector,mcpi_vec)
        return cls(world_vec, mcpi_vec)

    @classmethod
    def from_MCWorld_Vec(cls, world_vec):
        mcpi_vec=MCVector.__world_to_mcpi(MCVector,world_vec)
        return cls(world_vec, mcpi_vec)

    @classmethod
    def from_mcpi_Vec(cls, mcpi_vec):
        world_vec=MCVector.__mcpi_to_world(MCVector,mcpi_vec)
        return cls(world_vec, mcpi_vec)

    def __mcpi_to_world(self, mcpi_vec):
        world_vec = vec3.Vec3(
            mcpi_vec.x+MCVector.WORLD_TO_MCPI_OFFSET.get().x,
            mcpi_vec.y+MCVector.WORLD_TO_MCPI_OFFSET.get().y,
            mcpi_vec.z+MCVector.WORLD_TO_MCPI_OFFSET.get().z
        )

        return world_vec    

    def __world_to_mcpi(self, world_vec):
        mcpi_vec = vec3.Vec3(
            world_vec.x-MCVector.WORLD_TO_MCPI_OFFSET.get().x,
            world_vec.y-MCVector.WORLD_TO_MCPI_OFFSET.get().y,
            world_vec.z-MCVector.WORLD_TO_MCPI_OFFSET.get().z
        )
        return mcpi_vec
    
    def set_MCWorld_XYZ(self, x,y,z):
        self.__world_vec = vec3.Vec3(x,y,z)
        self.__mcpi_vec=self.__world_to_mcpi(self.__world_vec)

    def set_mcpi_XYZ(self, x,y,z):
        self.__mcpi_vec = vec3.Vec3(x,y,z)
        self.__world_vec=self.__mcpi_to_world(self.__mcpi_vec)

    def set_MCWorld_Vec(self, world_vec):
        self.__mcpi_vec=self.__world_to_mcpi(world_vec)
        self.__world_to_mcpi=world_vec

    def set_mcpi_Vec(self, mcpi_vec):
        self.__world_vec=self.__mcpi_to_world(mcpi_vec)
        self.__mcpi_vec=mcpi_vec

    def get_mcpiVec(self):
        return self.__mcpi_vec

    def get_MCWorld_Vec(self):
        return self.__world_vec

    def isEqual(self, other_MCVector):
        """
        Returns true if x, y, and z elements of both vectors match
        """
        return True if (
            (self.get_MCWorld_Vec().x==other_MCVector.get_MCWorld_Vec().x)&
            (self.get_MCWorld_Vec().y==other_MCVector.get_MCWorld_Vec().y)&
            (self.get_MCWorld_Vec().z==other_MCVector.get_MCWorld_Vec().z)) else False


    
