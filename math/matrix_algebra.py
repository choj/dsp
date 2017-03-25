# Matrix Algebra
import numpy as np
>>> from numpy import linalg as LA


# define given matrices
A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1],[8],[0],[5]])

# 1. Matrix Dimensions
A.shape
B.shape
C.shape
D.shape
u.shape
w.shape

# 2. Vector Operations
alpha = 6
u + v
u - v
alpha * u
np.dot(u,v)
np.linalg.norm(u)

# 3. Matrix Operations
A + C
A - np.transpose(C)
np.transpose(C) + 3*D
np.dot(B,A)
np.dot(B,np.transpose(A))