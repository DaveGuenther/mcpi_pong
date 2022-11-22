import unittest
from mcpi import vec3
import numpy as np
from pong.vector import MCVector
from pong.constant import Constant

class TestVector(unittest.TestCase):
    def testVectorFromMCPI_XYZ(self):
        my_world_vec = MCVector.from_mcpi_XYZ(1,1,1)
        self.assertTrue((
            my_world_vec.get_MCWorld_Vec().x,
            my_world_vec.get_MCWorld_Vec().y,
            my_world_vec.get_MCWorld_Vec().z),(33,-65,-127))
        
        my_world_vec.set_mcpi_XYZ(2,2,2)
        self.assertTrue((
            my_world_vec.get_MCWorld_Vec().x,
            my_world_vec.get_MCWorld_Vec().y,
            my_world_vec.get_MCWorld_Vec().z),(34,-64,-126))


    def testVectorFromMCPI_Vec(self):
        my_world_vec = MCVector.from_mcpi_Vec(vec3.Vec3(1,1,1))
        self.assertTrue((
            my_world_vec.get_MCWorld_Vec().x,
            my_world_vec.get_MCWorld_Vec().y,
            my_world_vec.get_MCWorld_Vec().z),(33,-65,-127))

        my_world_vec.set_mcpi_Vec(vec3.Vec3(2,2,2))
        self.assertTrue((
            my_world_vec.get_MCWorld_Vec().x,
            my_world_vec.get_MCWorld_Vec().y,
            my_world_vec.get_MCWorld_Vec().z),(34,-64,-126))

    def testVectorFromWorld_XYZ(self):
        my_mcpi_vec = MCVector.from_MCWorld_XYZ(33,-65,-127)
        self.assertTrue((
            my_mcpi_vec.get_mcpiVec().x,
            my_mcpi_vec.get_mcpiVec().y,
            my_mcpi_vec.get_mcpiVec().z),(1,1,1))
        
        my_mcpi_vec.set_MCWorld_XYZ(34,-64,-126)
        self.assertTrue((
            my_mcpi_vec.get_mcpiVec().x,
            my_mcpi_vec.get_mcpiVec().y,
            my_mcpi_vec.get_mcpiVec().z),(2,2,2))

    def testVectorFromWorld_Vec(self):
        my_mcpi_vec = MCVector.from_MCWorld_Vec(vec3.Vec3(33,-65,-127))
        self.assertTrue((
            my_mcpi_vec.get_mcpiVec().x,
            my_mcpi_vec.get_mcpiVec().y,
            my_mcpi_vec.get_mcpiVec().z),(1,1,1))

        my_mcpi_vec.set_MCWorld_Vec(vec3.Vec3(34,-64,-126))
        self.assertTrue((
            my_mcpi_vec.get_mcpiVec().x,
            my_mcpi_vec.get_mcpiVec().y,
            my_mcpi_vec.get_mcpiVec().z),(2,2,2))

