import numpy as np
import math

class MatrixTools:
    pi=3.1415926535

    def getVectorLength(vector):
        """
        Returns the length of a scaled vector
        vector          tuple           This is a 2d vector representing the input vector
        """
        vec_length = math.sqrt(vector[0]**2+vector[1]**2)
        return vec_length

    def getUnitVector(non_unit_vector):
        """
        Returns the unit vector of the input vector
        vector          tuple           This is a 2d vector representing the input vector
        """
        vec_length = MatrixTools.getVectorLength(non_unit_vector)
        out_vec = (non_unit_vector[0]/vec_length, non_unit_vector[1]/vec_length)
        return out_vec

    def rotateVector(deg_theta:float, unit_vector):
        """
        deg_theta       float           This is the the angle to rotate by in degrees.  
        vector          np.array        This is a 2d vector representing the unit vector that needs to be rotated
        """
        rad_theta = MatrixTools.pi/180*deg_theta
        cos_theta = math.cos(rad_theta)
        sin_theta = math.sin(rad_theta)
        rot_matrix = np.array(
            [
                [cos_theta, -1*sin_theta],
                [sin_theta, cos_theta]
            ])
        ret_val = np.matmul(rot_matrix,unit_vector)
        return ret_val

    def getOrthogonalForceVector(non_unit_vector, force:float):
        """
        This method will take a scaled vector input and a force value and provide the scaled orgthogonal force vector.  If the force value is negative, the force vector will be 90 deg CCW from the input vector.  f the force value is positive, the force vector will be 90 deg CW from the input vector.

        non_unit_vector         np.array        2D vector that represents the current direction and magnitude
        force                   float           Negative value is a 90 deg CCW force, Positive is a 90deg CW force.  0 is no lateral force
        """
        force_vec=(0,0)
        if force !=0:
            #non_unit_vector = np.array(non_unit_vector)
            vec_length = MatrixTools.getVectorLength(non_unit_vector)
            force_scalar = force/vec_length
            force_vec = force_scalar*non_unit_vector
            force_length = MatrixTools.getVectorLength(force_vec)
            unit_vec = MatrixTools.getUnitVector(force_vec)
            
            if force<0: 
                #force is 90 deg CCW from input vector
                force_vec = MatrixTools.rotateVector(90, force_vec)
                force_vec=force_vec*force_length
            elif force >0:
                #force is 90 deg CW from input vector
                force_vec = MatrixTools.rotateVector(-90, force_vec)
                force_vec=force_vec*force_length
        return force_vec
