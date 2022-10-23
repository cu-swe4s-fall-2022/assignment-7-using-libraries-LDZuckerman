import numpy as np
import pandas as pd

def get_random_matrix(num_rows, num_columns):

	try:
		a = np.random.rand(num_rows, num_columns)
	except TypeError:
		raise TypeError('num_rows and num_columns must be ints or floats')
	except ValueError:
		raise ValueError('num_rows and num_columns must be positive int or'
					    +' float values')

	return a

def get_file_dimensions(file_name):
	return (0,0)

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
