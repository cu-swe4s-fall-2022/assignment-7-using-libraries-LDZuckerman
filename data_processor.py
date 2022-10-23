import numpy as np
import pandas as pd

def get_random_matrix(num_rows, num_columns):

	try:
		a = np.random.rand(num_rows, num_columns)
	except (ValueError, TypeError):
		print('num_rows and num_cols must be postive integars (or zero)')

	return a

def get_file_dimensions(file_name):
	return (0,0)

def write_matrix_to_file(num_rows, num_columns, file_name):
	return None
