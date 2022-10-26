import numpy as np
import pandas as pd

def get_random_matrix(num_rows, num_columns):

	"""" Create a matrix of random numbers

	Parameters:
    -----------
    num_rows: int
		The number of rows in the matrix
	num_cols: int
		The number of collumns in the matrix

    Returns:
    -------
    a
        The random matrix
	"""

	try:
		a = np.random.rand(num_rows, num_columns)
	except TypeError:
		raise TypeError('num_rows and num_columns must be ints or floats')
	except ValueError:
		raise ValueError('num_rows and num_columns must be positive int or'
					     + ' float values')

	return a

def get_file_dimensions(file_name, has_header):

	"""" Find the dimensions of the array contained in a CSV file

	Parameters:
    -----------
    file_name: string
		The name of the file containing the array
	has_header: True of False
		Whether the first line of the file should be treated as a header

    Returns:
    -------
    shape
        The shape of the array contained in the file
	"""
	if has_header == True:
		header = 0
	elif has_header == False:
		header = None
	else:
		raise ValueError('has_header must be True or False')

	try:
		df = pd.read_csv(file_name, header=None)
	except FileNotFoundError:
		raise FileNotFoundError('File '+str(file_name)+' not found')

	shape = np.shape(df)

	return shape

def write_matrix_to_file(num_rows, num_columns, file_name):

	"""" Write a random matrix to a CSV file

	Parameters:
    -----------
    num_rows: int
		The number of rows in the matrix
	num_cols: int
		The number of collumns in the matrix
	file_name: string
		The name of the file to save the array to 

    Returns:
    -------
    Creates CSV file containing random data array
	"""

	if type(file_name) != str:
		raise NameError('file_name must be a string')

	a = get_random_matrix(num_rows, num_columns)

	np.savetxt(file_name, a, delimiter=",")

	return None
