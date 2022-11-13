import unittest
import numpy as np
from pong.render import PixelArray
import pong.game_object as GO

class TestGameObjectInterface(unittest.TestCase):
    def testInstanceGameObject(self):
        my_sprite = PixelArray(np.array(
            [
                [1,0,5],
                [0,2,3],
                [0,4,0]
            ]
        ))
        my_PC_Minecraft_Controller=None
        my_base_object = GO.GameObject(np.array([0,1]), my_sprite)
        self.assertIsInstance(my_base_object, GO.GameObject)

    def testInstanceMovableVirtualGameObject(self):
        my_sprite = PixelArray(np.array(
            [
                [1,0,5],
                [0,2,3],
                [0,4,0]
            ]
        ))
        my_PC_Minecraft_Controller=None
        my_VirtualObject = GO.MovableVirtualGameObject(np.array([0,1]), my_sprite, 10, np.array([1,0]), 1)
        self.assertIsInstance(my_VirtualObject, GO.MovableVirtualGameObject)

    def testInstanceMovablePhysicalGameObject(self):
        my_sprite = PixelArray(np.array(
            [
                [1,0,5],
                [0,2,3],
                [0,4,0]
            ]
        ))
        my_PC_Minecraft_Controller=None
        my_InputGameObject = GO.MovablePhysicalGameObject(np.array([0,1]), my_sprite, 10, np.array([1,0]), 1, my_PC_Minecraft_Controller)
        self.assertIsInstance(my_InputGameObject, GO.MovablePhysicalGameObject)

    def testGameObjectSetGet(self):
        my_sprite = PixelArray(np.array(
            [
                [1,0,5],
                [0,2,3],
                [0,4,0]
            ]
        ))
        my_PC_Minecraft_Controller=None
        my_base_object = GO.GameObject(np.array([0,1]), my_sprite)
        my_assert_sprite = PixelArray(np.array(
            [
                [1,7,5],
                [7,2,3],
                [7,4,7]
            ]
        ))
        assert_pos=np.array([3,4])
        my_base_object.setCartPos(assert_pos)
        my_base_object.setSprite(my_assert_sprite)
        self.assertTrue((my_base_object.getCartPos()==assert_pos).all()) 
        self.assertTrue((my_base_object.getSprite().getData()==my_assert_sprite.getData()).all())

    def testMovableVirtualGameObjectSetGet(self):
        my_sprite = PixelArray(np.array(
            [
                [1,0,5],
                [0,2,3],
                [0,4,0]
            ]
        ))
        my_PC_Minecraft_Controller=None
        my_VirtualObject = GO.MovableVirtualGameObject(np.array([0,1]), my_sprite, 10, np.array([1,0]), 1)
        my_VirtualObject.setSpeed(5)
        my_VirtualObject.setDirection(np.array([5,3]))
        my_VirtualObject.setLateralForceVector(-0.33)
        self.assertEqual(my_VirtualObject.getLateralForceVector(), -0.33)
        self.assertTrue((my_VirtualObject.getDirection()==np.array([5,3])).all())
        self.assertTrue((my_VirtualObject.getSprite().getData()==my_sprite.getData()).all())
        self.assertTrue((my_VirtualObject.getCartPos()==np.array([0,1])).all())
        self.assertEqual(my_VirtualObject.getSpeed(),5)


    def testMovablePhysicalGameObjectSetGet(self):
        my_sprite = PixelArray(np.array(
            [
                [1,0,5],
                [0,2,3],
                [0,4,0]
            ]
        ))
        my_PC_Minecraft_Controller=None
        my_InputGameObject = GO.MovablePhysicalGameObject(np.array([0,1]), my_sprite, 10, np.array([1,0]), 1, None)
        my_InputGameObject.setSpeed(5)
        my_InputGameObject.setDirection(np.array([5,3]))
        my_InputGameObject.setLateralForceVector(-0.33)
        self.assertEqual(my_InputGameObject.getLateralForceVector(), -0.33)
        self.assertTrue((my_InputGameObject.getDirection()==np.array([5,3])).all())
        self.assertTrue((my_InputGameObject.getSprite().getData()==my_sprite.getData()).all())
        self.assertTrue((my_InputGameObject.getCartPos()==np.array([0,1])).all())
        self.assertEqual(my_InputGameObject.getSpeed(),5)
        self.assertIsNone(my_InputGameObject.getInput())

