import os
import numpy as np
from numpy import random as rnd
import matplotlib.pyplot as plt 
rnd.seed()

def print_pretty_2d_array(arr):
	for i in range(arr.shape[0]):
		for j in range(arr.shape[1]):
			print("%3d" % arr[i, j], end = ' ')
		print()

arr1 = 10 * rnd.random(size = (3, 3) )
arr2 = 10 * rnd.random(size = (3, 3) )

filename = "binary_arrays.npz"
np.savez(filename, array_n1 = arr1, array_n2 = arr2)

with np.load(filename) as data:
	x1 = data["array_n1"]
	x2 = data["array_n2"]
	print_pretty_2d_array(x1)
	print_pretty_2d_array(x2)