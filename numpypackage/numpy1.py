#numpy is use working with arrays, and numpy is actually use in across the whole range of science and engineering fields.
#It keeps a fast and efficient ways manipulating arrays and inside the arrays theres a data.

#importing numpy
import numpy as np

def numpy_dimensions():
    #every dimensions
    print('Zero Dimensional Array')
    zero_dim = np.array(47292715)
    print(zero_dim)
    print(f'The dimension of given array is {zero_dim.ndim}\n')

    print('One Dimensional Array')
    array = np.array([1,2,3,4,5]) 
    print(array)
    print(f'The dimension of given array is {array.ndim}\n')

    print('Two Dimensional Array')
    two_dim = np.array([[1,2,3],[4,5,6]])
    print(two_dim)
    print(f'The dimension of given array is {two_dim.ndim}\n')

    print('Three Dimensional Array')
    three_dim = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]]])
    print(three_dim)
    print(f'The dimension of given array is {three_dim.ndim}\n') #to know what dimensional array is used on the given array

if __name__ == "__main__":
    numpy_dimensions()