import numpy as np
from pong.matrix_tools import MatrixTools





my_vec = np.array([0,3])
print(my_vec)
my_vec_length = MatrixTools.getVectorLength(my_vec)
my_vec = MatrixTools.getUnitVector(my_vec)
my_vec = MatrixTools.rotateVector(-90.0, my_vec)
my_vec = my_vec*my_vec_length
print(my_vec)

my_vec = np.array([0.01,6.01])
my_force_vec = MatrixTools.getOrthogonalForceVector(my_vec, 1)
my_vec = my_vec+my_force_vec
my_vec = MatrixTools.getUnitVector(my_vec)
print(my_vec)

#my_vec_length = getVectorLength(my_vec)


my_vec = MatrixTools.rotateVector(-90.0, my_vec)
my_vec = my_vec*my_vec_length
print(my_vec)


