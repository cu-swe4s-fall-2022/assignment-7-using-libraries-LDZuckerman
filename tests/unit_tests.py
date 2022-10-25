import unittest
import random
import numpy as np
import sys
sys.path.append('../')
import data_processor  # nopep8


class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        """Create toy data for tests
        """
        array_5_6 = a = np.empty((5,6))
        np.savetxt("test56.csv", array_5_6, delimiter=",")
        cls.testfile_5_6 = 'test56.csv'

    @classmethod
    def tearDownClass(cls):

        """Get rid of toy data created in setup
        """

    def test_get_random_matrix(cls):

        """Test that get_random_matrix functions correctly
        """

        # positive test: returns data of correct shape
        cls.assertEqual(np.shape(data_processor.get_random_matrix(2, 3)), (2, 3))

        # negative test: does not return data of incorrect shape
        cls.assertNotEqual(np.shape(data_processor.get_random_matrix(2, 3)), (3, 2))

        # check that correct errors are raised
        cls.assertRaises(TypeError, data_processor.get_random_matrix, 'three', 3)
        cls.assertRaises(ValueError, data_processor.get_random_matrix, -2, 3)

    def test_get_file_dimensions(cls):

        """Test that get_file_dimensions functions correctly
        """
        
        # positive test: returns correct shape
        cls.assertEqual(data_processor.get_file_dimensions(cls.testfile_5_6), (5, 6))

        # negative test: does not return data of incorrect shape
        cls.assertNotEqual(data_processor.get_file_dimensions(cls.testfile_5_6), (6, 5))

        # check that correct errors are raised
        cls.assertRaises(FileNotFoundError, data_processor.get_file_dimensions, 'csvDNE.csv')

    def test_write_matrix_to_file(cls):

        """Test that get_file_dimensions functions correctly
        """
        
        # positive test: test that matrix created has the correct dimensions 
        data_processor.write_matrix_to_file(2,3, 'testfile.csv')
        cls.assertEqual(data_processor.get_file_dimensions('testfile.csv'), (2,3))

        # negative test: 
        cls.assertNotEqual(data_processor.get_file_dimensions('testfile.csv'), (3,2))

        # check that correct errors are raised
        cls.assertRaises(TypeError, data_processor.write_matrix_to_file, 'three', 3, 'file.csv')
        cls.assertRaises(ValueError, data_processor.write_matrix_to_file, -2, 3, 'file.csv')
        cls.assertRaises(NameError, data_processor.write_matrix_to_file, -2, 3, file.csv)

if __name__ == '__main__':
    unittest.main()