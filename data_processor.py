import numpy as np
import pandas as pd

def get_random_matrix(num_rows, num_columns):

	try:
		a = np.random.rand(num_rows, num_columns)
	except TypeError:
		raise TypeError('num_rows and num_columns must be ints or floats')
	except ValueError:
		raise ValueError('num_rows and num_columns must be positive int or'
					     + ' float values')

	return a

def get_file_dimensions(file_name):

	try:
		df = pd.read_csv(file_name, header=None)
	except FileNotFoundError:
		raise FileNotFoundError('File '+str(file_name)+' not found')

	return np.shape(df)

def write_matrix_to_file(num_rows, num_columns, file_name):

	if type(file_name) != str:
		raise NameError('file_name must be a string')

	a = get_random_matrix(num_rows, num_columns)

	np.savetxt(file_name, a, delimiter=",")

	return None
