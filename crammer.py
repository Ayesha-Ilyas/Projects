import numpy as np
import Cramer

def test_Cramer():
    L = [2, 3, 0, 5,
         1, 1, 1, 3,
         2,-1, 3, 7]
    A = np.array(L)
    A.shape = (3,4)
    result = Cramer.solve(A)
    if result:
        x,y,z = result
        print( 'solution')
        print ('x =', x)
        print ('y =', y)
        print ('z =', z, '\n')
        Cramer.check(A,x,y,z)

test_Cramer()