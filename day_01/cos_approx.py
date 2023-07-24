#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Qusai Al Shidi'
__email__ = 'qusai@umich.edu'

from math import factorial
from math import pi
# import numpy as np


def cos_approx(x, accuracy=10):
    """
    Put the definition here
    """
    
    cosine = [(((-1)**n)/factorial(2*n))*(x**(2*n)) for n in range(accuracy)] 
    return sum(cosine)


    # Alternative method (using numpy):
    # test = []
    # for n in range(accuracy):
    #     numerator_1 = (-1)**n
    #     denominator = factorial(2*n)
    #     numerator_2 = x**(2*n)
    #     cosine = (numerator_1*numerator_2)/denominator
    #     test.append(cosine)
        
    # return sum(np.array(test))
        

# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
